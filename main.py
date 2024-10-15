from source.data.tushare_client import TushareClient
from source.backtest.backtest_engine import BackTestEngine
from source.strategies.strategy_base import OpenHighCloseLowStrategy
import backtrader as bt

if __name__ == "__main__":
    ts_client = TushareClient()
    df = ts_client.get_daily_data("002709.SZ", "20240101", "20240930")

    cerebro = bt.Cerebro()
    cerebro.addstrategy(OpenHighCloseLowStrategy)
    cerebro.broker.setcash(10000)
    cerebro.broker.setcommission(commission=0.001)

    back = BackTestEngine()
    back.set_data(df)

    back.run_test(cerebro)
