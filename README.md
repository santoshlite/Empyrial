# By Investors, for Investors

<div align="center">
<img src="https://i.ibb.co/vVdyvfj/Trafalgar.png"/>

![Downloads](https://static.pepy.tech/personalized-badge/trafalgar-py?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Users)
![](https://img.shields.io/badge/license-MIT-blue)
![](https://img.shields.io/badge/flow%20level-A++-brightgreen)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/views-+11k-red)
![](https://img.shields.io/badge/activity-8.8/10-yellow)
![](https://camo.githubusercontent.com/97d4586afa582b2dcec2fa8ed7c84d02977a21c2dd1578ade6d48ed82296eb10/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e7376673f763d313033)

<br>
Featured on
<br><br>

<img align="left" src="https://www.libhunt.com/assets/logo/logo-og-12f445719d17ec887b4f67216c07a38850ebfbc93ed81fa8b3bbb338d63a7adb.png" width="200"/>
<img align="left" src="https://cdn-images-1.medium.com/max/1200/1*NHYVDHC_WbdaUicoYyJFrA.png" width="100"/>
<img align="left" src="https://cdn-images-1.medium.com/max/1200/1*yAqDFIFA5F_NXalOJKz4TA.png" width="100"/>
<img align="left"src="https://pychina.org/img/pycon.png" width="100"/><br>
<img align="left"src="https://i.ibb.co/r4ZzyLQ/Capture.jpg" width="300"/>
</div>



<br><br><br><br><br><br>

# Installation 🔥

To install Trafalgar, you should do:

```
pip install trafalgar.py
```
(https://pypi.org/project/trafalgar.py/)


## Features include 📈

- Get close price, open price, adj close, volume and graphs of these in one line of code!
- Build an efficient frontier programm in 3 lines of code
- Make quantitative analysis on stocks/portfolios (alpha, beta, skew, kurtosis, rolling volatility...)
- Build a  Capital Asset Pricing Model of a portfolio
- Backtest a portfolio, see its stats and compare it to a benchmark 
- many other things...

Here is the code from a google collab, you can use it to follow along with the code: https://colab.research.google.com/drive/13i049m2kIHK3WdklOZXrhqF1jw93kEBb?usp=sharing

## Credits ✌️

This library would not exist without the existence of Github and :

- the contributors @rslopes, @rakeshbhat9, @Haizzz and @george-adams1
- Quantopian and their incredible lectures (https://gist.github.com/ih2502mk/50d8f7feb614c8676383431b056f4291)
- the authors of codingfinance.com
- Quantconnect
- @mrmushfiq and his repo https://github.com/mrmushfiq/python_meets_finance

# Documentation🚀

### Call the library
First, you should do:
```sh
import trafalgar
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

<center><img src="https://i.ibb.co/wYRR4nJ/Capture.jpg"/></center>

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

### Cointegration
```sh
#cointegration(stock1, stock2, start_date, end_date)
cointegration("GOOG", "MSFT", "2012-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/CbCXVb7/Capture.jpg"/></center>

### Returns Cointegration
```sh
#return_cointegration(stock1, stock2, start_date, end_date)
return_cointegration("GOOG", "MSFT", "2012-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/XYG5wGH/Capture.jpg"/></center>

### Stationarity
```sh
#stationarity(stock, start_date, end_date)
stationarity("GOOG", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/2MPh0S4/Capture.jpg"/></center>

### Returns Stationarity
```sh
#return_stationarity(stock, start_date, end_date)
return_stationarity("GOOG", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/V2MPpqy/Capture.jpg"/></center>

### Graph rolling volatility
```sh
#graph_rvolatility(stock, wts, start_date, end_date, window_time)
#for a stock
graph_rvolatility(["TSLA"], 1, "2019-01-01", "2021-01-01", 180)

#for a portfolio
graph_rvolatility(["AAPL", "AMD", "TSLA"], [0.45, 0.45, 0.1], "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/d6QkDb3/Capture.jpg"/></center>

### Get rolling volatility data
```sh
#rvolatility(stock, wts, start_date, end_date, window_time)
#for a stock
rvolatility(["TSLA"], 1, "2019-01-01", "2021-01-01", 180)

#for a portfolio
rvolatility(["AAPL", "AMD", "TSLA"], [0.45, 0.45, 0.1], "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/T2W0Y3T/Capture.jpg"/></center>

### Graph rolling beta
```sh
#graph_rbeta(stock,wts, benchmark, start_date, end_date, window_time)

#for a stock
graph_rbeta(["TSLA"], 1, "SPY", "2019-01-01", "2021-01-01", 180)

#for a portfolio
graph_rbeta(["AAPL", "AMD", "GOOG"], [0.45, 0.45, 0.1], "SPY", "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/k2ZFRNH/Capture.jpg"/></center>

### Get rolling beta data
```sh
#rbeta(stock,wts, benchmark, start_date, end_date, window_time)

#for a stock
rbeta(["TSLA"], 1, "SPY", "2019-01-01", "2021-01-01", 180)

#for a portfolio
rbeta(["AAPL", "AMD", "GOOG"], [0.45, 0.45, 0.1], "SPY", "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/QQSWPP3/Capture.jpg"/></center>

### Graph rolling alpha
```sh
#graph_ralpha(stock,wts, benchmark, start_date, end_date, window_time)

#for a stock
graph_ralpha(["TSLA"], 1, "SPY", "2019-01-01", "2021-01-01", 180)

#for a portfolio
graph_ralpha(["AAPL", "AMD", "GOOG"], [0.45, 0.45, 0.1], "SPY", "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/BN7ZHQq/Capture.jpg"/></center>

### Get rolling alpha data
```sh
#ralpha(stock,wts, benchmark, start_date, end_date, window_time)

#for a stock
ralpha(["TSLA"], 1, "SPY", "2019-01-01", "2021-01-01", 180)

#for a portfolio
ralpha(["AAPL", "AMD", "GOOG"], [0.45, 0.45, 0.1], "SPY", "2019-01-01", "2021-01-01", 180)
```
<center><img src="https://i.ibb.co/VJTgXs2/Capture.jpg"/></center>

### Get implied volatility
```sh
#implied_vol(option_type, option_price, stock price, strike price, risk-free rate, the time to expiration, continuous dividend rate)
#option type : "c" (call option) or "p"(put option)

implied_vol('c', 0.3, 3, 3, 0.032, 30.0/365, 0.01)
```
<center><img src="https://i.ibb.co/gS19VTM/Capture.jpg"/></center>

### Backtest your portfolio

```sh
#backtest(stocks, wts, benchmark, start_date, end_date)
stocks = ["GOOG", "AMZN", "FB", "AAPL"]
wts = [0.25, 0.25, 0.25, 0.25]
backtest(stocks, wts, "SPY", "2019-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/PmRR2gC/Capture.jpg"/></center>
<center><img src="https://i.ibb.co/VwBNf17/t-l-chargement-14.png"/></center>
<center><img src="https://i.ibb.co/mvvGwCf/Capture.jpg"/></center>
<center><img src="https://i.ibb.co/VN83w2z/t-l-chargement-15.png"/></center>
<center><img src="https://i.ibb.co/Bfc1xKG/t-l-chargement-16.png"/></center>
<center><img src="https://i.ibb.co/R7cj5Hd/t-l-chargement-17.png"/></center>
<center><img src="https://i.ibb.co/dWZq4wg/t-l-chargement-18.png"/></center>
<center><img src="https://i.ibb.co/Df2FqWC/Capture.jpg"/></center>
<center><img src="https://i.ibb.co/tY5rjhx/Capture.jpg"/></center>

## License

**MIT**

