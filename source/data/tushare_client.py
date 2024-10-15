from source.utils import config_loader as conf
import tushare
import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class TushareClient:
    def __init__(self, token: str = ""):
        """
        初始化 Tushare API 客户端
        :param token: Tushare API token
        """
        config = conf.ConfigLoader()
        self.token = token or config.get("tushare.token")
        if not self.token:
            raise ValueError("Tushare token is required.")
        tushare.set_token(self.token)
        self.pro = tushare.pro_api()

    def fetch_data(self, func, **kwargs) -> pd.DataFrame:
        """
        通用数据获取方法
        :param func: Tushare API 方法
        :param kwargs: API 参数
        :return: 返回的数据 DataFrame
        """
        try:
            logger.info(f"Fetching data with parameters: {kwargs}")
            data = func(**kwargs)
            logger.info(f"Data fetched, rows: {len(data)}")
            return data
        except Exception as e:
            logger.error(f"Error fetching data with parameters {kwargs}: {e}")
            return pd.DataFrame()

    def get_daily_data(
        self, ts_code: str, start_date: str, end_date: str
    ) -> pd.DataFrame:
        """
        获取 A 股日线数据
        :param ts_code: 股票代码 (如 '600519.SH')
        :param start_date: 开始日期 (YYYYMMDD)
        :param end_date: 结束日期 (YYYYMMDD)
        :return: 股票日线数据的 DataFrame
        """
        return self.fetch_data(
            self.pro.daily, ts_code=ts_code, start_date=start_date, end_date=end_date
        )

    def get_minute_data(
        self, ts_code: str, start_date: str, end_date: str, freq: str = "5min"
    ) -> pd.DataFrame:
        """
        获取股票的分钟线数据
        :param ts_code: 股票代码 (如 '600519.SH')
        :param start_date: 开始日期 (YYYYMMDD)
        :param end_date: 结束日期 (YYYYMMDD)
        :param freq: 时间间隔 ('1min', '5min', '15min', '30min', '60min')
        :return: 股票分钟线数据的 DataFrame
        """
        return self.fetch_data(
            tushare.pro_bar,
            ts_code=ts_code,
            freq=freq,
            start_date=start_date,
            end_date=end_date,
        )
