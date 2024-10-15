import backtrader as bt
import pandas as pd


class BackTestEngine:
    def __init__(self):
        self.data = None  # 初始化数据为 None

    def set_data(self, dataframe: pd.DataFrame):
        # 检查输入的 DataFrame 是否包含所需的列
        if not all(
            col in dataframe.columns
            for col in ["trade_date", "open", "high", "low", "close", "vol"]
        ):
            raise ValueError("数据框缺少必需的列。")

        # 复制 DataFrame，避免修改原数据
        dataframe = dataframe.copy()

        # 将 'trade_date' 转换为 datetime 格式，并设置为索引
        dataframe["datetime"] = pd.to_datetime(dataframe["trade_date"])
        dataframe.set_index("datetime", inplace=True)

        # 将 'vol' 列重命名为 'volume'，以便 Backtrader 识别
        dataframe = dataframe[["open", "high", "low", "close", "vol"]].rename(
            columns={"vol": "volume"}
        )

        # 设置 Backtrader 数据源
        self.data = bt.feeds.PandasData(dataname=dataframe)

    def run_test(self, cerebro: bt.Cerebro, style: str = "candlestick"):
        # 检查是否已经设置了数据源
        if self.data is None:
            raise ValueError("数据未设置。请先调用 set_data() 方法。")

        # 添加数据源到 cerebro
        cerebro.adddata(self.data)

        # 获取初始资金
        start_value = cerebro.broker.getvalue()
        print(f"初始资金: {start_value:.2f}")

        # 运行回测
        cerebro.run()

        # 获取回测结束后的资金
        end_value = cerebro.broker.getvalue()
        print(f"回测结束资金: {end_value:.2f}")

        # 绘制回测结果图表，使用指定的样式
        cerebro.plot(style=style)
