import json
import requests
import time
import random
import traceback
import os
import platform
from my_workspace.shot.role_shot.scene import mv_scenes_all
from my_workspace.shot.role_shot.content import role_shots_all
from my_workspace.shot.role_shot.cloth import clothing_prompts_female
from my_workspace.shot.role_shot.camera import camera_motion_prompts, camera_orientation_prompts
from my_workspace.shot.role_shot.range import frame_range_prompts
from my_workspace.shot.role_shot.expression import expression_prompts


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
process_time = 90 if  is_windows() else 120

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + "/my_workspace/workflow/参考生视频_api.json"  # 你的工作流API格式文件
INPUT_IMAGE_PATH = COMFYUI_PATH+"/output/material/role_image"
OUTPUT_VIDEO_DIR = COMFYUI_PATH+"/output/material/role_shot"


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
    mv_shots = [(i, v) for i, v in enumerate(role_shots_all[exp_nm])]
    random.shuffle(mv_shots)
    for content_ind, itm in mv_shots:
        try:
            prompt_dct = {
                "风格": "现代高清的吉卜力动画风格，细腻、干净、明亮的手绘风格，线条清晰，色彩鲜明自然，避免过度泛黄或昏暗，整体呈现温柔、通透且富有情感的动画质感。",
                "少女": "蓝色眼睛，黄色长发，白皮肤，",
            }

            cloth_ind = int(random.random()*len(clothing_prompts_female))
            cloth_content = clothing_prompts_female[cloth_ind]
            prompt_dct["少女"] += cloth_content

            scene_ind = int(random.random()*len(mv_scenes_all[exp_nm]))
            scene_content = mv_scenes_all[exp_nm][scene_ind]
            prompt_dct.update(scene_content)
            
            prompt_dct.update({k: v for k, v in itm.items() if k != "id" and k != "镜头含义"})
            camera_motion_id = int(random.random()*len(camera_motion_prompts))
            prompt_dct["运镜"] = camera_motion_prompts[camera_motion_id]
            camera_orientation_id = int(random.random()*len(camera_orientation_prompts))
            prompt_dct["角度"] = camera_orientation_prompts[camera_orientation_id]
            # prompt_dct["角度"] = camera_orientation_prompts[int(random.random()*3)] + " and then " + camera_orientation_prompts[int(random.random()*len(camera_orientation_prompts))]
            range_id = int(random.random()*len(frame_range_prompts))
            prompt_dct["范围"] = frame_range_prompts[range_id]
            expression_id = int(random.random()*len(expression_prompts))
            prompt_dct["表情"] = expression_prompts[expression_id]
            # prompt_dct["场景"] = "课堂"
            # prompt_dct["动作"] = "边笑边画画"
            
            file_name_prefix = f"""{exp_nm}_场景#{scene_ind}_内容#{content_ind}_表情#{expression_id}"""
            current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流
            kwargs = {
                "ref_img": os.path.join(INPUT_IMAGE_PATH, os.listdir(INPUT_IMAGE_PATH)[int(random.random()*len(os.listdir(INPUT_IMAGE_PATH)))]),
                "output_filename_prefix": os.path.join(OUTPUT_VIDEO_DIR, f"{file_name_prefix}"),
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
