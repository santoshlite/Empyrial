# Trafalgar

Python library to make development of portfolio analysis faster and easier

# Installation 🔥

For the moment, Trafalgar is still in beta development. To install it you should:

1) Download trafalgars-0.0.1-py3-none-any.whl in the folder you want
2) Go to your folder with the command prompt and write : 
```
pip install trafalgars-0.0.1-py3-none-any.whl
```

## Features include 📈

- Get close price, open price, adj close, volume and graphs of these in one line of code!
- Build a efficient frontier programm in 3 lines of code
- Backtest a portfolio, see its stats and compare it to a benchmark 



# Documentation

### Graph of the closing price of a stock

```sh
#graph_close(stock, start_date, end_date)
graph_close(["FB"], "2020-01-01", "2021-01-01")
```
<img src="https://i.ibb.co/PQmRL9b/t-l-chargement-6.png"/>

### Graph of the closing price of multiple stocks 
```sh
graph_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
<img src="https://i.ibb.co/1bYRWpv/t-l-chargement-7.png"/>

### Graph the volume 
```sh
#for one stock
graph_volume(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_volume(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
### Graph the opening price
```sh
#for one stock
graph_open(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_open(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```
### Graph the adjourned closing price
```sh
#for one stock
graph_adj_close(["FB"], "2020-01-01", "2021-01-01")

#for multiple stocks
graph_adj_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```


### Graph the returns (for each day)

```sh
#this one only work for one stock
returns_graph(["FB"], "2020-01-01", "2021-01-01")
```
<img src="https://i.ibb.co/4KS98MS/t-l-chargement-8.png"/>

### Get closing price data (in dataframe format)

```sh
close(["FB"], "2020-01-01", "2021-01-01")
```
<img src="https://i.ibb.co/bHFtrMd/Capture.jpg"/>

### Get volume data (in dataframe format)

```sh
volume(["FB"], "2020-01-01", "2021-01-01")
```

### Get opening price data (in dataframe format)
```sh
open(["FB"], "2020-01-01", "2021-01-01")
```
### Get adjourned closing price data (in dataframe format)
```sh
adj_close(["FB"], "2020-01-01", "2021-01-01")
```



## License

**MIT**

