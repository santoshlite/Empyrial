# Trafalgar

Python library to make development of portfolio analysis faster and easier
<img src="https://i.ibb.co/vVdyvfj/Trafalgar.png"/>
# Installation 🔥

For the moment, Trafalgar is still in beta development. To install it you should:

1) Download requirements.txt in the folder where you want to execute the trafalgar library
2) Go to your folder directory with the command prompt and write : 
```
pip install -r requirements.txt
```
3) Download trafalgars-0.0.1-py3-none-any.whl in the same folder
4) Go to your folder directory with the command prompt and write : 
```
pip install trafalgars-0.0.1-py3-none-any.whl
```

## Features include 📈

- Get close price, open price, adj close, volume and graphs of these in one line of code!
- Build a efficient frontier programm in 3 lines of code
- Backtest a portfolio, see its stats and compare it to a benchmark 

Here is the code of this article from a google collab, you can use it to follow along with this article: https://colab.research.google.com/drive/1qgFDDQneQP-oddbJVWWApfPKFMnbpj6I?usp=sharing

# Documentation

### Call the library
First, you should do:
```sh
from trafalgar import *
```

### Graph of the closing price of a stock

```sh
#graph_close(stock, start_date, end_date)
graph_close(["FB"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/PQmRL9b/t-l-chargement-6.png"/></center>

### Graph of the closing price of multiple stocks 
```sh
graph_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/1bYRWpv/t-l-chargement-7.png"/></center>

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


### Graph the returns (for each day)

```sh
#returns_graph(stock, start_date, end_date)

#this one only work for one stock
returns_graph("FB", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/4KS98MS/t-l-chargement-8.png"/></center>

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

### Get data from a stock in OHLCV format directly

```sh
#ohlcv(stock, start_date, end_date)
ohlcv("AAPL", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/GtcqJmy/Capture.jpg"/>

### Graph the cumulative returns of a stock/portfolio

```sh
#cum_returns_graph(stocks, weights, start_date, end_date)
cum_returns_graph(["FB", "AAPL", "AMD"], [0.3, 0.4, 0.3],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/Xb30TBZ/t-l-chargement-9.png"/></center>

### Get cumulative returns data of a stock/portfolio (in a dataframe format)
```sh
#cum_returns(stocks, weights, start_date, end_date)
cum_returns(["FB", "AAPL", "AMD"], [0.3, 0.4, 0.3],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/2dWJ11T/Capture.jpg"/></center>

Disclaimer : 
From there, the functions only work for portfolios, not for individual stocks.I'm sorry about that, I'm working on that right now...

### Annual Volatility of a portfolio
```sh
#annual_volatility(stocks, weights, start_date, end_date)
annual_volatility(["FB", "AAPL", "AMD"], [0.3, 0.4, 0.3],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/frNdHdG/Capture.jpg"/></center>

### Sharpe Ratio of a portfolio
```sh
#sharpe_ratio(stocks, weights, start_date, end_date)
sharpe_ratio(["FB", "AAPL", "AMD"], [0.3, 0.4, 0.3],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/vPL5JNZ/Capture.jpg"/></center>

### Compare the returns of a portfolio to a benchmark
```sh
#returns_benchmark(stocks, weights, benchmark, start_date, end_date)
returns_benchmark(["AAPL", "AMD", "MSFT"], [0.3, 0.4, 0.3], "SPY", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/w6q7s1g/t-l-chargement-10.png"/></center>

Blue line : returns of your portfolio
Red line : returns of the benchmark

### Compare the cumulative returns of a portfolio to a benchmark
```sh
#cum_returns_benchmark(stocks, weights, benchmark, start_date, end_date)
cum_returns_benchmark(["AAPL", "AMD", "MSFT"], [0.3, 0.4, 0.3], "SPY", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/NKGThvy/Capture.jpg"/></center>

Blue line : cumulative returns of your portfolio
Red line : cumulative returns of the benchmark

### Alpha and Beta of a portfolio

```sh
#alpha_beta(stocks, weights, benchmark, start_date, end_date)
alpha_beta(["AAPL", "AMD", "MSFT"], [0.3, 0.4, 0.3], "SPY", "2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/nmL4Qym/Capture.jpg"/></center>

### Efficient frontier to optimize allocation of shares in your portfolio

```sh
#efficient_frontier(stocks, start_date, end_date, iterations) -> iterations = 10000 is a good starting point
efficient_frontier(["AAPL", "FB", "TSLA", "BABA"], "2020-01-01", "2021-01-01", 10000)
```
<center><img src="https://i.ibb.co/pyfqgfS/Capture.jpg"/></center>

### Graph individual cumulative returns for your portfolio

```sh
#individual_cum_returns_graph(stocks, start_date, end_date)
individual_cum_returns_graph(["FB", "AAPL", "AMD"],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/B2RHDGf/Capture.jpg"/></center>

### Individual cumulative returns datas for your portfolio (in dataframe format)

```sh
#individual_cum_returns(stocks, start_date, end_date)
individual_cum_returns(["FB", "AAPL", "AMD"],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/MNNJWw1/Capture.jpg"/></center>

### Mean daily return of each stocks in your portfolio

```sh
#individual_mean_daily_return(stocks, start_date, end_date)
individual_mean_daily_return(["FB", "AAPL", "AMD"],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/tm4Tdr0/Capture.jpg"/></center>

### Portfolio mean daily return
```sh
#portfolio_daily_mean_return(stocks,weights, start_date, end_date)
portfolio_daily_mean_return(["FB", "AAPL", "AMD"],"2020-01-01", "2021-01-01")
```
<center><img src="https://i.ibb.co/Qfj4vH1/Capture.jpg"/></center>

### Value at Risk of a stock (still in development)
```sh
#VaR(stock, start_date, end_date, confidence_level)
VaR("FB","2020-01-01", "2021-01-01", 98)
```
<center><img src="https://i.ibb.co/hfQqP3z/Capture.jpg"/></center>

## License

**MIT**

