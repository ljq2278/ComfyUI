import json
import requests
import time
import random
import traceback
import os
from my_workspace.shot.bg_shot.content import bg_shots_all_en
from my_workspace.shot.bg_shot.camera import camera_motion_prompts
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


exp_nm = "campus"

COMFYUI_PATH = "f:/projects/ComfyUI" if is_windows() else "/workspace/ComfyUI"
COMFYUI_URL = "http://127.0.0.1:8188" if is_windows() else "http://127.0.0.1:8190"
process_time = 15 if is_windows() else 20

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + \
    "/my_workspace/workflow/生成参考图像_api.json"  # 你的工作流API格式文件
OUTPUT_VIDEO_DIR = COMFYUI_PATH+"/output/material/bg_image"


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

    save_video_node_id = "9"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = kwargs["output_filename_prefix"]

    posi_prompt_node_id = "16"  # 替换为实际的节点ID
    current_workflow[posi_prompt_node_id]["inputs"]["text"] = kwargs["prompt"]

    return current_workflow


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r', encoding="utf-8") as f:
    base_workflow = json.load(f)


mx_cont = 200
for cont in range(0, mx_cont):
    try:
        prompt_dct = {
           "Style": "Modern high-definition Ghibli animation style, delicate, clean, and bright hand-drawn aesthetics with clear lines and naturally vivid colors. Avoid excessive yellowing or dim tones, ensuring a gentle, transparent, and emotionally rich animation texture."
        }
        content_id = int(random.random()*len(bg_shots_all_en[exp_nm]))
        content = bg_shots_all_en[exp_nm][content_id]
        prompt_dct.update(content)

        camera_motion_id = int(random.random()*len(camera_motion_prompts))
        prompt_dct["Camera Movement"] = camera_motion_prompts[camera_motion_id]

        file_name_prefix = f"""{exp_nm}_content#{content_id}"""

        current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流
        img_ind = int(random.random()*6)
        kwargs = {
            "output_filename_prefix": os.path.join(OUTPUT_VIDEO_DIR, f"{file_name_prefix}"),
            "prompt": f"{prompt_dct}"
        }
        current_workflow = set_workflow(current_workflow, **kwargs)

        print(f"Processing video: {kwargs}")
        result = queue_prompt(current_workflow)
        if result and 'prompt_id' in result:
            prompt_id = result['prompt_id']
            print(f"Queued with prompt_id: {prompt_id}, cont {cont}")
            # 此处可以添加等待任务完成的逻辑，例如轮询 /history/{prompt_id}
        else:
            print(f"Failed to queue {kwargs}")
        print("-" * 30)
        time.sleep(process_time)  # 等待一段时间，避免请求过于频繁，并给ComfyUI一点处理时间
    except Exception as e:
        traceback.print_exc()
        print(f"except: {e}")


print("All videos processed.")
