import json
import requests
import time
import os
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
process_time = 90 if  is_windows() else 120

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + "/my_workspace/comfy重要工作流/参考生视频_api.json"  # 你的工作流API格式文件
INPUT_VIDEO_DIR = COMFYUI_PATH+"/output/bg_shots/campus/use"
OUTPUT_VIDEO_DIR = COMFYUI_PATH+"/output/bg_shots/campus/fix"


def get_video_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mov'))] # 根据需要添加更多格式

def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    try:
        response = requests.post(f"{COMFYUI_URL}/prompt", data=data, timeout=60*10)
        response.raise_for_status() # 如果请求失败则抛出异常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error queuing prompt: {e}")
        # if response:
        #     print(f"Response content: {response.text}")
        return None


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r') as f:
    base_workflow = json.load(f)

video_files = get_video_files(INPUT_VIDEO_DIR)

for f in video_files:
    input_video_path = os.path.join(INPUT_VIDEO_DIR, f)
    output_video_path = os.path.join(OUTPUT_VIDEO_DIR, f"res_{f}")
    current_workflow = json.loads(json.dumps(base_workflow)) # 深拷贝工作流

    video_filename = os.path.basename(input_video_path)
    video_name_no_ext = os.path.splitext(video_filename)[0]

    # 找到 VHS_LoadVideoPath 节点并修改其输入
    # 你需要知道该节点在工作流JSON中的ID (例如 "6")
    # 你可以通过在ComfyUI界面中右键节点查看其属性，或者直接查看API JSON文件
    load_video_node_id = "3" # 替换为实际的节点ID
    current_workflow[load_video_node_id]["inputs"]["video"] = input_video_path

    # 找到 VHS_SaveVideo 节点并修改其输入 (确保输出文件名唯一)
    save_video_node_id = "4" # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = output_video_path.split(".")[0]
    # current_workflow[save_video_node_id]["inputs"]["output_path"] = OUTPUT_VIDEO_DIR

    print(f"Processing video: {input_video_path}")
    result = queue_prompt(current_workflow)
    if result and 'prompt_id' in result:
        prompt_id = result['prompt_id']
        print(f"Queued with prompt_id: {prompt_id}")
        # 此处可以添加等待任务完成的逻辑，例如轮询 /history/{prompt_id}
    else:
        print(f"Failed to queue {input_video_path}")
    print("-" * process_time)
    time.sleep(5) # 等待一段时间，避免请求过于频繁，并给ComfyUI一点处理时间

print("All videos processed.")