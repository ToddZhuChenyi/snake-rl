# 🐍 Snake RL Project | 贪吃蛇强化学习项目

<div align="center">
<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Stable--Baselines3-2.0+-green?style=flat-square"/>
<img src="https://img.shields.io/badge/PyTorch-2.0+-ee4c2c?style=flat-square&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Gymnasium-1.1+-yellow?style=flat-square"/>
<img src="https://img.shields.io/badge/Pygame-2.0+-brightgreen?style=flat-square&logo=pygame&logoColor=white"/>
</div>

---

## ✨ 项目简介 | Introduction

本项目实现了一个基于**Stable-Baselines3 + Gymnasium + PyTorch** 的可训练贪吃蛇强化学习环境，支持：
- ✅ 自定义奖励函数（Reward Shaping）
- ✅ 自定义状态空间（Observation Design）
- ✅ 并行环境训练（Vectorized Env）
- ✅ Tensorboard 日志
- ✅ 支持 GPU/MPS

A trainable Snake RL environment with **custom reward shaping, observation design, vectorized training, and Tensorboard support**.  
Perfect for RL research, demo, or course projects.

---

## 📦 目录结构 | Project Structure

```text
snake_rl_project/
├── models/           # 训练好的模型 / Saved models
├── snake_envs/       # 环境相关 / Environment code
│   ├── game_logic.py
│   └── snake_env.py
├── train.py          # 训练脚本 / Train agent
├── evaluate.py       # 评估与可视化 / Evaluate agent
├── config.yaml       # 超参数配置 / Hyperparameters
├── requirements.txt  # 依赖列表 / Requirements
└── README.md
```

## 🚀 快速上手 | Quick Start
### 1. 安装依赖 / Install dependencies
```bash
pip install -r requirements.txt
```

### 2. 训练模型 / Train the agent
```bash
python train.py
```

### 3. 评估和可视化 / Evaluate and visualize
```bash
python evaluate.py
```

### 4. Tensorboard 可视化 (可选) / Tensorboard Visualization (Optional)
```bash
tensorboard --logdir runs
# 打开 http://localhost:6006
```

## ✨ 项目亮点 | Highlights

- 完全自定义奖励设计，轻松探索不同RL训练策略
- 多种观察空间与特征提取方式，适配MLP/CNN模型
- 支持矢量化并行训练，高效利用多核CPU
- 训练过程集成 Tensorboard，轻松可视化和对比
- 代码结构清晰，上手简单，适合RL新手和研究者

## 🙋‍♂️ 常见问题 | FAQ

- Q: 训练慢怎么办？  
  A: 可调大 n_envs/n_steps，或用更小地图测试。

- Q: 如何自定义奖励/观测？  
  A: 修改 snake_env 或 game_logic 文件中相应部分即可。

- Q: MPS支持吗？  
  A: Mac M1/M2/M3 可用 PyTorch MPS，但训练速度依然主要受CPU影响。
