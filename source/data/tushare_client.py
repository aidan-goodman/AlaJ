from source.utils import config_loader as conf
from source.utils import logger
import tushare as ts
import pandas as pd

log = logger.Logger(name=__name__, save=True)


class TushareClient:
    def __init__(self, token: str = ""):
        """初始化 Tushare API 客户端。

        :param token: Tushare API 的 token。
        """
        config = conf.ConfigLoader()
        self.api_token = token or config.get("tushare.token")
        if not self.api_token:
            raise ValueError("Tushare token is required.")
        ts.set_token(self.api_token)
        self.api_instance = ts.pro_api()

    def _fetch_data(self, api_method, **params) -> pd.DataFrame:
        """通用数据获取方法。

        :param api_method: Tushare API 的方法。
        :param params: API 的参数。
        :return: 返回的数据 DataFrame。
        """
        try:
            log.info(f"Fetching data with parameters: {params}")
            data = api_method(**params)
            log.info(f"Data fetched, rows: {len(data)}")
            return data
        except Exception as e:
            log.error(f"Error fetching data with parameters {params}: {e}")
            return pd.DataFrame()

    def get_daily_data(
        self, stock_code: str, start_date: str, end_date: str
    ) -> pd.DataFrame:
        """获取 A 股日线数据。

        :param stock_code: 股票代码，例如 '600519.SH'。
        :param start_date: 开始日期，格式为 'YYYYMMDD'。
        :param end_date: 结束日期，格式为 'YYYYMMDD'。
        :return: 包含股票日线数据的 DataFrame。
        """
        return self._fetch_data(
            self.api_instance.daily,
            ts_code=stock_code,
            start_date=start_date,
            end_date=end_date,
        )

    def get_minute_data(
        self, stock_code: str, start_date: str, end_date: str, frequency: str = "5min"
    ) -> pd.DataFrame:
        """获取股票的分钟线数据。

        :param stock_code: 股票代码，例如 '600519.SH'。
        :param start_date: 开始日期，格式为 'YYYYMMDD'。
        :param end_date: 结束日期，格式为 'YYYYMMDD'。
        :param frequency: 时间间隔，可选值为 '1min', '5min', '15min', '30min', '60min'。
        :return: 包含股票分钟线数据的 DataFrame。
        """
        return self._fetch_data(
            ts.pro_bar,
            ts_code=stock_code,
            freq=frequency,
            start_date=start_date,
            end_date=end_date,
        )
