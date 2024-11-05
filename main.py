from source.data import tushare_client
from source.data import ma_calculator

if __name__ == "__main__":

    client = tushare_client.TushareClient()
    dailys = client.get_daily_data("600519.SH", "20241001", "20241031")

    calculator = ma_calculator.MACalculator()
    dailys_with_ma = calculator.get_data_with_ma(dailys)
    print(dailys_with_ma)
