import pandas as pd


class MACalculator:
    def __init__(self):
        """
        初始化类，不需要 Tushare API token，数据通过外部传入
        """
        pass

    def calculate_ma(self, df, periods=[5, 10, 20]):
        """
        计算指定周期的移动均线 (MA)
        :param df: pandas DataFrame, 股票数据 (必须包含 'close' 列)
        :param periods: list, 包含不同周期的移动均线长度 (默认 [5, 10, 20])
        :return: pandas DataFrame, 带有均线的股票数据
        """
        for period in periods:
            df[f"MA{period}"] = df["close"].rolling(window=period).mean()
        return df

    def get_data_with_ma(self, df, periods=[5, 10, 20]):
        """
        获取带有均线的股票数据
        :param df: pandas DataFrame, 外部传入的股票数据，必须包含 'trade_date' 和 'close' 列
        :param periods: list, 均线的周期 (默认 [5, 10, 20])
        :return: pandas DataFrame, 包含均线和收盘价的股票数据
        """
        df = df[["trade_date", "close"]]  # 确保只保留交易日期和收盘价
        df["trade_date"] = pd.to_datetime(
            df["trade_date"]
        )  # 将日期转换为 datetime 格式
        df = df.sort_values("trade_date")  # 按日期升序排列
        df_with_ma = self.calculate_ma(df, periods)
        return df_with_ma
