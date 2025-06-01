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
process_time = 90 if  is_windows() else 120

WORKFLOW_API_JSON_FILE = COMFYUI_PATH + \
    "/my_workspace/comfy重要工作流/参考生视频_api.json"  # 你的工作流API格式文件
INPUT_IMAGE_PATH = COMFYUI_PATH+"/my_workspace/control_objs"
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
    
camera_motion_prompts = [
    "dolly in",  # 推镜：缓慢向前推进镜头
    "dolly out",  # 拉镜：镜头平稳后拉
    "tracking shot",  # 横移：镜头沿着特定路径移动
    "follow shot",  # 跟随角色：从左往右或从右往左移动
    "crane shot",  # 升降镜头：从地面仰拍升起或降落
    "orbital shot",  # 环绕镜头：环绕角色缓慢旋转
    "zoom in",  # 变焦推进：放大视角
    "zoom out",  # 变焦拉远：缩小视角
    "tilt up",  # 仰拍：镜头向上倾斜
    "tilt down",  # 俯拍：镜头向下倾斜
    "pan left",  # 左摇镜头：镜头水平向左移动
    "pan right",  # 右摇镜头：镜头水平向右移动
    "overhead shot",  # 俯视镜头：从高处向下拍摄
    "ground level shot",  # 地面级镜头：与地面平行拍摄
    "handheld shot",  # 手持镜头：模拟手持摄像机的晃动效果
    "steadicam shot",  # 稳定跟拍：平稳移动摄像机追随主体
    "extreme close-up",  # 超特写：聚焦于角色的局部细节
    "wide establishing shot",  # 远景定场镜头：展示环境和场景
    "first-person shot",  # 第一视角：模拟角色的视角拍摄
    "point-of-view shot",  # 视角镜头：以角色的角度拍摄
    "slow motion shot",  # 慢动作镜头：降低帧速率呈现慢速画面
    "fast motion shot",  # 快速镜头：加快帧速率呈现快动作
    "rack focus",  # 变焦焦点：快速切换焦点
    "deep focus shot",  # 深焦镜头：保持前景和背景同时清晰
    "shallow focus shot"  # 浅焦镜头：突出主体背景虚化
]
camera_orientation_prompts = [
    "front view",  # 正面
    "profile view",  # 侧面
    "half-front view",  # 半正面
    "back view",  # 背面
    "(quarter front view:1.5)",  # 四分之一正面
    "looking at the camera",  # 看向镜头
    "facing the camera",  # 面对镜头
    "turned towards the camera",  # 转向镜头
    "looking away from the camera",  # 不看镜头
    "facing away from the camera",  # 背对镜头
    "looking up at the camera",  # 抬头看向镜头
    "looking down at the camera",  # 低头看向镜头
    "looking sideways at the camera"  # 向侧面看向镜头
]
frame_range_prompts = [
    "upper body",  # 上半身或腰部以上
    "waist up",  # 腰部以上
    "thigh up",  # 大腿以上
    "knees up",  # 膝盖以上
    "full body",  # 全身
    # "zoom in on the subject",  # 放大主体
    # "zoom out on the subject",  # 缩小主体
    # "frame the subject tightly",  # 紧密框选主体
    # "frame the subject loosely",  # 松散框选主体
    # "center the subject",  # 将主体置于中心
    # "move the subject to the left",  # 将主体移至左侧
    # "move the subject to the right",  # 将主体移至右侧
    # "move the subject up",  # 将主体向上移动
    # "move the subject down",  # 将主体向下移动
    # "focus on the subject’s face",  # 聚焦于主体脸部
    # "focus on the subject’s body",  # 聚焦于主体身体
    # "blur the background",  # 模糊背景
    # "isolate the subject",  # 使主体与背景分离
    # "draw attention to the subject",  # 吸引注意力至主体
    # "avoid cutting off the subject",  # 避免裁剪主体
    # "isolate the subject’s hands",  # 突出主体的手部
    # "isolate the subject’s legs",  # 突出主体的腿部
    # "isolate the subject’s torso"  # 突出主体的躯干
]
expression_prompts = [
    "neutral expression",  # 中性表情
    "smiling",  # 微笑
    "grinning",  # 咧嘴笑
    "laughing",  # 笑
    "crying",  # 哭泣
    "sad expression",  # 悲伤表情
    "angry expression",  # 生气表情
    "furious expression",  # 愤怒表情
    "surprised expression",  # 惊讶表情
    "shocked expression",  # 震惊表情
    "fearful expression",  # 恐惧表情
    "confused expression",  # 困惑表情
    "embarrassed expression",  # 尴尬表情
    "blushing",  # 害羞、脸红
    "determined expression",  # 坚定表情
    "smirking",  # 嘲讽笑容
    "teary eyes",  # 含泪眼神
    "pouting",  # 撅嘴
    "sneering",  # 冷笑
    "wink",  # 眨眼
    "sleepy expression",  # 困倦表情
    "serious expression",  # 严肃表情
    "playful expression",  # 调皮表情
    "thoughtful expression",  # 深思表情
    "bewildered expression",  # 迷茫表情
    "gentle smile",  # 温柔微笑
    "melancholy expression",  # 忧郁表情
    "joyful expression",  # 欢乐表情
    "intense gaze"  # 强烈目光
]

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
            prompt_dct.update(scene_content)

            file_name_prefix = f"""{act_ind}_{cloth_ind}_{scene_ind}"""
            prompt_dct.update({k: v for k, v in itm.items() if k != "id" and k != "人物位置" and k != "镜头含义"})
            prompt_dct["运镜"] = camera_motion_prompts[int(random.random()*len(camera_motion_prompts))]
            prompt_dct["范围"] = frame_range_prompts[int(random.random()*len(frame_range_prompts))]
            prompt_dct["角度"] = camera_orientation_prompts[int(random.random()*3)] + " and then " + camera_orientation_prompts[int(random.random()*len(camera_orientation_prompts))]
            prompt_dct["表情"] = expression_prompts[int(random.random()*len(expression_prompts))]

            current_workflow = json.loads(json.dumps(base_workflow))  # 深拷贝工作流
            img_ind = int(random.random()*6)
            kwargs = {
                "ref_img": f"{INPUT_IMAGE_PATH}/{img_ind}d.png",
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
