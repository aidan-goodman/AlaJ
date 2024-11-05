# AlaJ

## 模块目录

```
AlaJ/source/
├── data/                   # 数据获取
│   ├── __init__.py
│   ├── tushare_client.py   # 获取行情数据
│   ├── ma_calculator.py    # 均线计算
├── strategies/             # 量化交易策略
│   ├── __init__.py
│   ├── strategy_base.py    # 基础策略类
├── backtest/               # 回测模块
│   ├── __init__.py
│   ├── backtest_engine.py  # 回测引擎，整合策略、数据和结果
├── execution/              # 交易执行模块
│   ├── __init__.py
│   ├── notice.py           # 实盘消息通知
│   ├── order_execution.py  # 下单管理
├── risk_management/        # 风险管理模块
│   ├── __init__.py
│   ├── position_size.py    # 仓位控制
│   ├── stop_loss.py        # 止损策略
├── chart/                  # 图像展示
├── utils/                  # 辅助工具
│   ├── __init__.py
│   ├── config_loader.py    # 配置加载工具
├── main.py                 # 项目的入口文件
└── README.md               # 项目说明文件
```
