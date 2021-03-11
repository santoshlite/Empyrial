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



## Documentation

Displaying the graph of the close price of a stock in a given time

```sh
#graph_close(stock, start_date, end_date)
#get the graph of a stock
graph_close(["FB"], "2020-01-01", "2021-01-01")
```

```sh
#get the graph of multiple stocks
graph_close(["FB", "AAPL", "TSLA"], "2020-01-01", "2021-01-01")
```

## License

**MIT**
