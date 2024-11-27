from main import portfolio_analysis, Engine
import pandas as pd

# Define custom data
portfolio_data = pd.DataFrame({
    "AAPL": [145.0, 147.0, 149.0],
    "MSFT": [240.0, 242.0, 245.0],
    "GOOGL": [2700.0, 2725.0, 2750.0],
}, index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]))

benchmark_data = pd.DataFrame({
    "TGT": [420.0, 425.0, 430.0],
}, index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]))


portfolio = Engine(
    start_date="2023-01-01",
    portfolio=["AAPL", "MSFT", "GOOGL"],
    weights=[0.4, 0.3, 0.3],
    data=portfolio_data,
    benchmark=["TGT"],
    benchmark_data=benchmark_data
)

# Fetch benchmark data and analyze
portfolio.fetch_benchmark_data()
portfolio_analysis(portfolio)

