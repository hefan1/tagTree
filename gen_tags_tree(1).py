def get_json():
    return [
        {
            "id": 1,
            "label": "人工智能s（Artificial Intelligence）",
            "label_en":"Artificial Intelligence",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "人工智能（英语：Artificial Intelligence, AI）亦称机器智能，是指由人制造出来的机器所表现出来的智能。通常人工智能是指通过普通计算机程序的手段实现的人类智能技术。该词也指出研究这样的智能系统是否能够实现，以及如何实现的科学领域。",
            "description_en": ""
        },
        {
            "id": 2,
            "fatherid": 1,
            "label": "自动驾驶（Autonomous Driving）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Google_self_driving_car_at_the_Googleplex.jpg",
            "description": "自动驾驶（英语：Autopilot）是一种经由机械、电子仪器、液压系统、陀螺仪等，做出无人操控的自动化驾驶。常用在飞行器、船舰及部分的铁路列车。公路交通工具的自动驾驶仍在研究开发中，尚未大规模商用。",
            "description_en": ""
        },
        {
            "id": 3,
            "fatherid": 2,
            "label": "无人驾驶车（Driverless Car）",,
            "label_en": "Driverless Car",
            "icon_url": "https://images.pexels.com/photos/1098662/pexels-photo-1098662.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "description": "自动驾驶汽车，又称为无人驾驶汽车、电脑驾驶汽车或轮式移动机器人，是无人地面载具的一种，具有传统汽车的运输能力。作为自动化载具，自动驾驶汽车不需要人为操作即能感测其环境及导航。",
            "description_en": ""
        },
        # {
        #     "id": 4,
        #     "fatherid": 3,
        #     "label": "百度无人驾驶车",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 5,
        #     "fatherid": 3,
        #     "label": "Google无人驾驶汽车",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""

        # },
        {
            "id": 6,
            "fatherid": 3,
            "label": "运动规划（Motion planning）",,
            "label_en": "Motion Planning",
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Motion_planning_configuration_space_road_map_path.svg/768px-Motion_planning_configuration_space_road_map_path.svg.png",
            "description": "运动规划（英语：Motion Planning）是一个过程，用来寻找从起始状态到目标状态的移动步骤。运动规划常常需要在运动受到约束的条件下找到最优解。运动规划多用于机器人学。",
            "description_en": ""
        },
        # {
        #     "id": 7,
        #     "fatherid": [
        #         3,
        #         5
        #     ],
        #     "label": "Waymo（谷歌无人驾驶公司）",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 8,
            "fatherid": 1,
            "label": "模式识别（Pattern Recognition）",,
            "label_en": "Autonomous Driving",
            "icon_url": "https://petapixel.com/assets/uploads/2016/06/facialrecognition_1.jpg",
            "description": "模式识别（英语：Pattern recognition），就是通过计算机用数学技术方法来研究模式的自动处理和判读。我们把环境与客体统称为“模式”。随着计算机技术的发展，人类有可能研究复杂的信息处理过程。信息处理过程的一个重要形式是生命体对环境及客体的识别。",
            "description_en": ""
        },
        # {
        #     "id": 9,
        #     "fatherid": [
        #         8,
        #         14
        #     ],
        #     "label": "文字识别（Optical Character Recognition）",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "光学字符识别（英语：Optical Character Recognition, OCR）是指对文本资料的图像文件进行分析识别处理，获取文字及版面信息的过程。",
        #     "description_en": ""
        # },
        {
            "id": 10,
            "fatherid": 9,
            "label": "OCR（光学字符识别）",,
            "label_en": "Autonomous Driving",
            "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Portable_scanner_and_OCR_%28video%29.webm/1200px--Portable_scanner_and_OCR_%28video%29.webm.jpg",
            "description": "光学字符识别（英语：Optical Character Recognition, OCR）是指对文本资料的图像文件进行分析识别处理，获取文字及版面信息的过程。",
            "description_en": ""
        },
        # {
        #     "id": 11,
        #     "fatherid": 10,
        #     "label": "图书电子化",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 12,
        #     "fatherid": 9,
        #     "label": "汉字识别",,
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 13,
            "fatherid": 8,
            "label": "声纹识别",,
            "label_en": "Acoustic fingerprint Recognition）",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "声学指纹（Acoustic fingerprint）是通过特定算法从音频信号中提取的一段数字摘要，用于识别声音样本或者快速定位音频数据库中的相似音频。音频压缩技术的进步以及大容量存储器的出现使得互联网上出现了以音乐为主的海量音频信息，手工选取某首歌曲很多时候已经变得不可能，这直接促使产生了可以进行音乐自动识别的数字音频指纹技术。",
            "description_en": ""
        },
        {
            "id": 14,
            "fatherid": [
                8,
                67,
                188
            ],
            "label": "图像识别（Image Recognition）",
            "label_en": "Image Recognition",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        # {
        #     "id": 15,
        #     "fatherid": 14,
        #     "label": "时光相册",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 16,
            "fatherid": [
                8,
                14,
                17
            ],
            "label": "人脸识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://petapixel.com/assets/uploads/2016/06/facialrecognition_1.jpg",
            "description": "人脸识别，特指利用分析比较人脸视觉特征信息进行身份鉴别的计算机技术。广义的人脸识别实际包括构建人脸识别系统的一系列相关技术，包括人脸图像采集、人脸定位、人脸识别预处理、身份确认以及身份查找等；而狭义的人脸识别特指通过人脸进行身份确认或者身份查找的技术或系统。",
            "description_en": ""
        },
        {
            "id": 17,
            "fatherid": 8,
            "label": "生物特征识别",
            "label_en": "Autonomous Driving",
            "icon_url": "http://whatsnext.nuance.com/wp-content/uploads/eye-and-finger.jpg",
            "description": "生物识别技术（biometrics，也称生物测定学），是指用数理统计方法对生物进行分析，现在多指对生物体（一般特指人）本身的生物特征来区分生物体个体的计算机技术。研究领域主要包括语音、脸、指纹、手掌纹、虹膜、视网膜、体形、个人习惯（例如敲击键盘的力度和频率、签字）等，相应的识别技术就有说话人识别、人脸识别、指纹识别、掌纹识别、虹膜识别、视网膜识别、体形识别、键盘敲击识别、签字识别等。",
            "description_en": ""
        },
        {
            "id": 18,
            "fatherid": 17,
            "label": "虹膜识别",
            "label_en": "Autonomous Driving",
            "icon_url": "http://biometricsecurity.wikispaces.com/file/view/IrisScan.jpg/119837635/280x210/IrisScan.jpg",
            "description": "虹膜又称黄仁，眼睛构造的一部分，虹膜中心有一圆形开口，称为瞳孔，犹如相机当中可调整大小的光圈，内含色素决定眼睛的颜色。因为每个人的虹膜都是不同的，所以也用于身份辨识。",
            "description_en": ""
        },
        {
            "id": 19,
            "fatherid": 17,
            "label": "指纹识别",
            "label_en": "Autonomous Driving",
            "icon_url": "http://digitalfire.ucd.ie/wp-content/uploads/2012/10/JackyFoxBlog.jpg",
            "description": "指纹识别技术是一种生物识别技术，指纹识别系统是一套包括指纹图像获取、处理、特征提取和比对等模块的模式识别系统。常用于需要人员身份确认的场所，如门禁系统、考勤系统、笔记本电脑、银行内部处理、银行支付等。",
            "description_en": ""
        },
        # {
        #     "id": 20,
        #     "fatherid": 19,
        #     "label": "触控ID",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "触控 ID（英语：Touch ID）是苹果公司设计发布的一款指纹识别功能。",
        #     "description_en": ""
        # },
        # {
        #     "id": 21,
        #     "fatherid": 19,
        #     "label": "指纹锁",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 22,
        #     "fatherid": 21,
        #     "label": "指纹解锁（移动设备）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 23,
        #     "fatherid": 17,
        #     "label": "声音识别",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 24,
            "fatherid": [
                8,
                137
            ],
            "label": "语音识别",
            "label_en": "Autonomous Driving",
            "icon_url": "http://www.wired.com/images_blogs/gadgetlab/2009/12/_g7i9162-660x440.jpg",
            "description": "语音识别（speech recognition；语音辨识／言语辨别）技术，也被称为自动语音识别（英语：Automatic Speech Recognition, ASR）、电脑语音识别（英语：Computer Speech Recognition）或是语音转文本识别（英语：Speech To Text, STT），其目标是以电脑自动将人类的语音内容转换为相应的文字。与说话人识别及说话人确认不同，后者尝试识别或确认发出语音的说话人而非其中所包含的词汇内容。",
            "description_en": ""
        },
        # {
        #     "id": 25,
        #     "fatherid": 24,
        #     "label": "小i机器人",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 26,
        #     "fatherid": 24,
        #     "label": "云知声",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 27,
        #     "fatherid": 24,
        #     "label": "科大讯飞",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 28,
        #     "fatherid": 27,
        #     "label": "讯飞口讯",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 29,
        #     "fatherid": 27,
        #     "label": "灵犀语音助手",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 30,
        #     "fatherid": 24,
        #     "label": "语音输入法",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 31,
        #     "fatherid": [
        #         24,
        #         38
        #     ],
        #     "label": "Siri",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 32,
        #     "fatherid": [
        #         24,
        #         38
        #     ],
        #     "label": "Cortana",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 33,
        #     "fatherid": 32,
        #     "label": "微软小娜",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 34,
        #     "fatherid": 24,
        #     "label": "中文语音识别",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 35,
        #     "fatherid": 34,
        #     "label": "语音输入法",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 36,
        #     "fatherid": 24,
        #     "label": "Amazon Echo",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 37,
        #     "fatherid": 24,
        #     "label": "语音系统",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 38,
        #     "fatherid": 24,
        #     "label": "语音助手",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 39,
        #     "fatherid": 38,
        #     "label": "讯飞语点",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 40,
        #     "fatherid": 38,
        #     "label": "出门问问",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 41,
        #     "fatherid": 40,
        #     "label": "Ticwear",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 42,
        #     "fatherid": 40,
        #     "label": "Ticwatch",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 43,
        #     "fatherid": 38,
        #     "label": "Viv",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 44,
        #     "fatherid": 38,
        #     "label": "Google Now",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 45,
        #     "fatherid": 24,
        #     "label": "Nuance",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 46,
            "fatherid": 1,
            "label": "人工智能算法",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 47,
            "fatherid": 46,
            "label": "深度学习（Deep Learning）",
            "label_en": "Deep Learning",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "深度学习（deep learning）是机器学习的分支，是一种试图使用包含复杂结构或由多重非线性变换构成的多个处理层对数据进行高层抽象的算法。",
            "description_en": ""
        },
        {
            "id": 48,
            "fatherid": 47,
            "label": "Theano",
            "label_en": "Theano",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation. <a href='http://www.deeplearning.net/software/theano/' target=_blank></a>",
            "description_en": "Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation. <a href='http://www.deeplearning.net/software/theano/' target=_blank></a>"
        },
        {
            "id": 49,
            "fatherid": [47,58,67]
            "label": "TensorLayer（深度学习库）",
            "label_en": "TensorLayer",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "A Deep Learning Library for Researchers and Engineers built on top of TensorFlow. <a href='https://github.com/tensorlayer/tensorlayer' target=_blank></a>",
            "description_en": "A Deep Learning Library for Researchers and Engineers built on top of TensorFlow. <a href='https://github.com/tensorlayer/tensorlayer' target=_blank></a>"
        },
        {
            "id": 50,
            "fatherid": 47,
            "label": "PyTorch",
            "label_en": "PyTorch",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Tensors and Dynamic neural networks in Python with strong GPU acceleration. <a href='http://pytorch.org/' target=_blank></a>",
            "description_en": "Tensors and Dynamic neural networks in Python with strong GPU acceleration. <a href='http://pytorch.org/' target=_blank></a>"
        },
        {
            "id": 51,
            "fatherid": 47,
            "label": "MXNet",
            "label_en": "MXNet",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Scala, Go, Javascript and more. <a href='https://mxnet.apache.org' target=_blank></a>",
            "description_en": "Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Scala, Go, Javascript and more. <a href='https://mxnet.apache.org' target=_blank></a>"
        },
        {
            "id": 52,
            "fatherid": 47,
            "label": "Torch (深度学习框架)",
            "label_en": "Torch",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Torch is the main package in Torch7 where data structures for multi-dimensional tensors and mathematical operations over these are defined. Additionally, it provides many utilities for accessing files, serializing objects of arbitrary types and other useful utilities. <a href='https://github.com/torch/torch7' target=_blank></a>",
            "description_en": "Torch is the main package in Torch7 where data structures for multi-dimensional tensors and mathematical operations over these are defined. Additionally, it provides many utilities for accessing files, serializing objects of arbitrary types and other useful utilities. <a href='https://github.com/torch/torch7' target=_blank></a>"
        },
        {
            "id": 53,
            "fatherid": 47,
            "label": "迁移学习 (Transfer Learning)",
            "label_en": "Transfer Learning",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 54,
            "fatherid": [47,67,69],
            "label": "卷积神经网络（CNN）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "卷积神经网络（Convolutional Neural Network, CNN）是一种前馈神经网络，它的人工神经元可以响应一部分覆盖范围内的周围单元，对于大型图像处理有出色表现。卷积神经网络由一个或多个卷积层和顶端的全连通层（对应经典的神经网络）组成，同时也包括关联权重和池化层（pooling layer）。这一结构使得卷积神经网络能够利用输入数据的二维结构。与其他深度学习结构相比，卷积神经网络在图像和语音识别方面能够给出更好的结果。这一模型也可以使用反向传播算法进行训练。相比较其他深度、前馈神经网络，卷积神经网络需要考量的参数更少，使之成为一种颇具吸引力的深度学习结构。",
            "description_en": ""
        },
        {
            "id": 55,
            "fatherid": 47,
            "label": "LSTM",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "长短期记忆（英语：Long Short-Term Memory，LSTM）是一种时间递归神经网络（RNN），论文首次发表于1997年。由于独特的设计结构，LSTM适合于处理和预测时间序列中间隔和延迟非常长的重要事件。",
            "description_en": ""
        },
        {
            "id": 56,
            "fatherid": 47,
            "label": "RNN",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "递归神经网络（RNN）是两种人工神经网络的总称。一种是时间递归神经网络（recurrent neural network），另一种是结构递归神经网络（recursive neural network）。时间递归神经网络的神经元间连接构成矩阵，而结构递归神经网络利用相似的神经网络结构递归构造更为复杂的深度网络。RNN一般指代时间递归神经网络。",
            "description_en": ""
        },
        {
            "id": 57,
            "fatherid": 47,
            "label": "Caffee（深度学习框架）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Caffe: a fast open framework for deep learning. <a href='http://caffe.berkeleyvision.org/' target=_blank></a>",
            "description_en": "Caffe: a fast open framework for deep learning. <a href='http://caffe.berkeleyvision.org/' target=_blank></a>"
        },
        {
            "id": 58,
            "fatherid": 47,
            "label": "TensorFlow",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "TensorFlow是一个开源软件库，用于各种感知和语言理解任务的机器学习。目前被50个团队用于研究和生产许多Google商业产品，如语音识别、Gmail、Google 相册和搜索，其中许多产品曾使用过其前任软件DistBelief。TensorFlow最初由Google Brain团队开发，用于Google的研究和生产，于2015年11月9日在Apache 2.0开源许可证下发布。<a href='https://tensorflow.org' target=_blank></a>",
            "description_en": "Computation using data flow graphs for scalable machine learning."
        },
        # {
        #     "id": 59,
        #     "fatherid": 58,
        #     "label": "TensorLayer",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 60,
            "fatherid": 58,
            "label": "TPU（Tensor Processing Unit）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "PU 是 Google 为了 TensorFlow 机器学习框架专门设计的 ASIC 芯片，其第二代为 Cloud TPU",
            "description_en": ""
        },
        {
            "id": 61,
            "fatherid": 47,
            "label": "PaddlePaddle",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "百度开源的并行分布式全功能深度学习平台 <a href='http://www.paddlepaddle.org/' target=_blank></a>",
            "description_en": ""
        },
        {
            "id": 62,
            "fatherid": [
                46,
                123,
                121
            ],
            "label": "AlphaZero",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "AlphaZero 从零开始自学任何棋类游戏，算法适用于所有图版游戏（Board Game）<br> AlphaGo Zero 从零开始自学围棋",
            "description_en": ""
        },
        {
            "id": 63,
            "fatherid": 62,
            "label": "Leela Zero（围棋AI）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Leela 是一款免费围棋软件，稳定正式版为 0.11.0，最新开源版本为 Leela Zero。2017年11月作者 gcp 启动 Leela Zero 项目，以 AlphaGo Zero 和 AlphaZero 论文为基础编程，尝试复现 AlphaGo，并开源，采用分布式训练，受到全世界网友的协助。权重迭代与等级分增长曲线参见官网 Leela Zero。目前，Leela 已经是水平最高的家用围棋软件。",
            "description_en": ""
        },
        # {
        #     "id": 64,
        #     "fatherid": 121,
        #     "label": "Zen（天顶围棋）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 65,
            "fatherid": [
                46,
                67
            ],
            "label": "强化学习（Reinforcement Learning）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "强化学习（英语：Reinforcement learning，简称RL）是机器学习中的一个领域，强调如何基于环境而行动，以取得最大化的预期利益。其灵感来源于心理学中的行为主义理论，即有机体如何在环境给予的奖励或惩罚的刺激下，逐步形成对刺激的预期，产生能获得最大利益的习惯性行为。",
            "description_en": ""
        },
        {
            "id": 66,
            "fatherid": [
                46,
                67
            ],
            "label": "迁移学习（Transfer Learning）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 67,
            "fatherid": [
                1,
                46
            ],
            "label": "机器学习",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "机器学习是人工智能的一个分支。人工智能的研究历史有着一条从以“推理”为重点，到以“知识”为重点，再到以“学习”为重点的自然、清晰的脉络。显然，机器学习是实现人工智能的一个途径，即以机器学习为手段解决人工智能中的问题。机器学习在近30多年已发展为一门多领域交叉学科，涉及概率论、统计学、逼近论、凸分析、计算复杂性理论等多门学科。机器学习理论主要是设计和分析一些让计算机可以自动“学习”的算法。机器学习算法是一类从数据中自动分析获得规律，并利用规律对未知数据进行预测的算法。因为学习算法中涉及了大量的统计学理论，机器学习与推断统计学联系尤为密切，也被称为统计学习理论。",
            "description_en": ""
        },
        {
            "id": 68,
            "fatherid": 67,
            "label": "人工神经网络（Artificial Neural Network）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "人工神经网络（英语：Artificial Neural Network，ANN），简称神经网络（Neural Network，NN）或类神经网络，在机器学习和认知科学领域，是一种模仿生物神经网络（动物的中枢神经系统，特别是大脑）的结构和功能的数学模型或计算模型，用于对函数进行估计或近似。神经网络由大量的人工神经元联结进行计算。大多数情况下人工神经网络能在外界信息的基础上改变内部结构，是一种自适应系统。",
            "description_en": ""
        },
        # {
        #     "id": 69,
        #     "fatherid": 69,
        #     "label": "寒武纪（神经网络处理器）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 70,
            "fatherid": [69,67],
            "label": "Keras",
            "label_en": "Keras",
            "icon_url": "https://keras.io/img/keras-logo-small-2018.jpg",
            "description": "The Python Deep Learning library. <a href='http://keras.io/' target=_blank></a>",
            "description_en": ""
        },
        {
            "id": 71,
            "fatherid": 69,
            "label": "生成对抗网络（GAN）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "生成对抗网络（英语：Generative Adversarial Network，简称GAN）是非监督式学习的一种方法，通过让两个神经网络相互博弈的方式进行学习。该方法由伊恩·古德费洛等人于2014年提出。生成对抗网络由一个生成网络与一个判别网络组成。生成网络从潜在空间（latent space）中随机采样作为输入，其输出结果需要尽量模仿训练集中的真实样本。判别网络的输入则为真实样本或生成网络的输出，其目的是将生成网络的输出从真实样本中尽可能分辨出来。而生成网络则要尽可能地欺骗判别网络。两个网络相互对抗、不断调整参数，最终目的是使判别网络无法判断生成网络的输出结果是否真实。生成对抗网络常用于生成以假乱真的图片。此外，该方法还被用于生成视频、三维物体模型等。",
            "description_en": ""
        },
        # {
        #     "id": 72,
        #     "fatherid": 69,
        #     "label": "卷积神经网络（CNN）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 73,
            "fatherid": 69,
            "label": "神经机器翻译(NMT)",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "神经机器翻译，Neural Machine Tranlation, 简称 NMT, 2014年开始兴起的机器翻译方法，逐渐应用卷积神经网络(CNN)，递归神经网络(RNN)，注意力机制等技术，2016年已基本全面取代传统的统计机器翻译(SMT)。Google，百度，搜狗等已上线神经机器翻译系统。",
            "description_en": ""
        },
        {
            "id": 74,
            "fatherid": 73,
            "label": "OpenNMT",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Open Source Neural Machine Translation in Torch. <a href='http://opennmt.net/' target=_blank></a>",
            "description_en": ""
        },
        {
            "id": 75,
            "fatherid": 67,
            "label": "集成学习（Ensemble Learning)",
            "label_en": "Ensemble Learning",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "集成学习是使用一系列学习器进行学习，并使用某种规则把各个学习结果进行整合从而获得比单个学习器更好的学习效果的一种机器学习方法。比较常见的集成学习方法有随机森林等。",
            "description_en": ""
        },
        # {
        #     "id": 76,
        #     "fatherid": 67,
        #     "label": "TensorLayer(深度学习库）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 77,
            "fatherid": 67,
            "label": "最大期望算法（Expectation Maximization Algorithm）",
            "label_en": "Expectation Maximization Algorithm",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在统计计算中，最大期望（EM）算法是在概率模型中寻找参数最大似然估计或者最大后验估计的算法，其中概率模型依赖于无法观测的隐性变量。最大期望算法经常用在机器学习和计算机视觉的数据聚类（Data Clustering）领域。最大期望算法经过两个步骤交替进行计算，第一步是计算期望（E），利用对隐藏变量的现有估计值，计算其最大似然估计值；第二步是最大化（M），最大化在E步上求得的最大似然值来计算参数的值。M步上找到的参数估计值被用于下一个E步计算中，这个过程不断交替进行。",
            "description_en": ""
        },
        {
            "id": 78,
            "fatherid": 67,
            "label": "社会网络分析",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "社会网络（英语：Social network），是由许多节点以及节点间关系构成的一个网络结构。节点通常是指个人或组织（又称社团）。社会网络代表各种社会关系，经由这些社会关系，把从偶然相识的泛泛之交到紧密结合的家人关系的各种人们或组织串连起来。社会网络依赖于一种到多种关系而形成，如价值观、理想、观念、兴趣爱好、友谊、血缘关系、共同厌恶的事物、冲突或贸易。由此产生的网络结构往往是非常复杂的。社会网络分析是用来查看节点、链接之间的社会关系的分析方式。",
            "description_en": ""
        },
        # {
        #     "id": 79,
        #     "fatherid": 67,
        #     "label": "卷积神经网络",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 80,
            "fatherid": 67,
            "label": "决策树（Decision Tree）",
            "label_en": "Decision Tree",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "决策论中 （如风险管理），决策树（Decision tree）由一个决策图和可能的结果（包括资源成本和风险）组成， 用来创建到达目标的规划。决策树建立并用来辅助决策，是一种特殊的树结构。决策树是一个利用像树一样的图形或决策模型的决策支持工具，包括随机事件结果，资源代价和实用性。它是一个算法显示的方法。决策树经常在运筹学中使用，特别是在决策分析中，它帮助确定一个能最可能达到目标的策略。如果在实际中，决策不得不在没有完备知识的情况下被在线采用，一个决策树应该平行概率模型作为最佳的选择模型或在线选择模型算法。决策树的另一个使用是作为计算条件概率的描述性手段。",
            "description_en": ""
        },
        # {
        #     "id": 81,
        #     "fatherid": 67,
        #     "label": "高维数据分析",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 82,
            "fatherid": 67,
            "label": "贝叶斯统计",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "贝叶斯定理（英语：Bayes' theorem）是概率论中的一个定理，它跟随机变量的条件概率以及边缘概率分布有关。在有些关于概率的解释中，贝叶斯定理（贝叶斯公式）能够告知我们如何利用新证据修改已有的看法。这个名称来自于托马斯·贝叶斯。",
            "description_en": ""
        },
        {
            "id": 83,
            "fatherid": [67,82,108]
            "label": "高斯过程机器学习",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "高斯过程是基于统计学习理论和贝叶斯理论发展起来的一种机器学习方法，适于处理高维度、小样本和非线性等复杂回归问题，且泛化能力强，与神经网络、支持向量机相比，GP具有容易实现、超参数自适应获取、非参数推断灵活以及输出具有概率意义等优点。",
            "description_en": ""
        },
        {
            "id": 84,
            "fatherid": [
                67,
                116,
                163
            ],
            "label": "异常检测（Anomaly Detection）",
            "label_en": "Anomaly Detection",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在数据挖掘中，异常检测（英语：Anomaly Detection）对不匹配预期模式或数据集中其他项目的项目、事件或观测值的识别。通常异常项目会转变成银行欺诈、结构缺陷、医疗问题、文本错误等类型的问题。异常也被称为离群值、新奇、噪声、偏差和例外。",
            "description_en": ""
        },
        {
            "id": 85,
            "fatherid": 84,
            "label": "哈希函数",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "散列函数（英语：Hash function）又称散列算法、哈希函数，是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值（hash values，hash codes，hash sums，或hashes）的指纹。散列值通常用一个短的随机字母和数字组成的字符串来代表。好的散列函数在输入域中很少出现散列冲突。在散列表和数据处理中，不抑制冲突来区别数据，会使得数据库记录更难找到。",
            "description_en": ""
        },
        {
            "id": 86,
            "fatherid": 85,
            "label": "SHA-1",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "SHA-1（英语：Secure Hash Algorithm 1，中文名：安全散列算法1）是一种密码散列函数，美国国家安全局设计，并由美国国家标准技术研究所（NIST）发布为联邦数据处理标准（FIPS）[2]。SHA-1可以生成一个被称为消息摘要的160位（20字节）散列值，散列值通常的呈现形式为40个十六进制数。SHA-1已经不再视为可抵御有充足资金、充足计算资源的攻击者。",
            "description_en": ""
        },
        {
            "id": 87,
            "fatherid": 85,
            "label": "MD5",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "MD5消息摘要算法（英语：MD5 Message-Digest Algorithm），一种被广泛使用的密码散列函数，可以产生出一个128位（16字节）的散列值（hash value），用于确保信息传输完整一致。MD5由美国密码学家罗纳德·李维斯特（Ronald Linn Rivest）设计，于1992年公开，用以取代MD4算法。这套算法的程序在 RFC 1321 中被加以规范。将数据（如一段文字）运算变为另一固定长度值，是散列算法的基础原理。",
            "description_en": ""
        },
        {
            "id": 88,
            "fatherid": 67,
            "label": "学习理论",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "学习理论是教育学和教育心理学的一门分支学科，描述或说明人类和动物学习的类型、过程，以及有效学习的条件。",
            "description_en": ""
        },
        {
            "id": 89,
            "fatherid": 67,
            "label": "数据降维",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在机器学习和统计学领域，降维是指在某些限定条件下，降低随机变量个数，得到一组“不相关”主变量的过程[1]。 降维可进一步细分为特征选择和特征提取两大方法。",
            "description_en": ""
        },
        {
            "id": 90,
            "fatherid": 89,
            "label": "主成分分析（Principal Components Analysis，PCA）",
            "label_en": "Principal Components Analysis",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在多元统计分析中，主成分分析（英语：Principal components analysis，PCA）是一种分析、简化数据集的技术。主成分分析经常用于减少数据集的维数，同时保持数据集中的对方差贡献最大的特征。这是通过保留低阶主成分，忽略高阶主成分做到的。这样低阶成分往往能够保留住数据的最重要方面。但是，这也不是一定的，要视具体应用而定。由于主成分分析依赖所给数据，所以数据的准确性对分析结果影响很大。",
            "description_en": ""
        },
        {
            "id": 91,
            "fatherid": 89,
            "label": "因子分析（Factor Analysis）",
            "label_en": "Factor Analysis",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 92,
            "fatherid": 67,
            "label": "PRML",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "PRML一般指代Pattern Recognition and Machine Learning一书。该书出版于2006年，是贝叶斯机器学习领域的经典之作。作者为Christopher M. Bishop，现为剑桥微软研究院实验室主任。",
            "description_en": ""
        },
        # {
        #     "id": 93,
        #     "fatherid": 67,
        #     "label": "图像识别",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 94,
        #     "fatherid": 67,
        #     "label": "戴森（Dyson）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 95,
        #     "fatherid": 64,
        #     "label": "无叶电风扇",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 96,
        #     "fatherid": [67,82],
        #     "label": "高斯过程机器学习",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 97,
        #     "fatherid": 67,
        #     "label": "sklearn",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 98,
            "fatherid": 67,
            "label": "半监督学习（Semi-supervised Learning）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在有标签数据+无标签数据混合成的训练数据中使用的机器学习算法，一般假设，无标签数据比有标签数据多，甚至多得多。半监督深度学习，深度学习需要用到大量有标签数据，即使在大数据时代，干净能用的有标签数据也是不多的，由此引发深度学习与半监督学习的结合。",
            "description_en": ""
        },
        {
            "id": 99,
            "fatherid": 67,
            "label": "深度学习（Deep Learning)",
            "label_en": "Deep Learning",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "深度学习（deep learning）是机器学习的分支，是一种试图使用包含复杂结构或由多重非线性变换构成的多个处理层对数据进行高层抽象的算法。深度学习是机器学习中一种基于对数据进行表征学习的算法。观测值（例如一幅图像）可以使用多种方式来表示，如每个像素强度值的向量，或者更抽象地表示成一系列边、特定形状的区域等。而使用某些特定的表示方法更容易从实例中学习任务（例如，人脸识别或面部表情识别）。深度学习的好处是用非监督式或半监督式的特征学习和分层特征提取高效算法来替代手工获取特征。",
            "description_en": ""
        },
        # {
        #     "id": 100,
        #     "fatherid": 67,
        #     "label": "Keras",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 101,
            "fatherid": [
                67,
                137
            ],
            "label": "word2vec",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "将字词转换成多维向量的技术，由 Google 发布。<a href='https://www.tensorflow.org/tutorials/word2vec' target=_blank></a>",
            "description_en": ""
        },
        {
            "id": 102,
            "fatherid": 67,
            "label": "特征选择（Feature Selection）",
            "label_en": "Feature Selection",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在机器学习和统计学中，特征选择（英语：feature selection）也被称为变量选择、属性选择 或变量子集选择 。它是指：为了构建模型而选择相关特征（即属性、指标）子集的过程。",
            "description_en": ""
        },
        {
            "id": 103,
            "fatherid": 67,
            "label": "xgboost",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library, for Python, R, Java, Scala, C++ and more. Runs on single machine, Hadoop, Spark, Flink and DataFlow. <a href='https://github.com/dmlc/xgboost' target=_blank></a>",
            "description_en": ""
        },
        # {
        #     "id": 104,
        #     "fatherid": 67,
        #     "label": "贝叶斯分类",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 105,
            "fatherid": 67,
            "label": "监督式学习（Supervised learning）",
            "label_en": "Supervised learning",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "监督式学习（英语：Supervised learning），是一个机器学习中的方法，可以由训练资料中学到或建立一个模式（函数 / learning model），并依此模式推测新的实例。训练资料是由输入物件（通常是向量）和预期输出所组成。函数的输出可以是一个连续的值（称为回归分析），或是预测一个分类标签（称作分类）。",
            "description_en": ""
        },
        {
            "id": 106,
            "fatherid": [
                105,
                107
            ],
            "label": "SVM（支持向量机）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在机器学习中，支持向量机（英语：support vector machine，常简称为SVM，又名支持向量网络[1]）是在分类与回归分析中分析数据的监督式学习模型与相关的学习算法。给定一组训练实例，每个训练实例被标记为属于两个类别中的一个或另一个，SVM训练算法创建一个将新的实例分配给两个类别之一的模型，使其成为非概率二元线性分类器。SVM模型是将实例表示为空间中的点，这样映射就使得单独类别的实例被尽可能宽的明显的间隔分开。然后，将新的实例映射到同一空间，并基于它们落在间隔的哪一侧来预测所属类别。",
            "description_en": ""
        },
        # {
        #     "id": 107,
        #     "fatherid": 105,
        #     "label": "分类算法",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 108,
            "fatherid": 105,
            "label": "回归分析（英语：Regression Analysis）",
            "label_en": "Regression Analysis",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "回归分析（英语：Regression Analysis）是一种统计学上分析数据的方法，目的在于了解两个或多个变量间是否相关、相关方向与强度，并建立数学模型以便观察特定变量来预测研究者感兴趣的变量。更具体的来说，回归分析可以帮助人们了解在只有一个自变量变化时因变量的变化量。一般来说，通过回归分析我们可以由给出的自变量估计因变量的条件期望。",
            "description_en": ""
        },
        # {
        #     "id": 109,
        #     "fatherid": 108,
        #     "label": "变量选择",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 110,
        #     "fatherid": 108,
        #     "label": "回归诊断",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 111,
            "fatherid": 108,
            "label": "一般线性模型",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "一般线性模型（the General Linear Model, GLM）是一个统计学上常见的线性模型。这个模型在计量经济学的应用中十分重要。",
            "description_en": ""
        },
        {
            "id": 112,
            "fatherid": 111,
            "label": "逻辑回归（Logistic regression）",
            "label_en": "Logistic regression",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "逻辑回归（英语：Logistic regression 或logit regression），即逻辑模型（英语：Logit model，也译作“评定模型”、“分类评定模型”）是离散选择法模型之一，属于多重变量分析范畴，是社会学、生物统计学、临床、数量心理学、计量经济学、市场营销等统计实证分析的常用方法。",
            "description_en": ""
        },
        # {
        #     "id": 113,
        #     "fatherid": 108,
        #     "label": "高斯过程机器学习",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 114,
        #     "fatherid": 108,
        #     "label": "多元线性回归",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 115,
            "fatherid": 108,
            "label": "线性回归（Linear regression）",
            "label_en": "Linear regression",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "在统计学中，线性回归（Linear regression）是利用称为线性回归方程的最小二乘函数对一个或多个自变量和因变量之间关系进行建模的一种回归分析。这种函数是一个或多个称为回归系数的模型参数的线性组合。只有一个自变量的情况称为简单回归，大于一个自变量情况的叫做多元回归。（这反过来又应当由多个相关的因变量预测的多元线性回归区别[来源请求]，而不是一个单一的标量变量。）",
            "description_en": ""
        },
        {
            "id": 116,
            "fatherid": 67,
            "label": "无监督学习",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "非监督式学习是一种机器学习的方式，并不需要人力来输入标签。它是监督式学习和强化学习等策略之外的一种选择。在监督式学习中，典型的任务是分类和回归分析，且需要使用到人工预先准备好的范例(base)。一个常见的非监督式学习是数据聚类。在人工神经网络中，生成对抗网络（GAN）、自组织映射（SOM）和适应性共振理论（ART）则是最常用的非监督式学习。",
            "description_en": ""
        },
        {
            "id": 117,
            "fatherid": 116,
            "label": "聚类分析（Cluster analysis）",
            "label_en": "Cluster analysis",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "聚类分析（英语：Cluster analysis，亦称为群集分析）是对于统计数据分析的一门技术，在许多领域受到广泛应用，包括机器学习，数据挖掘，模式识别，图像分析以及生物信息。聚类是把相似的对象通过静态分类的方法分成不同的组别或者更多的子集（subset），这样让在同一个子集中的成员对象都有相似的一些属性，常见的包括在坐标系中更加短的空间距离等。",
            "description_en": ""
        },
        # {
        #     "id": 118,
        #     "fatherid": 117,
        #     "label": "聚类算法",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 119,
            "fatherid": 46,
            "label": "提升方法（Boosting）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "提升方法（Boosting），是一种可以用来减小监督式学习中偏差的机器学习元算法。面对的问题是迈可·肯斯（Michael Kearns）提出的：[1]一组“弱学习者”的集合能否生成一个“强学习者”？弱学习者一般是指一个分类器，它的结果只比随机分类好一点点；强学习者指分类器的结果非常接近真值。",
            "description_en": ""
        },
        {
            "id": 120,
            "fatherid": 1,
            "label": "人机对战",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 121,
            "fatherid": 120,
            "label": "对弈人工智能",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 122,
            "fatherid": 121,
            "label": "五子棋AI",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 123,
            "fatherid": 121,
            "label": "AlphaGo",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 124,
            "fatherid": 123,
            "label": "Leela",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 125,
            "fatherid": 121,
            "label": "CrazyStone",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 126,
            "fatherid": 120,
            "label": "图灵测试",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 127,
            "fatherid": 126,
            "label": "反图灵测试",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 128,
            "fatherid": 126,
            "label": "验证码",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 129,
            "fatherid": 128,
            "label": "验证码",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 130,
            "fatherid": 129,
            "label": "reCAPTCHA",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 131,
            "fatherid": 129,
            "label": "短信验证码",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 132,
            "fatherid": 120,
            "label": "计算机博弈",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 133,
            "fatherid": 1,
            "label": "智慧城市",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 134,
            "fatherid": 133,
            "label": "智能交通",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 135,
            "fatherid": 134,
            "label": "电子警察",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 136,
            "fatherid": 133,
            "label": "智能医疗",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 137,
            "fatherid": 1,
            "label": "自然语言处理",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 138,
            "fatherid": 137,
            "label": "HNC概念层次网络理论",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 139,
            "fatherid": 137,
            "label": "文本分类",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 140,
            "fatherid": 137,
            "label": "语义识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 141,
            "fatherid": 137,
            "label": "命名实体识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 142,
            "fatherid": 137,
            "label": "语料库",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 143,
            "fatherid": 137,
            "label": "分词",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 144,
            "fatherid": 143,
            "label": "Sphinx(检索引擎）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        # {
        #     "id": 145,
        #     "fatherid": 137,
        #     "label": "语音识别",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 146,
            "fatherid": 137,
            "label": "主题模型",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 147,
            "fatherid": [
                146,
                175
            ],
            "label": "LDA",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 148,
            "fatherid": 146,
            "label": "pLSA",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 149,
            "fatherid": 146,
            "label": "LSA",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 150,
            "fatherid": 137,
            "label": "文本挖掘",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 151,
            "fatherid": 137,
            "label": "简繁转换",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 152,
            "fatherid": 137,
            "label": "word embedding",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 153,
            "fatherid": 137,
            "label": "语义搜索",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 154,
            "fatherid": 137,
            "label": "机器翻译",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 155,
            "fatherid": 154,
            "label": "神经机器翻译（NMT) ",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 156,
            "fatherid": 155,
            "label": "OpenNMT) ",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 157,
            "fatherid": 137,
            "label": "问答系统",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 158,
            "fatherid": 157,
            "label": "Question2Answer",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 159,
            "fatherid": 137,
            "label": "NLTK",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 160,
            "fatherid": 1,
            "label": "语音合成",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 161,
            "fatherid": 160,
            "label": "TTS(text-to-speech)",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 162,
            "fatherid": 1,
            "label": "专家系统",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 163,
            "fatherid": 1,
            "label": "数据挖掘",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 164,
            "fatherid": 163,
            "label": "核心数据指标",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 165,
            "fatherid": 163,
            "label": "用户画像",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 166,
            "fatherid": 163,
            "label": "topic model",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        # {
        #     "id": 167,
        #     "fatherid": 163,
        #     "label": "Kaggle",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 168,
            "fatherid": 163,
            "label": "多媒体数据挖掘",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 169,
            "fatherid": 163,
            "label": "文本分析",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 170,
            "fatherid": 163,
            "label": "决策树",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 171,
            "fatherid": 163,
            "label": "数据挖掘SPSS",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 172,
            "fatherid": 163,
            "label": "文本挖掘",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 173,
            "fatherid": 163,
            "label": "数据科学家",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 174,
            "fatherid": 1,
            "label": "机器人",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 175,
            "fatherid": 1,
            "label": "推荐系统",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 176,
            "fatherid": 175,
            "label": "推荐引擎",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        # {
        #     "id": 177,
        #     "fatherid": 176,
        #     "label": "豆瓣猜",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 178,
        #     "fatherid": 175,
        #     "label": "YouTube",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 179,
        #     "fatherid": 178,
        #     "label": "YouTuber",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 180,
        #     "fatherid": 178,
        #     "label": "Elsagate",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 181,
        #     "fatherid": 178,
        #     "label": "YouTube Red(付费会员）",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        # {
        #     "id": 182,
        #     "fatherid": 178,
        #     "label": "youtube版权",
        #     "label_en": "Autonomous Driving",
        #     "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
        #     "description": "",
        #     "description_en": ""
        # },
        {
            "id": 183,
            "fatherid": 175,
            "label": "个性化推荐",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 184,
            "fatherid": 183,
            "label": "个性化推荐技术",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 185,
            "fatherid": 175,
            "label": "推荐系统实现",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 186,
            "fatherid": 1,
            "label": "人工智能产品",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 187,
            "fatherid": 1,
            "label": "人工智能公司",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 188,
            "fatherid": 1,
            "label": "计算机视觉",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 189,
            "fatherid": 188,
            "label": "视觉显著性",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 190,
            "fatherid": 188,
            "label": "OpenCV",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 191,
            "fatherid": 188,
            "label": "图像处理",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 192,
            "fatherid": 188,
            "label": "物体识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 193,
            "fatherid": 188,
            "label": "行人重识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 194,
            "fatherid": 188,
            "label": "增强现实（AR）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 195,
            "fatherid": 194,
            "label": "HoloLens",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 196,
            "fatherid": 194,
            "label": "刀剑神域",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 197,
            "fatherid": 194,
            "label": "实时渲染",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 198,
            "fatherid": [
                197,
                200
            ],
            "label": "Cycles 4D",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 199,
            "fatherid": 197,
            "label": "Twinmotion",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 200,
            "fatherid": 197,
            "label": "Cycles渲染器",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 201,
            "fatherid": 200,
            "label": "gpu渲染器",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 202,
            "fatherid": 201,
            "label": "Twinmotion",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 203,
            "fatherid": 188,
            "label": "AR游戏",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 204,
            "fatherid": 188,
            "label": "Niantic,Inc.",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 205,
            "fatherid": 188,
            "label": "RealSense",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 206,
            "fatherid": 188,
            "label": "Magic Leap",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 207,
            "fatherid": 206,
            "label": "Magic Leap One",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 208,
            "fatherid": 188,
            "label": "图像检索",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 209,
            "fatherid": 208,
            "label": "基于内容的图像检索",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 210,
            "fatherid": 188,
            "label": "人脸识别",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 211,
            "fatherid": 188,
            "label": "行人检测",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 212,
            "fatherid": 188,
            "label": "目标检测",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        },
        {
            "id": 213,
            "fatherid": 188,
            "label": "运动推断结构（SfM）",
            "label_en": "Autonomous Driving",
            "icon_url": "https://img-ac.oss-cn-zhangjiakou.aliyuncs.com/ai_icon_201804281521.jpg",
            "description": "",
            "description_en": ""
        }
    ]