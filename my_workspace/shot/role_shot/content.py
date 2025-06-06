role_shots_all = {
    "campus": [
        # 为一个长发蓝眼少女设计100个mv镜头，需要给出角度，距离，运镜，人物位置范围，动作，表情，镜头含义。
        # 其中人物位置范围要给出少女在镜头中的位置范围，是全身，半身，还是局部特写。运镜要给出关注的身体部位焦点及镜头移动变化。
        # 另外尽量少拍脸部特写，多关注半身和全身。不要涉及具体场景。用python list表形式返回结果，每个项包含
        # "角度""距离""运镜""范围""动作""表情""镜头含义"几个字段
        {
            "角度": "背后跟随",
            "距离": "远景",
            "运镜": "镜头缓慢向前推进，焦点在少女摇曳的长发上，逐渐拉近至全身",
            "范围": "全身，画面中心偏下，走向远方",
            "动作": "少女缓步向前走，长发随风轻摆",
            "表情": "背影，看不清表情",
            "镜头含义": "神秘的开场，引发对人物的好奇，旅程的开始"
        },
        {
            "角度": "低角度仰拍",
            "距离": "全景",
            "运镜": "固定镜头，焦点在少女全身，风吹动发丝和衣角",
            "范围": "全身，画面中心，占据大部分空间",
            "动作": "少女静立，抬头望向天空（天空不入镜），风吹拂着她的长发",
            "表情": "平静，略带憧憬",
            "镜头含义": "展现人物的独立与思考，带有希望感"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "缓慢从左向右平移，焦点始终在少女上半身",
            "范围": "半身，画面左侧三分之一处",
            "动作": "少女侧身站立，目光投向画面右侧远方，手轻轻拨弄垂在胸前的发丝",
            "表情": "沉思，略带忧郁",
            "镜头含义": "人物的内心独白，对远方的凝望"
        },
        {
            "角度": "高角度俯拍",
            "距离": "全景",
            "运镜": "镜头从少女头顶正上方缓慢下降，焦点从头顶发旋到全身",
            "范围": "全身，画面中心",
            "动作": "少女坐在地上，双腿蜷缩，手臂环抱膝盖，头轻靠在膝上",
            "表情": "安静，略显脆弱",
            "镜头含义": "孤独感，内心的宁静或无助"
        },
        {
            "角度": "侧后方45度",
            "距离": "中景",
            "运镜": "手持感，轻微晃动，焦点在少女的侧脸轮廓和飘动的发丝",
            "范围": "半身，画面右侧",
            "动作": "少女在奔跑，长发向后扬起",
            "表情": "看不清，但能感受到动态的活力",
            "镜头含义": "追逐，自由，释放"
        },

        # 动态与节奏变化
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "快速横向摇摄（甩镜头），从模糊到清晰定格在少女身上，焦点在她旋转的动作",
            "范围": "全身，画面中心",
            "动作": "少女原地快速旋转，裙摆和长发飞扬",
            "表情": "愉悦，享受旋转的眩晕感",
            "镜头含义": "喜悦的爆发，展现活力与动感"
        },
        {
            "角度": "低角度",
            "距离": "中景",
            "运镜": "固定镜头，焦点在少女跳跃至最高点的瞬间",
            "范围": "半身，从下往上充满画面",
            "动作": "少女向上跳跃，双手展开，长发向上飘起",
            "表情": "自由，开朗",
            "镜头含义": "挣脱束缚，向上的力量"
        },
        {
            "角度": "平视",
            "距离": "远景",
            "运镜": "固定镜头，焦点在广阔背景中的小小身影",
            "范围": "全身，画面中一个较小的剪影",
            "动作": "少女在广阔的（抽象）空间中奔跑，向着镜头方向或远离镜头",
            "表情": "模糊不清",
            "镜头含义": "渺小与广阔的对比，追寻的意境"
        },
        {
            "角度": "过肩",
            "距离": "中景",
            "运镜": "焦点在少女的手部，她似乎在触摸什么（空气/光）",
            "范围": "半身，前景是她的肩膀和部分头发",
            "动作": "少女伸出手，手指张开，似乎想抓住什么",
            "表情": "专注，带有一丝渴望",
            "镜头含义": "对未知的探索，渴望触碰"
        },
        {
            "角度": "旋转镜头（主观）",
            "距离": "中景到全景",
            "运镜": "镜头围绕少女旋转，速度由慢到快，焦点始终在她身上",
            "范围": "半身/全身，画面中心",
            "动作": "少女站立不动，或配合镜头做缓慢的转身",
            "表情": "迷离或坚定",
            "镜头含义": "眩晕感，世界的变化，内心的漩涡"
        },

        # 情绪与细节
        {
            "角度": "平视",
            "距离": "特写（手部）",
            "运镜": "固定镜头，焦点在少女紧握的拳头或轻柔抚摸某物的手",
            "范围": "局部特写，手部",
            "动作": "手指蜷缩成拳/手指轻柔拂过（如裙摆、发梢）",
            "表情": "通过手部动作暗示情绪（紧张/温柔）",
            "镜头含义": "细节展现内心力量或温柔"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "缓慢向前推近，焦点在少女垂下的长发和微弓的背部",
            "范围": "半身，背对镜头",
            "动作": "少女肩膀轻微耸动，头略低垂",
            "表情": "背影，暗示悲伤或失落",
            "镜头含义": "无声的悲伤，脆弱的时刻"
        },
        {
            "角度": "侧面",
            "距离": "全景",
            "运镜": "固定镜头，焦点在少女身上，她慢慢蹲下",
            "范围": "全身，画面一侧",
            "动作": "少女从站立姿势缓缓蹲下，将脸埋入手臂中",
            "表情": "被遮挡，但动作暗示悲伤",
            "镜头含义": "崩溃的边缘，需要安慰"
        },
        {
            "角度": "平视",
            "距离": "特写（眼睛，但避免正脸特写）",
            "运镜": "从模糊到清晰，焦点快速定格在少女的蓝色眼睛（可能被发丝半遮）",
            "范围": "局部特写，眼睛区域",
            "动作": "眼睛眨动，或有泪光闪烁（可选）",
            "表情": "清澈，或含泪",
            "镜头含义": "灵魂之窗，情绪的直接传递（但仍保持神秘）"
        },
        {
            "角度": "仰拍（透过发丝）",
            "距离": "中景",
            "运镜": "镜头从下往上，部分被少女垂下的发丝遮挡，焦点在发丝后的模糊身影",
            "范围": "半身，透过前景发丝观看",
            "动作": "少女低头，长发垂下形成帷幕",
            "表情": "模糊，神秘",
            "镜头含义": "隐藏的情感，窥视感"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "焦点在少女，背景失焦模糊，她慢慢抬起头",
            "范围": "半身，画面中心",
            "动作": "少女从低头姿态慢慢抬起头，目光由低垂转向前方",
            "表情": "从迷茫到逐渐坚定",
            "镜头含义": "觉醒，重新找回力量"
        },
        {
            "角度": "Dutch Angle (倾斜)",
            "距离": "全景",
            "运镜": "固定镜头，焦点在少女身上",
            "范围": "全身，画面中以倾斜构图存在",
            "动作": "少女静止或缓慢移动，周围环境（抽象）也随之倾斜",
            "表情": "不安或困惑",
            "镜头含义": "内心的失衡，环境的压迫或不稳定感"
        },
        {
            "角度": "平视",
            "距离": "特写（脚部）",
            "运镜": "固定镜头，焦点在少女赤裸的脚尖或穿着鞋的脚",
            "范围": "局部特写，脚部",
            "动作": "脚尖踮起/在地面上轻轻摩擦/迈出一步",
            "表情": "无",
            "镜头含义": "犹豫，坚定，启程的第一步"
        },
        {
            "角度": "背后",
            "距离": "全景",
            "运镜": "镜头缓慢拉远，焦点始终在少女背影",
            "范围": "全身，从画面中心逐渐变小",
            "动作": "少女迈着坚定的步伐走向远方（抽象的亮光或出口）",
            "表情": "背影",
            "镜头含义": "走向未来，希望，旅程的延续"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "环绕运镜，焦点在她和她手中握着的小物件（如一朵花，一个信物，但物件不清晰）",
            "范围": "半身，画面中心",
            "动作": "少女低头凝视手中物件，手指轻轻摩挲",
            "表情": "温柔，珍视，略带回忆",
            "镜头含义": "珍贵的回忆，情感的寄托"
        },
        # --- 更多镜头 ---
        {
            "角度": "高角度",
            "距离": "全景",
            "运镜": "固定，焦点在少女身上，她躺在（抽象的）地面上，长发散开",
            "范围": "全身，画面中心，像一幅画",
            "动作": "静静躺着，手臂自然张开或放在腹部",
            "表情": "平静，安详，或疲惫",
            "镜头含义": "休憩，梦境，脆弱与美丽"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头跟随少女的侧脸，她缓缓转头看向镜头（但不直视）",
            "范围": "半身，从侧面转向斜前方",
            "动作": "转头，目光流转，蓝眼睛在光线下闪烁",
            "表情": "平静中带有一丝探寻",
            "镜头含义": "与观众的间接交流，引人深思"
        },
        {
            "角度": "低角度",
            "距离": "特写（发梢）",
            "运镜": "微距感，焦点在几缕被风吹起的发梢，背景是模糊的少女轮廓",
            "范围": "局部特写，发梢作为前景",
            "动作": "发梢随风舞动",
            "表情": "无",
            "镜头含义": "细节之美，轻盈飘逸感"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "固定镜头，焦点在少女的背影和她梳理长发的动作",
            "范围": "半身，背对镜头",
            "动作": "少女用手指或（抽象的）梳子梳理长发",
            "表情": "背影，显得宁静专注",
            "镜头含义": "日常的仪式感，自我整理"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "缓慢推轨向前，焦点在少女，她坐在秋千上（秋千可抽象处理）轻轻晃动",
            "范围": "全身，画面中心",
            "动作": "轻轻晃动秋千，长发随之摆动",
            "表情": "惬意，略带童真或回忆",
            "镜头含义": "摇摆的思绪，轻松的时光"
        },
        {
            "角度": "俯视（略微倾斜）",
            "距离": "中景",
            "运镜": "固定，焦点在少女垂下的脸庞和散落的几缕蓝发",
            "范围": "半身，头部和肩膀在画面中",
            "动作": "少女低头，发丝散落在脸颊和肩上",
            "表情": "沉静，略带忧思",
            "镜头含义": "沉浸在自己的世界，不被打扰"
        },
        {
            "角度": "平视",
            "距离": "特写（肩膀和颈部线条）",
            "运镜": "缓慢平移，焦点在少女优美的颈部和肩部线条，以及垂落的发丝",
            "范围": "局部特写",
            "动作": "静止或头部轻微转动",
            "表情": "无，强调线条美",
            "镜头含义": "女性的柔美与脆弱感"
        },
        {
            "角度": "大远景",
            "距离": "极远景",
            "运镜": "固定镜头，焦点在广阔天地间的一个小点（少女）",
            "范围": "全身，非常小，几乎融入背景",
            "动作": "站立或行走，姿态不清晰",
            "表情": "不可见",
            "镜头含义": "孤独感，人与自然的融合，史诗感"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "失焦到清晰，焦点落在少女微笑的嘴角（不拍全脸）",
            "范围": "半身，嘴角和下巴部分",
            "动作": "嘴角微微上扬，形成一个微笑",
            "表情": "微笑",
            "镜头含义": "不经意的幸福感，温暖的瞬间"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "镜头向上缓慢仰摇，从少女的脚一直到她仰望的姿态（不拍天空）",
            "范围": "全身，逐渐充满画面",
            "动作": "站立，身体微微后仰，抬头向上看",
            "表情": "向往，期待",
            "镜头含义": "对未来的展望，积极向上的姿态"
        },
        {
            "角度": "侧面",
            "距离": "中景",
            "运镜": "手持跟拍，焦点在少女奔跑时晃动的头发和身体",
            "范围": "半身，画面中心或一侧",
            "动作": "奔跑，手臂自然摆动",
            "表情": "侧脸，可能带有喘息或坚毅",
            "镜头含义": "动态的追逐，努力的过程"
        },
        {
            "角度": "高角度（略微）",
            "距离": "全景",
            "运镜": "固定，焦点在少女，她张开双臂拥抱（空气/风）",
            "范围": "全身，画面中心",
            "动作": "张开双臂，身体舒展，长发被风吹起",
            "表情": "释然，喜悦",
            "镜头含义": "拥抱自由，释放情感"
        },
        {
            "角度": "平视",
            "距离": "特写（手指轻触水面或类似物体的涟漪）",
            "运镜": "固定，焦点在指尖和产生的涟漪",
            "范围": "局部特写，手和涟漪",
            "动作": "手指轻点水面（或其他能产生涟漪的表面）",
            "表情": "无",
            "镜头含义": "微小的动作引发的连锁反应，平静中的波澜"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "缓慢旋转至侧面，焦点从背影逐渐转向能看到部分侧脸和蓝眼睛",
            "范围": "半身，从背对到侧对镜头",
            "动作": "少女缓慢转身，目光望向远方",
            "表情": "平静，深邃",
            "镜头含义": "转变，揭示，多一分了解"
        },
        {
            "角度": "仰视（从地面向上）",
            "距离": "全景",
            "运镜": "固定，焦点在少女从画面外走进画面中心，停住",
            "范围": "全身，从画面边缘走到中心",
            "动作": "行走并停下，抬头挺胸",
            "表情": "坚定，自信",
            "镜头含义": "登场，宣告存在"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "虚焦背景，焦点在少女的发辫（如果梳了辫子）或发饰细节",
            "范围": "半身，焦点在头发细节",
            "动作": "静止或轻微晃动头部",
            "表情": "柔和",
            "镜头含义": "精致的细节，少女感"
        },
        {
            "角度": "低角度",
            "距离": "中景",
            "运镜": "手持拍摄，镜头跟随少女跳舞的步伐，焦点在她的下半身和飞扬的裙摆/裤脚",
            "范围": "半身（腰部以下）",
            "动作": "自由舞动，脚步轻快或有力",
            "表情": "无",
            "镜头含义": "节奏感，生命的律动"
        },
        {
            "角度": "平视（透过前景物体，如晃动的草叶、薄纱）",
            "距离": "中景",
            "运镜": "固定，焦点在前景后的少女，前景物体随风摆动形成动态遮挡",
            "范围": "半身，被前景部分遮挡",
            "动作": "静立或缓慢移动，目光迷离",
            "表情": "朦胧，梦幻",
            "镜头含义": "梦境感，神秘的氛围"
        },
        {
            "角度": "背后",
            "距离": "全景",
            "运镜": "镜头从低处慢慢升起（模拟无人机），展现少女走向广阔（抽象）地平线的背影",
            "范围": "全身，逐渐变小融入大背景",
            "动作": "稳步走向远方",
            "表情": "背影",
            "镜头含义": "史诗般的旅程，探索未知"
        },
        {
            "角度": "特写（耳朵和耳边的碎发）",
            "距离": "局部特写",
            "运镜": "固定，焦点在耳朵轮廓和几缕调皮的蓝色碎发",
            "范围": "局部特写，耳朵区域",
            "动作": "静止，或头部微侧让碎发轻晃",
            "表情": "无",
            "镜头含义": "不经意的细节美，青春气息"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头快速推近，停在少女坚定的眼神上（即使有发丝遮挡）",
            "范围": "半身，视觉中心是眼睛",
            "动作": "眼神坚定，直视前方（不一定是镜头）",
            "表情": "坚定，不屈",
            "镜头含义": "力量的凝聚，决心的展现"
        },
        {
            "角度": "旋转上升",
            "距离": "全景至中景",
            "运镜": "镜头围绕少女旋转并同时向上提升，焦点始终在她身上",
            "范围": "全身到半身，画面中心",
            "动作": "少女张开双臂向上仰望或旋转",
            "表情": "释放，喜悦，陶醉",
            "镜头含义": "情绪的升华，飞翔的意象"
        },
        {
            "角度": "剪影",
            "距离": "全景",
            "运镜": "固定，焦点在少女的剪影轮廓，背景是明亮的光源（抽象）",
            "范围": "全身，清晰的黑色剪影",
            "动作": "做出具有辨识度的姿态，如祈祷、跳跃、伸展",
            "表情": "剪影，不可见",
            "镜头含义": "神秘感，意境的表达，希望之光"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "慢动作，焦点在少女甩动长发的瞬间，发丝在空中划出优美弧线",
            "范围": "半身，画面中心",
            "动作": "猛然甩头或转身，长发散开",
            "表情": "洒脱，不羁，或带有力量感",
            "镜头含义": "瞬间的爆发力，女性的魅力与力量"
        },
        {
            "角度": "俯拍（略微）",
            "距离": "特写（放在腿上的手）",
            "运镜": "固定，焦点在少女交叠或并拢放在膝盖上的手，以及裙摆的褶皱",
            "范围": "局部特写，手部和膝盖区域",
            "动作": "双手安静放置，或手指轻微蜷曲",
            "表情": "无",
            "镜头含义": "安静的等待，内心的平静或紧张"
        },
        {
            "角度": "过肩（从少女背后向前看）",
            "距离": "远景",
            "运镜": "固定，焦点在远方（抽象的景物），前景是少女的背影轮廓",
            "范围": "半身或全身的背影轮廓在前景",
            "动作": "静静站立眺望",
            "表情": "背影",
            "镜头含义": "对未来的展望，与世界的对话"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "呼吸感镜头（轻微上下浮动），焦点在少女身上，她闭着眼睛感受风",
            "范围": "半身，画面中心",
            "动作": "闭眼，头部微仰，感受风吹过脸颊和头发",
            "表情": "享受，宁静",
            "镜头含义": "与自然的交融，内心的平和"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "固定，焦点在少女，她逆光站立，身体边缘有光晕",
            "范围": "全身，画面中心",
            "动作": "静立，长发和衣角被光勾勒",
            "表情": "模糊，但感觉神圣或坚定",
            "镜头含义": "希望的象征，光芒中的守护者"
        },
        {
            "角度": "侧面",
            "距离": "中景",
            "运镜": "慢镜头，焦点在她奔跑时，蓝色的眼睛（可被发丝部分遮挡）中映出的光芒",
            "范围": "半身，侧脸为主",
            "动作": "奔跑，风吹起发丝",
            "表情": "坚毅，眼中闪烁光芒",
            "镜头含义": "追逐梦想，眼中的希望之火"
        },
        {
            "角度": "平视",
            "距离": "特写（嘴唇，非性感）",
            "运镜": "固定，焦点在少女微抿的嘴唇或轻启欲言又止的唇",
            "范围": "局部特写，嘴唇",
            "动作": "嘴唇轻抿/微微张开",
            "表情": "通过唇部暗示思考、决心或犹豫",
            "镜头含义": "未说出口的话，内心的挣扎或决定"
        },
        # --- 51-75 ---
        {
            "角度": "背后跟随",
            "距离": "中景",
            "运镜": "手持稳定器，流畅跟随少女在抽象的狭窄通道中行走，焦点在她的背影和晃动的长发",
            "范围": "半身，画面中心",
            "动作": "在狭窄空间中前行，步伐坚定",
            "表情": "背影",
            "镜头含义": "探索未知，穿越困境"
        },
        {
            "角度": "高角度俯拍（旋转）",
            "距离": "全景",
            "运镜": "镜头围绕躺在地上的少女旋转并缓慢拉升，焦点从她散开的长发到全身",
            "范围": "全身，画面中心",
            "动作": "躺在地上，双臂展开，长发如花瓣般散开",
            "表情": "平静，仿佛融入大地",
            "镜头含义": "与世隔绝的宁静，梦的开始或结束"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "焦点在少女手中捧着的（抽象的）发光物体，光线映照在她低垂的脸上",
            "范围": "半身，画面中心",
            "动作": "双手捧着发光物，低头凝视",
            "表情": "专注，虔诚，被光芒吸引",
            "镜头含义": "希望的象征，内心的信仰"
        },
        {
            "角度": "低角度",
            "距离": "特写（飘动的裙摆/衣角）",
            "运镜": "固定，焦点在被风吹起的裙摆或衣角，背景是模糊的少女腿部",
            "范围": "局部特写，衣物细节",
            "动作": "静立，衣物随风飘动",
            "表情": "无",
            "镜头含义": "轻盈感，风的痕迹"
        },
        {
            "角度": "侧后方",
            "距离": "全景",
            "运镜": "固定，焦点在少女，她站在高处（抽象的台阶或坡顶）望向远方",
            "范围": "全身，画面一侧，有较大留白",
            "动作": "静立远眺，风吹动长发",
            "表情": "侧脸， contemplative",
            "镜头含义": "达成目标后的回望，对未来的展望"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "快速剪辑：少女连续做出几个不同的小动作（拨头发、歪头、轻笑但不见全脸）",
            "范围": "半身，连续的动态",
            "动作": "系列小动作的组合",
            "表情": "通过动作传递轻松、俏皮",
            "镜头含义": "展现人物的多面性和活力"
        },
        {
            "角度": "水下感（模拟）",
            "距离": "全景",
            "运镜": "缓慢漂浮感，焦点在少女（仿佛在水中）漂浮或缓慢游动，长发散开如海藻",
            "范围": "全身，画面中漂浮",
            "动作": "缓慢的肢体动作，如同在失重环境",
            "表情": "宁静，梦幻",
            "镜头含义": "潜意识，梦境，无拘无束的状态"
        },
        {
            "角度": "平视",
            "距离": "特写（锁骨与垂落的发丝）",
            "运镜": "固定，焦点在少女精致的锁骨以及几缕垂落在上面的蓝色发丝",
            "范围": "局部特写，锁骨区域",
            "动作": "静止，呼吸时轻微起伏",
            "表情": "无",
            "镜头含义": "脆弱与美的结合，细节的吸引力"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "固定，焦点在少女的背影，她将长发拢到一侧，露出后颈",
            "范围": "半身，背对镜头",
            "动作": "将头发拨开，露出颈部线条",
            "表情": "背影，暗示一丝清爽或小性感",
            "镜头含义": "不经意的魅力展现"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "镜头围绕少女快速旋转，营造眩晕感，焦点在她身上",
            "范围": "全身，画面中心",
            "动作": "少女静立或缓慢张开手臂，世界在旋转",
            "表情": "平静或享受这种眩晕",
            "镜头含义": "世界的喧嚣与内心的平静，或情绪的爆发点"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头从少女背后慢慢移到她的侧前方，焦点始终在她身上",
            "范围": "半身，从背影转为侧面",
            "动作": "静立或缓慢转身，目光投向斜前方",
            "表情": "平静，若有所思",
            "镜头含义": "视角的转变，对人物更深入的观察"
        },
        {
            "角度": "高角度",
            "距离": "全景",
            "运镜": "固定，焦点在少女，她独自坐在一个广阔（抽象）空间的中央，显得渺小",
            "范围": "全身，画面中心但占比较小",
            "动作": "安静坐着，可能抱着膝盖或双手撑地",
            "表情": "看不清，强调孤独感",
            "镜头含义": "孤独与广阔，个体的存在感"
        },
        {
            "角度": "平视",
            "距离": "特写（手腕与袖口）",
            "运镜": "固定，焦点在少女纤细的手腕和衣袖边缘，可能有简单的饰品",
            "范围": "局部特写，手腕区域",
            "动作": "手腕轻微转动或静止",
            "表情": "无",
            "镜头含义": "细节的点缀，精致感"
        },
        {
            "角度": "背后",
            "距离": "远景",
            "运镜": "缓慢向前推近，焦点从模糊的背影逐渐清晰，停留在中景",
            "范围": "从远景全身到中景半身，始终背对",
            "动作": "静立不动，仿佛在等待或沉思",
            "表情": "背影",
            "镜头含义": "悬念的营造，期待她的转身"
        },
        {
            "角度": "剪影特写（侧脸轮廓和发丝）",
            "距离": "中景（接近特写）",
            "运镜": "固定，强逆光，只看见清晰的侧脸和发丝剪影，蓝眼睛处可能有微弱反光",
            "范围": "半身剪影，侧脸轮廓清晰",
            "动作": "静止，目光望向光源方向",
            "表情": "剪影，神秘而坚定",
            "镜头含义": "艺术化的轮廓美，希望之光下的剪影"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头左右轻微摇晃（类似船上），焦点在少女努力保持平衡的身体",
            "范围": "半身，画面中心",
            "动作": "身体随镜头轻微晃动，试图站稳",
            "表情": "略带困惑或努力",
            "镜头含义": "生活中的摇摆不定，努力寻找平衡"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "固定，焦点在少女向上伸手的动作，仿佛要抓住从上方落下的东西（光斑、花瓣等抽象元素）",
            "范围": "全身，画面中心",
            "动作": "仰头，伸手向上抓取",
            "表情": "渴望，纯真",
            "镜头含义": "对美好事物的向往与追求"
        },
        {
            "角度": "平视",
            "距离": "特写（湿润的眼眶，侧面，非正脸）",
            "运镜": "极缓慢推近，焦点在少女侧面眼角闪烁的泪光或湿润感，蓝眼睛显得更清澈",
            "范围": "局部特写，眼睛侧面",
            "动作": "眼眶湿润，可能强忍泪水",
            "表情": "隐忍的悲伤或感动",
            "镜头含义": "无声的情绪流露，脆弱而美丽"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "固定，焦点在少女的背影，她慢慢将头发编成一个简单的辫子",
            "范围": "半身，背对镜头",
            "动作": "双手在脑后编织发辫",
            "表情": "背影，专注",
            "镜头含义": "整理心情，准备新的开始"
        },
        {
            "角度": "高角度俯视",
            "距离": "中景",
            "运镜": "镜头缓慢下降，焦点在少女低头时头顶的发旋和散落的肩发",
            "范围": "半身，头顶和肩膀为主",
            "动作": "低头沉思，发丝垂落",
            "表情": "看不清，但姿态显得内向",
            "镜头含义": "沉浸式的思考，不愿被打扰的瞬间"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "镜头跟随少女在（抽象的）雨中奔跑或行走，长发湿漉漉贴在身上",
            "范围": "全身，画面中移动",
            "动作": "雨中奔跑或漫步，头发和衣服湿透",
            "表情": "可能是释放、悲伤或享受雨水",
            "镜头含义": "洗礼，释放，困境中的坚持"
        },
        {
            "角度": "特写（脚踝和鞋子）",
            "距离": "局部特写",
            "运镜": "固定，焦点在少女的脚踝线条以及她穿着的鞋子（简约设计）",
            "范围": "局部特写，脚踝",
            "动作": "静止或脚尖轻点地面",
            "表情": "无",
            "镜头含义": "步伐的起点，细节的时尚感"
        },
        {
            "角度": "侧面",
            "距离": "中景",
            "运镜": "慢动作，少女的发丝被风吹到嘴边，她轻轻吹开或用手拨开",
            "范围": "半身，侧脸为主",
            "动作": "吹开/拨开挡住嘴唇的发丝",
            "表情": "不经意，自然",
            "镜头含义": "生活中的小插曲，自然的魅力"
        },
        {
            "角度": "背后",
            "距离": "全景",
            "运镜": "固定，焦点在少女走向一道门（抽象的，可能是光的形状）的背影",
            "范围": "全身，走向画面中的“门”",
            "动作": "走向门，即将踏入",
            "表情": "背影",
            "镜头含义": "选择，机遇，通往新的可能"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头从失焦逐渐对焦到少女身上，她正从睡梦中苏醒般慢慢睁开蓝眼睛（眼睛可部分被头发遮挡）",
            "范围": "半身，画面中心",
            "动作": "缓慢睁眼，眼神迷离到清醒",
            "表情": "初醒的迷茫与清新",
            "镜头含义": "新的开始，意识的苏醒"
        },
        # --- 76-100 ---
        {
            "角度": "低角度",
            "距离": "中景",
            "运镜": "固定，焦点在少女向上抛起一件轻物件（如一片羽毛、一张纸）的动作",
            "范围": "半身，身体向上舒展",
            "动作": "向上抛物件，仰头注视",
            "表情": "期待，轻快",
            "镜头含义": "放飞希望，轻松的心情"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "移轴效果（可选），少女在（抽象的）微缩景观中行走，显得巨大或渺小",
            "范围": "全身，与背景形成特殊比例",
            "动作": "在特殊比例的场景中行走",
            "表情": "好奇或平静",
            "镜头含义": "超现实感，视角错位带来的趣味"
        },
        {
            "角度": "背后特写（发髻或束起的马尾）",
            "距离": "局部特写",
            "运镜": "固定，焦点在精心打理或随意束起的发型细节，几缕碎发垂落颈间",
            "范围": "局部特写，后脑发型",
            "动作": "静止",
            "表情": "无",
            "镜头含义": "干练与柔美的结合，细节的精致"
        },
        {
            "角度": "高角度（略俯）",
            "距离": "中景",
            "运镜": "固定，焦点在少女席地而坐，膝上放着一本书（不露内容）或素描本",
            "范围": "半身，安静阅读或绘画的姿态",
            "动作": "低头阅读/绘画，手指翻页或持笔",
            "表情": "专注，沉静",
            "镜头含义": "文艺气息，内心的丰富世界"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "固定，少女背对镜头站在（抽象的）镜子前，镜中映出她模糊的正面或只有背影",
            "范围": "全身，背对镜头，前景是镜子",
            "动作": "静立，可能在审视镜中的自己",
            "表情": "镜中模糊，引人遐想",
            "镜头含义": "自我审视，身份的迷茫或确认"
        },
        {
            "角度": "侧面",
            "距离": "特写（耳垂与简单的耳饰）",
            "运镜": "固定，焦点在少女的耳垂和佩戴的简约耳饰，蓝发丝掠过",
            "范围": "局部特写，耳朵区域",
            "动作": "静止或头部轻微晃动",
            "表情": "无",
            "镜头含义": "低调的闪光点，细节的品味"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "旋转上升，焦点在少女向上跳跃并空中旋转的瞬间，裙摆和长发飞扬",
            "范围": "全身，在空中动态",
            "动作": "跳跃旋转",
            "表情": "极致的喜悦与自由",
            "镜头含义": "挣脱束缚，飞向自由的高潮"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "焦点在少女，她用发带或丝巾束起长发的过程（不露全脸）",
            "范围": "半身，手臂和头发为焦点",
            "动作": "抬手束发，动作轻柔",
            "表情": "专注，或带一丝微笑",
            "镜头含义": "日常的准备，改变造型的瞬间"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "固定，焦点在少女的背影和她肩上滑落的衣物（如外套、披肩的一角）",
            "范围": "半身，背对镜头",
            "动作": "静立，衣物不经意滑落",
            "表情": "背影，暗示放松或不设防",
            "镜头含义": "不经意的性感，卸下防备"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "剪影与实体交替闪回，少女在光影中时而清晰时而模糊",
            "范围": "全身，在光影变化中",
            "动作": "静止或缓慢移动",
            "表情": "模糊，神秘",
            "镜头含义": "梦与现实的交错，身份的不确定性"
        },
        {
            "角度": "高角度",
            "距离": "特写（摊开的手掌，掌心向上）",
            "运镜": "固定，焦点在少女摊开的手掌，掌纹清晰，可能有光斑落在掌心",
            "范围": "局部特写，手掌",
            "动作": "手掌摊开向上",
            "表情": "无",
            "镜头含义": "接纳，给予，命运的纹路"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头缓慢地从少女的脚踝向上摇摄至腰部，焦点始终在身体曲线上",
            "范围": "半身（下半身到腰部）",
            "动作": "静立或轻微摆动身体",
            "表情": "无",
            "镜头含义": "展现身体的线条美，优雅的姿态"
        },
        {
            "角度": "鱼眼镜头（可选）",
            "距离": "全景",
            "运镜": "固定或缓慢旋转，焦点在少女，周围环境发生奇特畸变",
            "范围": "全身，处于畸变画面的中心",
            "动作": "静止或夸张的动作",
            "表情": "好奇，迷茫或玩味",
            "镜头含义": "扭曲的现实，非同寻常的视角"
        },
        {
            "角度": "背后",
            "距离": "全景",
            "运镜": "镜头跟随少女跑向一片强烈的光芒中，最终身影消失在光里",
            "范围": "全身，从清晰到融入光芒",
            "动作": "奔跑，冲向光明",
            "表情": "背影",
            "镜头含义": "希望的极致，与光的融合，解脱或升华"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "光影效果：条状光影（如百叶窗）投射在少女身上，她缓慢移动，光影随之变化",
            "范围": "半身，被光影分割",
            "动作": "缓慢移动或转动身体",
            "表情": "平静，神秘",
            "镜头含义": "时间的流逝，捉摸不定的情绪"
        },
        {
            "角度": "低角度",
            "距离": "中景",
            "运镜": "固定，焦点在少女向上看的侧脸剪影，蓝眼睛在暗处依然有神采（如有微弱补光）",
            "范围": "半身，侧脸轮廓",
            "动作": "抬头仰望",
            "表情": "坚定，向往",
            "镜头含义": "黑暗中的希望，坚定的信念"
        },
        {
            "角度": "特写（手指轻触琴键或乐器弦）",
            "距离": "局部特写",
            "运镜": "固定，焦点在手指与乐器的互动，暗示音乐的流动",
            "范围": "局部特写，手与乐器",
            "动作": "弹奏，拨弦",
            "表情": "无，通过音乐传递情感",
            "镜头含义": "情感的另一种表达，艺术的慰藉"
        },
        {
            "角度": "平视",
            "距离": "全景",
            "运镜": "高速摄影（升格），少女在空中跳跃或旋转的慢动作，每一根发丝都清晰可见",
            "范围": "全身，空中的慢动作",
            "动作": "跳跃，旋转",
            "表情": "舒展，享受",
            "镜头含义": "时间凝固的美，极致的动态展现"
        },
        {
            "角度": "背后",
            "距离": "中景",
            "运镜": "手持跟拍，少女提着裙摆（或宽松裤脚）赤脚在（抽象的）草地或沙滩上奔跑，焦点在她的背影和脚步",
            "范围": "半身，奔跑的动态",
            "动作": "赤脚奔跑，提着裙摆",
            "表情": "背影，但能感到自由快乐",
            "镜头含义": "回归本真，无拘无束的快乐"
        },
        {
            "角度": "高角度（正上方）",
            "距离": "全景",
            "运镜": "固定，少女躺在纯色（如白色或深色）背景上，身体和长发构成优美的图案",
            "范围": "全身，如同一幅构图精美的平面作品",
            "动作": "静躺，手臂和腿部可摆出不同姿势",
            "表情": "平静，安详",
            "镜头含义": "纯粹的美感，艺术化的身体语言"
        },
        {
            "角度": "平视",
            "距离": "中景",
            "运镜": "镜头穿过摇曳的（抽象）花丛或植物，焦点在花丛后的少女模糊身影，逐渐清晰",
            "范围": "半身，从模糊到清晰",
            "动作": "在花丛后静立或微笑",
            "表情": "温柔，恬静",
            "镜头含义": "发现美，隐藏的惊喜"
        },
        {
            "角度": "特写（一缕被风吹起的蓝色发丝，拂过镜头）",
            "距离": "局部特写（极近）",
            "运镜": "固定或轻微晃动，焦点在发丝上，发丝短暂遮挡镜头后移开",
            "范围": "局部特写，发丝",
            "动作": "发丝拂过",
            "表情": "无",
            "镜头含义": "不经意的触碰，亲密感，过渡镜头"
        },
        {
            "角度": "低角度",
            "距离": "全景",
            "运镜": "固定，少女从高处（抽象台阶）缓缓走下，长发和衣袂飘逸",
            "范围": "全身，从上往下走入画面",
            "动作": "优雅地走下台阶",
            "表情": "平静，略带庄重",
            "镜头含义": "降临，优雅的登场"
        },
        {
            "角度": "侧面",
            "距离": "中景",
            "运镜": "固定，焦点在少女的侧影，她闭上眼睛，深吸一口气，然后缓缓睁开，眼神变得明亮",
            "范围": "半身，侧脸为主",
            "动作": "闭眼深呼吸再睁眼",
            "表情": "从平静到焕发神采",
            "镜头含义": "积蓄力量，重新出发，焕然一新"
        },
        {
            "角度": "背后",
            "距离": "远景",
            "运镜": "固定镜头，焦点在少女小小的背影，她走向地平线上微弱的晨曦或黄昏的光芒",
            "范围": "全身，画面中渺小的身影",
            "动作": "走向远方的光芒",
            "表情": "背影",
            "镜头含义": "永恒的追寻，对希望的向往，开放式结局的暗示"
        }
    ]
}
