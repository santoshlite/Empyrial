# Trafalgar🃏

Python library to make development of portfolio analysis faster and easier
<img src="https://i.ibb.co/vVdyvfj/Trafalgar.png"/>
# Installation 🔥

To install Trafalgar, you should do:

```
pip install trafalgars
```
(https://pypi.org/project/trafalgars/0.0.2/#description)

For Anaconda setup you can simply run below to install all dependencies with env name trafalgar.

```
conda env create --file environment.yaml  
```

Note : Step 1 and 2 are not always necessary, just make sure the libraries required by trafalgar are installed in you project env.

## Features include 📈

- Get close price, open price, adj close, volume and graphs of these in one line of code!
- Build a efficient frontier programm in 3 lines of code
- Make quantitative analysis on stocks/portfolios (alpha, beta, skew, kurtosis, rolling volatility...)
- Build a  Capital Asset Pricing Model of a portfolio
- Backtest a portfolio, see its stats and compare it to a benchmark 
- many other thnigs...

Here is the code from a google collab, you can use it to follow along with the code: https://colab.research.google.com/drive/1qgFDDQneQP-oddbJVWWApfPKFMnbpj6I?usp=sharing

# Documentation🚀

### Call the library
First, you should do:
```sh
from Trafalgars import *
```

### Graph of the closing price of a stock

```sh
#graph_close(stock, start_date, end_date)
graph_close(["FB"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/Hgk72HR/t-l-chargement.png"/></center>

### Graph of the closing price of multiple stocks 
```sh
graph_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/Rymq0Vb/t-l-chargement.png"/></center>

### Graph the volume 
```sh
#graph_volume(stock, start_date, end_date)

#for one stock
graph_volume(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_volume(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
### Graph the opening price
```sh
#graph_open(stock, start_date, end_date)

#for one stock
graph_open(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_open(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
### Graph the adjusted closing price
```sh
#graph_adj_close(stock, start_date, end_date)

#for one stock
graph_adj_close(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_adj_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```

### Get closing price data (in dataframe format)

```sh
#close(stock, start_date, end_date)
close(["AAPL"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/bHFtrMd/Capture.jpg"/></center>

### Get volume data (in dataframe format)

```sh
#volume(stock, start_date, end_date)
volume(["AAPL"], "2020-01-01", "2021-01-01")
```

### Get opening price data (in dataframe format)
```sh
#open(stock, start_date, end_date)
open(["AAPL"], "2020-01-01", "2021-01-01")
```
### Get adjusted closing price data (in dataframe format)
```sh
#adj_close(stock, start_date, end_date)
adj_close(["AAPL"], "2020-01-01", "2021-01-01")
```

### Covariance between stocks

```sh
#covariance(stocks, start_date, end_date, days) -> usually, days = 252
covariance(["AAPL", "DIS", "AMD"], "2020-01-01", "2021-01-01", 252)
```
<center><img src="https://i.ibb.co/CHR9Z33/Capture.jpg"/></center>

### Correlation between stocks

```sh
#correlation(stocks, start_date, end_date)
correlation(["AAPL", "AMD", "TSLA", "AMZN", "DIS", "SBUX", "NFLX", "AMZN", "GOOG"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/Fb43bXN/Capture.jpg"/></center>

### Graph correlation between stocks

```sh
#graph_correlation(stocks, start_date, end_date)
graph_correlation(["AAPL", "AMD", "TSLA", "AMZN", "DIS", "SBUX", "NFLX", "AMZN", "GOOG"], "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/992jvDD/t-l-chargement-6.png"/></center>

### Get data from a stock in OHLCV format directly

```sh
#ohlcv(stock, start_date, end_date)
ohlcv("AAPL", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/pjy5MkF/Capture.jpg"/>

### Graph the returns (for each day)

```sh
#graph_returns(stock,wts, start_date, end_date)

#for one stock
graph_returns(["AAPL"],1, "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/9NQcVPf/t-l-chargement-1.png"/></center>

```sh
#for a portfolio
graph_returns(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/vsNyMP8/t-l-chargement-2.png"/></center>

### Get returns data of a stock/portfolio (in a dataframe format)

```sh
#returns(stocks,wts, start_date, end_date)
# sum of wts(weights) should always be equal to 1, it represents the allocation of shares in your portfolio (1 = 100%)

#for one stock
returns(["AAPL"],1, "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/rQw0vSZ/a.jpg"/></center>

```sh
#for a portfolio
returns(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/d6CCQY5/Capture.jpg"/></center>

### Graph the cumulative returns of a stock/portfolio

```sh
#graph_creturns(stock, wts, start_date, end_date)

#for one stock
graph_creturns(["TSLA"], 1, "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/YLw0f79/t-l-chargement-5.png"/></center>

```sh
#for a portfolio
graph_creturns(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/4TNWJvz/t-l-chargement-4.png"/></center>

### Get cumulative returns data of a stock/portfolio (in a dataframe format)
```sh
#creturns(stock, wts, start_date, end_date)

#for one stock
creturns(["TSLA"], 1, "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/fXLnqwQ/l.jpg"/></center>

```sh
#for a portfolio
creturns(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/88F49dB/Capture.jpg"/></center>


### Annual Volatility of a portfolio/stock
```sh
#annual_volatility(stocks, wts, start_date, end_date)

#for one stock
annual_volatility(["TSLA"], 1, "2020-01-01", "2021-01-01")
#for multiple stocks
annual_volatility(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/41fNLMw/Capture.jpg"/></center>

### Sharpe Ratio of a portfolio/stock
```sh
#sharpe_ratio(stocks, wts, start_date, end_date)

#for one stock
sharpe_ratio(["TSLA"], 1, "2020-01-01", "2021-01-01")
#for multiple stocks
sharpe_ratio(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/7Y82t2z/Capture.jpg"/></center>

### Graph the returns of a portfolio/stock to a benchmark
```sh
#graph_rbenchmark(stocks, wts, benchmark, start_date, end_date)
#for a stock
graph_rbenchmark(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/sCyFH64/t-l-chargement-8.png"/></center>

```sh
#for a portfolio
graph_rbenchmark(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/3RGPcT7/t-l-chargement-9.png"/></center>

### Get the data of the returns of a portfolio/stock to a benchmark
```sh
#rbenchmark(stocks, wts, benchmark, start_date, end_date)

#for one stock
rbenchmark(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")
#for a portfolio
rbenchmark(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/LPvVw4t/Capture.jpg"/></center>



### Graph the cumulative returns of a portfolio/stock to a benchmark
```sh
#graph_cbenchmark(stocks, wts, benchmark, start_date, end_date)

#for a stock
graph_cbenchmark(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/QYPV1h2/t-l-chargement-11.png"/></center>

```sh
#for a portfolio
graph_cbenchmark(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/NKT7WdS/t-l-chargement-12.png"/></center>

### Get the data of the cumulative returns of a portfolio/stock to a benchmark
```sh
#cbenchmark(stocks, wts, benchmark, start_date, end_date)

#for a stock
cbenchmark(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")
#for a portfolio
cbenchmark(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```

<center><img src="https://i.ibb.co/LPvVw4t/Capture.jpg"/></center>

### Alpha of a portfolio/stock

```sh
#alpha(stocks, wts, benchmark, start_date, end_date)

#for a stock
alpha(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")

#for a portfolio
alpha(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/GJ35NpK/Capture.jpg"/></center>

### Beta of a portfolio/stock

```sh
#beta(stocks, wts, benchmark, start_date, end_date)

#for one stock
beta(["TSLA"], 1, "SPY", "2020-01-01", "2021-01-01")
#for multiple stocks
beta(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "SPY",  "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/5jLSR25/Capture.jpg"/></center>

### Efficient frontier to optimize allocation of shares in your portfolio

```sh
#efficient_frontier(stocks, start_date, end_date, iterations) -> iterations = 10000 is a good starting point
efficient_frontier(["AAPL", "FB", "MSFT", "AMD", "AIR", "AAL", "NFLX", "SBUX", "GOOG", "BABA"], "2020-01-01", "2021-01-01", 10000)
```
<center><img src="https://i.ibb.co/LtCGCj3/Capture.jpg"/></center>

### Get daily mean return of a stock/portfolio

```sh
#mean_daily_return(stocks,wts, start_date, end_date)

#for one stock
mean_daily_return(["AAPL"], 1, "2020-01-01", "2021-01-01")

#for multiple stocks
mean_daily_return(["AAPL", "AMD", "TSLA"], [0.25, 0.45, 0.3], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/w6w7tf2/Capture.jpg"/></center>

### Value at risk of a stock/portfolio

```sh
#var(value_invested, stocks, wts, alpha, start_date, end_date)

#for one stock
var(10000, ['AAPL'], 1, 0.95, "2020-01-01", "2021-01-01")

#for multiple stocks
var(10000, ['AAPL', 'TSLA', 'AMD'], [0.4, 0.2, 0.4], 0.95, "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/4FQ3HHp/Capture.jpg"/></center>

### Graph closing price of stock smoothly with Kalman Filters

```sh
#graph_kalman(stocks, start_date, end_date, noise_value)
#noise_value = 0.01 is good to get started
graph_kalman("AAPL", "2020-01-01", "2021-01-01", 0.01)
```
<center><img src="https://i.ibb.co/wdQ0KQq/t-l-chargement-13.png"/></center>

### Get the smoothed closing price of a stock with Kalman Filters

```sh
#kalman(stocks, start_date, end_date, noise_value)
kalman("AAPL", "2020-01-01", "2021-01-01", 0.01)
```
<center><img src="https://i.ibb.co/vc6ynJh/Capture.jpg"/></center>

### Get the Capital Asset Pricing Model
```sh
#capm(stocks, wts, start_date, end_date)
stocks = ["AAPL", "AMD", "TSLA", "MSFT"]
wts = [0.3, 0.2, 0.2, 0.3]
capm(stocks, wts, "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/4p9H1cB/Capture.jpg"/></center>

## License

**MIT**


