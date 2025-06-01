import json
import requests
import time
import random
import traceback
import os
from my_workspace.materials.scene import mv_scenes
from my_workspace.materials.act import mv_shots_new, mv_shots_long_hair_blue_eyes_girl, mv_shots_long_hair_blue_eyes_girl_detailed
from my_workspace.materials.cloth import clothing_prompts_female

COMFYUI_URL = "http://127.0.0.1:8188"  # ComfyUI API 地址
WORKFLOW_API_JSON_FILE = "K:/comfy重要工作流/参考生视频_api.json"  # 你的工作流API格式文件
INPUT_IMAGE_PATH = "C:/Users/ljq/Desktop/xiaoling/09b768b0-bcf0-415d-a3ad-d4806ee48787.png"
OUTPUT_VIDEO_DIR = "f:/projects/ComfyUI/output/materials"


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


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r', encoding="utf-8") as f:
    base_workflow = json.load(f)

iter_tt = 10
cont = 0
for it_cnt in range(0, iter_tt):
    mv_shots = [(i,v) for i,v in enumerate(mv_shots_new)]
    random.shuffle(mv_shots)
    for act_ind, itm in mv_shots:
        try:
            prompt_dct = {
                "风格": "动漫动画，Studio Ghibli anime style, watercolor-inspired backgrounds, soft line art, expressive characters, natural lighting, hand-drawn aesthetic",
                "少女": "蓝色眼睛，黄色长发，白皮肤，",
            }

            cloth_ind = int(random.random()*len(clothing_prompts_female))
            cloth_content = clothing_prompts_female[cloth_ind]
            prompt_dct["少女"] += cloth_content

            scene_ind = int(random.random()*len(mv_scenes))
            scene_content = mv_scenes[scene_ind]
            prompt_dct.update({"场景": scene_content})

            file_name_prefix = f"""{act_ind}_{cloth_ind}_{scene_ind}"""

            prompt_dct.update({k: v for k, v in itm.items() if k != "id"})
            output_video_path = os.path.join(OUTPUT_VIDEO_DIR, f"res_{f}")

            current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流

            load_image_node_id = "73"  # 替换为实际的节点ID
            current_workflow[load_image_node_id]["inputs"]["image"] = INPUT_IMAGE_PATH

            save_video_node_id = "69"  # 替换为实际的节点ID
            current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = os.path.join(
                OUTPUT_VIDEO_DIR, file_name_prefix)

            posi_prompt_node_id = "105"  # 替换为实际的节点ID
            current_workflow[posi_prompt_node_id]["inputs"]["text"] = "\n".join(
                [f"{k}: {v}" for k, v in prompt_dct.items()])

            print(f"Processing video: {file_name_prefix}")
            result = queue_prompt(current_workflow)
            if result and 'prompt_id' in result:
                cont += 1
                prompt_id = result['prompt_id']
                print(f"Queued with prompt_id: {prompt_id}, cont {cont}")
                # 此处可以添加等待任务完成的逻辑，例如轮询 /history/{prompt_id}
            else:
                print(f"Failed to queue {file_name_prefix}")
            print("-" * 30)
            time.sleep(34)  # 等待一段时间，避免请求过于频繁，并给ComfyUI一点处理时间
        except Exception as e:
            traceback.print_exc()
            print(f"except: {e}")


print("All videos processed.")
