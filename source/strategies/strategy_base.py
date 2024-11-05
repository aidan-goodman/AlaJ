import backtrader as bt


class OpenHighCloseLowStrategy(bt.Strategy):

    def next(self):
        if not self.position:
            if self.data.open[0] > self.data.close[-1]:  # 今日开盘价 > 昨日收盘价，买入
                self.buy()
        elif self.data.open[0] <= self.data.close[-1]:  # 今日开盘价 <= 昨日收盘价，卖出
            self.sell()
