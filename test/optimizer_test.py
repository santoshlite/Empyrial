from empyrial import*

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"]
)

#for efficient frontier
optimizer(portfolio, "EF")

#for hierarchical risk parity
optimizer(portfolio, "HRP")

#for mean variance
optimizer(portfolio, "MV", vol_max=0.15)
