# 策场 Signal-Arena-View — 交易可视化面板

> AI Agent 虚拟量化交易竞赛 · 个人学习 & 可视化工具

[策场 Signal Arena](https://signal.coze.com) 是一个 AI Agent 虚拟量化交易竞赛平台。每位参赛者使用 AI Agent 管理 ¥1,000,000 初始资金，在美股、港股、A股市场进行模拟交易，按累计收益率排名。

本项目提供该平台的实时可视化面板，包含持仓监控、资产走势、排行榜、多 Agent 对比等功能。

---

## 功能

- **📊 资产总览** — 总资产、收益率、现金、持仓市值一览
- **📈 资产走势图** — 基于快照数据绘制总资产变化曲线
- **🥧 持仓分布图** — 环形图直观展示各股票和现金占比
- **📋 持仓详情** — 股票数量、成本价、现价、盈亏明细
- **📜 交易记录** — 最近交易历史，含买卖方向、金额、手续费
- **🏆 排行榜** — 全平台 Agent 排名，含走势迷你图
- **👥 管理者库** — 添加多个 API Key 集中对比不同 Agent 的表现
- **🔄 自动刷新** — 每 30 秒自动同步最新数据

---

## 快速开始

### 前置要求

- Python 3.6+
- 策场 Signal Arena 账号及 Agent API Key

### 启动

```bash
# 克隆或进入项目目录
cd ForSignal

# 直接运行服务器
python server.py
```

打开浏览器访问 `http://localhost:8080`。

### 配置

在页面顶部的输入框中粘贴你的 Agent API Key，点击「切换」即可加载数据。

API Key 可从策场平台的 Agent 管理页面获取。

---

## 项目结构

```
ForSignal/
├── dashboard.html        # 交易可视化面板（前端）
├── server.py             # HTTP 服务器 / API 代理
└── README.md             # 本文件
```

### 核心文件说明

| 文件 | 说明 |
|---|---|
| `dashboard.html` | 单页前端应用，使用 Chart.js 绘制图表，纯浏览器端运行 |
| `server.py` | Python HTTP 服务器，提供静态文件服务并代理 API 请求至 `signal.coze.com` |
| `strategy_summary.md` | 个人交易策略学习笔记，包含技术指标、仓位管理、止损止盈规则等 |

---

## 使用说明

### API Key 管理

- 输入 API Key → 点击「切换」即可查看对应 Agent 的完整数据
- 点击「+ 加入管理者库」将当前 Agent 保存到本地对比列表
- 管理者库支持多个 Agent 同时对比，按收益率排序

### 自动刷新

面板每 30 秒自动刷新数据。也可随时点击右上角刷新按钮手动刷新。

### 管理者库

管理者库保存在浏览器 `localStorage` 中，切换浏览器或清除缓存后需要重新添加。

---

## 技术栈

- **前端**: 原生 HTML/CSS/JavaScript, Chart.js
- **后端**: Python 标准库 (`http.server`)
- **API**: 策场 Signal Arena REST API (`signal.coze.com`)

无外部依赖，Python 标准库即可运行。

---

## 免责声明

本项目为个人学习和研究用途。所有数据来自策场 Signal Arena 平台的模拟交易，不构成任何投资建议。
