from empyrial import *

tickers = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"]

portfolio = Engine(
      start_date = "2019-01-01",
      portfolio = tickers,
      optimizer = "EF", 
      rebalance = "1y"
)

test = portfolio.rebalance

empyrial(portfolio, rebalance = True)