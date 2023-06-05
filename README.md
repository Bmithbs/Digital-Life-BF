
# Digital Life Fay 

本项目主要采用 Fay 控制器，Fay 专注于构建智能数字助理的开源解决方案。它提供了灵活的模块化设计，使开发人员能够定制和组合各种功能模块，包括情绪分析、NLP 处理、语音合成和语音输出等。Fay 数字人助理版为开发人员提供了强大的工具和资源，用于构建智能、个性化和多功能的数字助理应用。通过该版本，开发人员可以轻松创建适用于各种场景和领域的数字人助理，为用户提供智能化的语音交互和个性化服务。

## 推荐集成

- 集成 VisualGLM：B 站视频
- 给 Fay 加上本地免费语音识别（达摩院 funaar）: https://www.bilibili.com/video/BV1qs4y1g74e/?share_source=copy_web&vd_source=64cd9062f5046acba398177b62bea9ad
- 消费级 pc 大模型（ChatGLM-6B 的基础上前置 Rasa 会话管理）：https://m.bilibili.com/video/BV1D14y1f7pr 
- UE5 工程：https://github.com/xszyou/fay-ue5
- 视频三维重建（真人 2D 驱动）：https://github.com/waityousea/xuniren

## Fay 数字人助理版

- PC 远程助理 [`PC demo`](https://github.com/TheRamU/Fay/tree/main/python_connector_demo)
- 手机远程助理 [`android demo`](https://github.com/TheRamU/Fay/tree/main/android_connector_demo)
- 与数字形象通讯（非必须，控制器需要关闭“面板播放”）控制器与采用 WebSocket 方式与 UE5 通讯
  - 下载工程：[https://pan.baidu.com/s/1RBo2Pie6A5yTrCf1cn_Tuw?pwd=ck99](https://pan.baidu.com/s/1RBo2Pie6A5yTrCf1cn_Tuw?pwd=ck99)
  - 下载 windows 运行包：[https://pan.baidu.com/s/1CsJ647uV5rS2NjQH3QT0Iw?pwd=s9s8](https://pan.baidu.com/s/1CsJ647uV5rS2NjQH3QT0Iw?pwd=s9s8)
  - 工程及运行包：https://github.com/xszyou/fay-ue5
  - 通讯地址：[`ws://127.0.0.1:10002`](ws://127.0.0.1:10002)（已接通）
  - 消息格式：查看 [WebSocket.md](https://github.com/TheRamU/Fay/blob/main/WebSocket.md)

- 与远程音频输入输出设备连接（非必须，外网需要配置 http://ngrok.cc tcp 通道的 clientid）

  - 控制器与采用 socket（非 websocket) 方式与 音频输出设备通讯
  - 内网通讯地址：[`ws://127.0.0.1:10001`](ws://127.0.0.1:10001)
  - 外网通讯地址：通过 http://ngrok.cc 获取
  - 消息格式：参考 [remote_audio.py](https://github.com/TheRamU/Fay/blob/main/python_connector_demo/remote_audio.py)

<div align="center">
<img src="images/Dingtalk_20230131122109.jpg">
</div>


## Fay controller core logic

![](images/luoji.png)


### Content structure

```
.
├── main.py					# 程序主入口
├── fay_booter.py			# 核心启动模块
├── config.json				# 控制器配置文件
├── system.conf				# 系统配置文件
├── ai_module
│   ├── ali_nls.py			# 阿里云 实时语音
│   ├── ms_tts_sdk.py       # 微软 文本转语音
│   ├── xf_aiui.py          # 讯飞 人机交互-自然语言处理
│   ├── chatgpt.py          # gpt3.5 对接
│   ├── nlp_gpt.py          # 对接 chat.openai.com（免 key)
│   ├── yuan_1_0.py         # 浪潮。源大模型对接
│   ├── nlp_rasa.py         # ChatGLM-6B 的基础上前置 Rasa 会话管理（强烈推荐）
│   ├── nlp_VisualGLM.py    # 对接多模态大语言模型 VisualGLM-6B
│   ├── yolov8.py           # yolov8 资态识别
│   └── xf_ltp.py           # 讯飞 情感分析
├── bin                     # 可执行文件目录
├── core                    # 数字人核心
│   ├── fay_core.py         # 数字人核心模块
│   ├── recorder.py         # 录音器
│   ├── tts_voice.py        # 语音生源枚举
│   ├── viewer.py           # 抖音直播间接入模块
│   └── wsa_server.py       # WebSocket 服务端
├── gui                     # 图形界面
│   ├── flask_server.py     # Flask 服务端
│   ├── static
│   ├── templates
│   └── window.py           # 窗口模块
├── scheduler
│   └── thread_manager.py   # 调度管理器
├── utils                   # 工具模块
    ├── config_util.py      
    ├── storer.py
    └── util.py
└── test                    # 都是惊喜
```

## Roadmap

- [ ] GPT Memory
- [ ] Memory Selector
- [ ] Memory information set
- [ ] Autonomous simulation of conversational style

## Upgrade log

2023.05.27：

+ 修复多个 bug：消息框换行及空格问题、语音识别优化；
+ 彩蛋转正，Fay 沟通与 ChatGPT 并行；
+ 加入 yolov8 姿态识别；
+ 加入 VisualGLM-6B 多模态单机离线大语言模型。

2023.05.12：

+ 打出 Fay 数字人助理版作为主分支（带货版移到分支 [`fay-sales-edition`](https://github.com/TheRamU/Fay/tree/fay-sales-edition)）；
+ 添加 Fay 助理的文字沟通窗口（文字与语音同步）；
+ 添加沟通记录本地保存功能；
+ 升级 ChatGLM-6B 的应用逻辑，长文本与语音回复分离。

## Installation

1. Available Environments
   - Python 3.9、3.10
   - Windows、macos、linux
2. Install the Requirements
    ```shell
    pip install -r requirements.txt
    ```
3. Configure the secret key
   + 查看 [AI 模块](#ai-模块)
   + 浏览链接，注册并创建应用，将应用密钥填入 `./system.conf` 中

4. Run the Fay controller
    ```shell
    python main.py
    ```

### AI Modules
启动前需填入应用密钥

| 代码模块                  | 描述                       | 链接                                                         |
| ------------------------- | -------------------------- | ------------------------------------------------------------ |
| ./ai_module/ali_nls.py    | 实时语音识别（非必须，免费 3 个月，asr 二选一）    | https://ai.aliyun.com/nls/trans                              |
| ./ai_module/funasr.py    | 达摩院开源免费本地 asr （非必须，asr 二选一）   | fay/test/funasr/README.MD                           |
| ./ai_module/ms_tts_sdk.py | 微软 文本转情绪语音（非必须，不配置时使用免费的 edge-tts） | https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/ |
| ./ai_module/xf_ltp.py     | 讯飞 情感分析              | https://www.xfyun.cn/service/emotion-analysis                |
| ./utils/ngrok_util.py     | ngrok.cc 外网穿透（可选）  | http://ngrok.cc                                              |
| ./ai_module/yuan_1_0.py    | 浪潮源大模型（NLP 多选 1） | https://air.inspur.com/                                              |
| ./ai_module/chatgpt.py     | ChatGPT（NLP 多选 1） | *******                                              |
| ./ai_module/xf_aiui.py    | 讯飞自然语言处理（NLP 多选 1）  | https://aiui.xfyun.cn/solution/webapi                        |
| ./ai_module/nlp_rasa.py    | ChatGLM-6B 的基础上前置 Rasa 会话管理（NLP 多选 1）  | https://m.bilibili.com/video/BV1D14y1f7pr |
| ./ai_module/nlp_VisualGLM.py | 对接 VisualGLM-6B 多模态单机离线大语言模型（NLP 多选 1） | B 站视频 |

## 使用说明

### 使用说明

+ 语音助理：fay 控制器（麦克风输入源开启、面板播放开启）；
+ 远程语音助理：fay 控制器（面板播放关闭）+ 远程设备接入；
+ 数字人互动：fay 控制器（麦克风输入源开启、面板播放关闭、填写性格 Q&A）+ 数字人；
+ 贾维斯、Her：加入我们一起完成。

### 语音指令

| 关闭核心                  | 静音                       | 取消静音                                                         |
| ------------------------- | -------------------------- | ------------------------------------------------------------ |
| 关闭、再见、你走吧   | 静音、闭嘴、我想静静        |   取消静音、你在哪呢、你可以说话了                            |

| 播放歌曲（音乐库暂不可用）                  | 暂停播放                       | 更多                                                         |
| ------------------------- | -------------------------- | ------------------------------------------------------------ |
| 播放歌曲、播放音乐、唱首歌、放首歌、听音乐、你会唱歌吗   | 暂停播放、别唱了、我不想听了        |     没有了。..                          |

### 人设
数字人属性，与用户交互中能做出相应的响应。

- 交互灵敏度：在交互中，数字人能感受用户的情感，并作出反应。最直的体现，就是语气的变化，如 开心/伤心/生气 等。设置灵敏度，可改变用户情感对于数字人的影响程度。
### 接收来源

- 文本输入：通过沟通窗口与助理文本沟通
- 麦克风：选择麦克风设备，实现面对面交互，成为你的伙伴
- socket 远程音频输入：可以接入远程音频输入，远程音频输出

### Related articles

1. 集成消费级 pc 大模型（ChatGLM-6B 的基础上前置 Rasa 会话管理）：https://m.bilibili.com/video/BV1D14y1f7pr 
2. [非常全面的数字人解决方案_郭泽斌之心的博客-CSDN 博客_数字人算法](https://blog.csdn.net/aa84758481/article/details/124758727)
3. 【开源项目：数字人 FAY——Fay 新架构使用讲解】 https://www.bilibili.com/video/BV1NM411B7Ab/?share_source=copy_web&vd_source=64cd9062f5046acba398177b62bea9ad
4. 【开源项目 FAY——UE 工程讲解】https://www.bilibili.com/video/BV1C8411P7Ac?vd_source=64cd9062f5046acba398177b62bea9ad
5. m1 机器安装办法（Gason 提供）：https://www.zhihu.com/question/437075754
6. bilbil 主页：[xszyou 的个人空间_哔哩哔哩_bilibili](https://space.bilibili.com/2111554564)
