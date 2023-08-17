# Personalized-EduChat
<p align="center" width="100%">
<a href="https://www.educhat.top/" target="_blank"><img src="https://github.com/icalk-nlp/Personalized-EduChat/blob/main/docs/imgs/EduChat.jpeg" alt="EduChat" style="width: 50%; min-width: 300px; display: block; margin: auto;"></a>
</p>
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/LianjiaTech/BELLE/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY--NC%204.0-blue.svg)](https://github.com/LianjiaTech/BELLE/blob/main/LICENSE)
[![Generic badge](https://img.shields.io/badge/WeChat-EduChat-green.svg?logo=wechat)](https://github.com/icalk-nlp/Personalized-EduChat/blob/main/docs/imgs/WeChat_EduChat.JPG)
[![Generic badge](https://img.shields.io/badge/🤗-Huggingface%20Repo-577CF6.svg)](https://huggingface.co/ecnu-icalk)

## 目录

- [介绍](#fountain_pen-介绍)
- [开源清单](#spiral_notepad-开源清单)
- [本地部署](#robot-本地部署)
  - [下载安装](#下载安装)
  - [配置](#配置)
  - [使用示例](#使用示例)
- [开源协议](#page_with_curl-开源协议)
- [引用](#引用)

----

## :fountain_pen: 介绍

Personalized-EduChat是一个针对教育垂直领域的对话大模型项目，由华东师范大学计算机科学与技术学院的[EduNLP团队](https://www.educhat.top/#/)开发。该项目旨在贯彻“以人为本”的教育理念，通过预训练大模型为基底的教育对话大模型相关技术，融合多样化的教育垂直领域数据，提供个性化、引导式、身心全面发展的教育支持。

**基础能力**：

![image](https://github.com/icalk-nlp/Personalized-EduChat/blob/main/docs/imgs/基础能力.gif)

## :spiral_notepad: 开源清单

### 模型
**注意：使用前按照模型介绍页面中的使用方法部分解密**
- **educhat-search-002-7b**（近期开源）：在**educhat-sft-002-7b**基础上加入搜索功能
- [**educhat-sft-002-7b**](https://huggingface.co/ecnu-icalk/educhat-sft-002-7b)：在educhat-base-002-7b基础上，使用我们构建的教育领域多技能数据微调后得到
- [**educhat-base-002-7b**](https://huggingface.co/ecnu-icalk/educhat-base-002-7b)：使用educhat-sft-002-data-osm数据训练得到
- [**educhat-sft-002-13b**](https://huggingface.co/ecnu-icalk/educhat-sft-002-13b)：训练方法与educhat-sft-002-7b相同，模型大小升级为13B
- [**educhat-base-002-13b**](https://huggingface.co/ecnu-icalk/educhat-base-002-13b)：训练方法与educhat-base-002-7b相同，模型大小升级为13B

### 数据

- [**educhat-sft-002-data-osm**](https://huggingface.co/datasets/ecnu-icalk/educhat-sft-002-data-osm): 混合多个开源中英指令、对话数据，并去重后得到，约400w



## :robot: 本地部署

### 下载安装

1. 环境检查

```bash
# 使用conda安装环境，确保python版本为3.9以上
conda create --name env_name python=3.9
# 激活环境
conda activate env_name
```

2. 安装依赖

```bash
# 拉取仓库
git clone https://github.com/icalk-nlp/Personalized-EduChat.git
# 进入目录
cd Personalized-EduChat
# 安装依赖
pip install -r requirements.txt
```

### 配置

在 `config/config.yaml` 中配置你的`EDUCHAT_SECRET_URL`

```python
# 该EDUCHAT_SECRET_URL为启动API服务得到的URL
EDUCHAT_SECRET_URL: 'YOUR_EDUCHAT_SECRET_URL'
```

### 使用示例

#### 网页demo

```bash
cd server
python educhat_gradio.py
```

#### 教材问答

1. 启动 API 服务

```bash
cd server
# 启动 API 服务，这将返回一个url
python educhat_api.py
```

2. 进行教材问答

```bash
# 回到项目根目录，然后运行document_conversation.py
python document_conversation.py
```

## :page_with_curl: 开源协议、模型局限、使用限制与免责声明

本项目所含代码采用[Apache 2.0](https://github.com/icalk-nlp/Personalized-EduChat/blob/main/LICENSE)协议，数据采用[CC BY-NC 4.0](https://github.com/icalk-nlp/EduChat/blob/main/DATA_LICENSE)协议。

尽管我们对EduChat进行了优化，但仍存在以下问题，需要进行改进：

- 当涉及到事实性指令时，可能会产生错误的回答，与实际事实相悖。

- 模型回复可能存在偏见，有可能生成危险性言论。

- 在某些场景中，比如推理、代码、多轮对话等方面，模型的能力仍有待提高。

鉴于上述模型的局限性，我们要求开发者仅将我们开源的代码、数据、模型以及由该项目生成的衍生物用于研究目的，禁止用于商业用途，以及其他可能对社会带来危害的用途。

本项目仅供研究目的使用，项目开发者对于使用本项目（包括但不限于数据、模型、代码等）所导致的任何危害或损失不承担责任。详情请参考该[免责声明](https://github.com/icalk-nlp/EduChat/blob/main/LICENSE/DISCLAIMER)。

## 引用

EduChat: A Large-Scale Language Model-based Chatbot System for Intelligent Education

链接：https://arxiv.org/abs/2308.02773

如果使用本项目的代码、数据或模型，请引用本项目论文：

```
@article{educhat2023,
  title={EduChat: A Large-Scale Language Model-based Chatbot System for Intelligent Education},
  author={Yuhao Dan, Zhikai Lei, Yiyang Gu, Yong Li, Jianghao Yin, Jiaju Lin, Linhao Ye, Zhiyan Tie, Yougen Zhou, Yilei Wang, Aimin Zhou, Ze Zhou, Qin Chen, Jie Zhou, Liang He, Xipeng Qiu},
  journal={arXiv preprint arXiv:2308.02773},
  year={2023}
}
```
