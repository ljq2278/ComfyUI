import json
import requests
import time
import os
import random
import traceback
import requests
from my_workspace.materials.bg_shots.bg_shots import mv_shots_no_protagonist
import platform

os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''

def is_windows():
    os_name = platform.system()
    if os_name.lower() == 'windows':
        print("当前操作系统为 Windows")
        return True
    elif os_name.lower() == 'linux':
        print("当前操作系统为 Linux")
        return False
    else:
        print(f"当前操作系统为 {os_name}")
        return False

COMFYUI_PATH = "f:/projects/ComfyUI" if is_windows() else "/workspace/ComfyUI"
COMFYUI_URL = "http://127.0.0.1:8188" if is_windows() else  "http://127.0.0.1:8190"
process_time = 60 if is_windows() else 80

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + "/my_workspace/comfy重要工作流/文字生视频吉卜力_api.json"  # 你的工作流API格式文件
OUTPUT_VIDEO_DIR = COMFYUI_PATH + "/output/bg_shots"


def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    try:
        response = requests.post(
            f"{COMFYUI_URL}/prompt", data=data, timeout=60*10)
        response.raise_for_status()  # 如果请求失败则抛出异常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error queuing prompt: {e}")
        # if response:
        #     print(f"Response content: {response.text}")
        return None


def set_workflow(current_workflow, **kwargs):

    save_video_node_id = "6"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["text"] = f"""{kwargs["prompt"]}"""

    save_video_node_id = "7"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["text"] = "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，倒着走"

    # save_video_node_id = "40"  # 替换为实际的节点ID
    # current_workflow[save_video_node_id]["inputs"]["length"] = 49

    save_video_node_id = "50"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = os.path.join(OUTPUT_VIDEO_DIR, f"""res_{kwargs["exp_name"]}_{kwargs["mv_shot_ind"]}""")

    return current_workflow


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r', encoding="utf-8") as f:
    base_workflow = json.load(f)

nm = mv_shots_no_protagonist["name"]
shot_list = mv_shots_no_protagonist["content"]
mv_shots = [(i, v) for i, v in enumerate(shot_list)]

candi_shots = [
    "推镜（DollyIn）：缓慢向前推进镜头",
    "拉镜（DollyOut）：镜头平稳后拉",
    "横移（TrackingShot）",
    "跟随角色（从左往右或从右往左）",
    "升降镜头（CraneShot）：从地面仰拍升起",
    "环绕镜头（360°Orbital）：环绕角色缓慢旋转",
]

mx_cont = 200
cont = 0
while True:
    try:
        current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流
        kwargs = {"exp_name": nm}

        mv_shot_cur = {}
        mv_shot_ind,  mv_shot_content = mv_shots[int(len(mv_shots)*random.random())]
        if mv_shot_content["运镜"]["类型"]=="固定镜头":
            mv_shot_content["运镜"]["类型"] = candi_shots[int(random.random()*len(candi_shots))]
        mv_shot_cur.update(mv_shot_content)
        mv_shot_cur.update({"风格": "Studio Ghibli style"})
        kwargs.update({"prompt": mv_shot_cur, "mv_shot_ind": mv_shot_ind})

        current_workflow = set_workflow(current_workflow, **kwargs)

        print(f"Processing video: {kwargs}")
        result = queue_prompt(current_workflow)
        if result and 'prompt_id' in result:
            cont += 1
            prompt_id = result['prompt_id']
            print(f"Queued with prompt_id: {prompt_id}")
            # 此处可以添加等待任务完成的逻辑，例如轮询 /history/{prompt_id}
        else:
            print(f"Failed to queue {kwargs}")
        print("-" * 30)
        if cont > mx_cont:
            break
        time.sleep(process_time)  # 等待一段时间，避免请求过于频繁，并给ComfyUI一点处理时间
    except Exception as e:
        traceback.print_exc()
        print(f"except: {e}")
print("All videos processed.")
