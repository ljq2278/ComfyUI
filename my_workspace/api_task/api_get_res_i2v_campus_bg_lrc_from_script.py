import logging
logging.basicConfig(filename="log.out", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

import platform
def is_windows():
    os_name = platform.system()
    if os_name.lower() == 'windows':
        logging.info("当前操作系统为 Windows")
        return True
    elif os_name.lower() == 'linux':
        logging.info("当前操作系统为 Linux")
        return False
    else:
        logging.info(f"当前操作系统为 {os_name}")
        return False

COMFYUI_PATH = "f:/projects/ComfyUI" if is_windows() else "/workspace/ComfyUI"
COMFYUI_URL = "http://127.0.0.1:8188" if is_windows() else "http://127.0.0.1:8190"
LRC_BASE_DIR = "f:/projects/auto_video/mv/data" if is_windows() else "/workspace/auto_video/mv/data"

import os
import sys
os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''
if "PYTHONPATH" in os.environ:
    os.environ["PYTHONPATH"] += f":{COMFYUI_PATH}"
else:
    os.environ["PYTHONPATH"] = f"{COMFYUI_PATH}"
sys.path.insert(0, COMFYUI_PATH)  

import asyncio
import traceback
import random
import time
import requests
import httpx
import json
from my_workspace.shot.bg_shot.camera import camera_motion_prompts
from my_workspace.restful_api import OpenaiClient

# from my_workspace.shot.bg_shot.content import bg_shots_all

httpx_client = httpx.AsyncClient(limits=httpx.Limits(max_connections=1024, max_keepalive_connections=1024))
llm_cli = OpenaiClient(
    engine="qwen-plus-latest",
    api_key="sk-e3392a85198840f1b201495b34182350",
    # deepseek_api_key="sk-e3392a85198840f1b201495b34182350" if "172.17.209.45" in ips else "sk-813a748ccc884dcb879b00bd03b1520f",
    url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    http_client=httpx_client,
)

exp_nm = "Dreaming_Deep"
topic = "围绕沉浸式梦境与深海意象。整体氛围宁静、神秘且略带忧郁，表达了一种在深海中沉睡、漂流，与寂静对话的体验。"

process_time = 120 if is_windows() else 180

bg_shots_all = json.load(
    open(f"{LRC_BASE_DIR}/{exp_nm}.json", "r", encoding="utf-8"))
mv_shots = []
for itm in bg_shots_all:
    for sub in itm["lyric"].split("\t"):
        if sub:
            mv_shots.append(sub)
WORKFLOW_API_JSON_FILE = COMFYUI_PATH + "/my_workspace/workflow/空参考生视频_api.json"  # 你的工作流API格式文件
OUTPUT_VIDEO_DIR = COMFYUI_PATH+"/output/material/bg_shot"


def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    try:
        response = requests.post(
            f"{COMFYUI_URL}/prompt", data=data, timeout=60*10)
        response.raise_for_status()  # 如果请求失败则抛出异常
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.info(f"Error queuing prompt: {e}")
        # if response:
        #     logging.info(f"Response content: {response.text}")
        return None


def set_workflow(current_workflow, **kwargs):

    save_video_node_id = "69"  # 替换为实际的节点ID
    current_workflow[save_video_node_id]["inputs"]["filename_prefix"] = kwargs["output_filename_prefix"]

    posi_prompt_node_id = "105"  # 替换为实际的节点ID
    current_workflow[posi_prompt_node_id]["inputs"]["text"] = kwargs["prompt"]

    k_sampler_node_id = "108"  # 替换为实际的节点ID
    current_workflow[k_sampler_node_id]["inputs"]["seed"] = int(
        random.random()*10000000000)

    return current_workflow


# 加载工作流模板
with open(WORKFLOW_API_JSON_FILE, 'r', encoding="utf-8") as f:
    base_workflow = json.load(f)


async def main():
    iter_tt = 200
    cont = 0
    for it_cnt in range(0, iter_tt):
        random.shuffle(mv_shots)
        for lyric in mv_shots:
            try:

                prompt_dct = {
                    "风格": "现代高清的吉卜力动画风格，细腻、干净、明亮的手绘风格，线条清晰，色彩鲜明自然，避免过度泛黄或昏暗，整体呈现温柔、通透且富有情感的动画质感。",
                }

                prompt_dct.update({"歌词": lyric})
                prompt_prompt = f"""请为下面名为'{exp_nm}'的歌曲的歌词:\n'{lyric}'\n添加画面内容描述，如果内容中有人物，给出人物表情描述；如果内容中没有人物，请给出画面焦点事物。150字左右。下面开始："""
                think = ""
                text = ""
                async for delta in llm_cli.async_stream_chat(chat_content="", history=[], prompt=prompt_prompt, max_length=256 * 16, temperature=0.4, enable_thinking=True):
                    # logging.info(f"process_message_async: delta: {delta}")
                    if "think" in delta:
                        think += delta["think"]
                    if "text" in delta:
                        text += delta["text"]
                prompt_dct.update({"画面内容": text})
                camera_motion_id = int(random.random()*len(camera_motion_prompts))
                prompt_dct["运镜"] = camera_motion_prompts[camera_motion_id]

                current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流

                file_name_prefix = f"""{exp_nm}_歌词#{prompt_dct["歌词"]}"""
                kwargs = {
                    "output_filename_prefix": os.path.join(OUTPUT_VIDEO_DIR, f"{file_name_prefix}"),
                    "prompt": f"{prompt_dct}"
                }
                current_workflow = set_workflow(current_workflow, **kwargs)

                logging.info(f"Processing video: cont:{cont}\t{kwargs}")
                result = queue_prompt(current_workflow)
                if result and 'prompt_id' in result:
                    prompt_id = result['prompt_id']
                    logging.info(f"""Queued with prompt_id: cont:{cont}\t{prompt_id}""")
                    cont += 1
                    # 此处可以添加等待任务完成的逻辑，例如轮询 /history/{prompt_id}
                else:
                    logging.info(f"Failed to queue {kwargs}")
                logging.info("-" * 30)
                time.sleep(process_time)  # 等待一段时间，避免请求过于频繁，并给ComfyUI一点处理时间
            except Exception as e:
                traceback.print_exc()
                logging.info(f"except: {e}")


    logging.info("All videos processed.")

if __name__=="__main__":
    asyncio.run(main())