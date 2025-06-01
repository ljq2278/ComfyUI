import json
import requests
import time
import random
import traceback
import os
from my_workspace.materials.shots.scene import mv_scenes_campus
from my_workspace.materials.shots.act import mv_shots_new
from my_workspace.materials.shots.cloth import clothing_prompts_female
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
COMFYUI_URL = "http://127.0.0.1:8188" if is_windows() else "http://127.0.0.1:8190"
process_time = 80 if  is_windows() else 120

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + \
    "/my_workspace/comfy重要工作流/参考生视频_api.json"  # 你的工作流API格式文件
INPUT_IMAGE_PATH = COMFYUI_PATH+"/my_workspace/control_objs/xiaoling.png"
OUTPUT_VIDEO_DIR = COMFYUI_PATH+"/output/role_shots/campus"


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

    load_image_node_id = "73"  # 替换为实际的节点ID
    current_workflow[load_image_node_id]["inputs"]["image"] = kwargs["ref_img"]

    save_video_node_id = "69"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = kwargs["output_filename_prefix"]

    posi_prompt_node_id = "105"  # 替换为实际的节点ID
    current_workflow[posi_prompt_node_id]["inputs"]["text"] = kwargs["prompt"]
    
    k_sampler_node_id = "108"  # 替换为实际的节点ID
    current_workflow[k_sampler_node_id]["inputs"]["seed"] = int(random.random()*10000000000)

    return current_workflow


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r', encoding="utf-8") as f:
    base_workflow = json.load(f)

iter_tt = 200
cont = 0
for it_cnt in range(0, iter_tt):
    mv_shots = [(i, v) for i, v in enumerate(mv_shots_new)]
    random.shuffle(mv_shots)
    for act_ind, itm in mv_shots:
        try:
            prompt_dct = {
                "风格": "现代高清的吉卜力动画风格，细腻、干净、明亮的手绘风格，线条清晰，色彩鲜明自然，避免过度泛黄或昏暗，整体呈现温柔、通透且富有情感的动画质感。",
                "少女": "蓝色眼睛，黄色长发，白皮肤，",
            }

            cloth_ind = int(random.random()*len(clothing_prompts_female))
            cloth_content = clothing_prompts_female[cloth_ind]
            prompt_dct["少女"] += cloth_content

            scene_ind = int(random.random()*len(mv_scenes_campus))
            scene_content = mv_scenes_campus[scene_ind]
            prompt_dct.update({"场景": scene_content})

            file_name_prefix = f"""{act_ind}_{cloth_ind}_{scene_ind}"""
            prompt_dct.update({k: v for k, v in itm.items() if k != "id"})

            current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流
            kwargs = {
                "ref_img": INPUT_IMAGE_PATH,
                "output_filename_prefix": os.path.join(OUTPUT_VIDEO_DIR, f"res_{file_name_prefix}"),
                "prompt": f"{prompt_dct}"
            }
            current_workflow = set_workflow(current_workflow, **kwargs)

            print(f"Processing video: {kwargs}")
            result = queue_prompt(current_workflow)
            if result and 'prompt_id' in result:
                cont += 1
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
