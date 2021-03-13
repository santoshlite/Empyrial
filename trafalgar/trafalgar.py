#python librairies
# Data manipulation
import numpy as np
import pandas as pd

# Plotting
import matplotlib.pyplot as plt
import seaborn
import matplotlib.mlab as mlab
# Statistical calculation
from scipy.stats import norm
# Tabular data output
from tabulate import tabulate
from pandas_datareader import data as web
from tabulate import tabulate
from datetime import datetime
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm
from statsmodels import regression
plt.style.use('fivethirtyeight')

def graph_close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

def graph_open(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Open']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Open Price from "+start_date + " to "+ end_date)

def graph_volume(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Volume']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

def graph_adj_close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

def close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  return df

def open(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Open']
  df = pd.DataFrame(df)
  return df

def adj_close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  return df

def volume(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Volume']
  df = pd.DataFrame(df)
  return df

def returns(stocks, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  return returns
  
def returns_graph(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  plt.figure(figsize=(20,10))
  plt.plot(returns.index, returns['Close'])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(stock + " Adj Revenues from "+start_date + " to "+ end_date)

def covariance(stocks, start_date, end_date, days):
  df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )['Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  cov_matrix_annual = returns.cov()*days
  return cov_matrix_annual

def ohlcv(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date )
  df = pd.DataFrame(df)
  df = df.drop(['Adj Close'], axis=1)
  return df

def cum_returns_graph(stocks, wts, start_date, end_date):

  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']
  ret_data = price_data.pct_change()[1:]
  weighted_returns = (wts * ret_data)
  port_ret = weighted_returns.sum(axis=1)
  cumulative_ret = (port_ret + 1).cumprod()
  fig = plt.figure(figsize=(20,10))
  ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
  ax1.plot(cumulative_ret)
  ax1.set_xlabel('Date')
  ax1.set_ylabel("Cumulative Returns")
  ax1.set_title("Portfolio Cumulative Returns")
  plt.show();

def cum_returns(stocks, wts, start_date, end_date):
  
  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']
  ret_data = price_data.pct_change()[1:]
  weighted_returns = (wts * ret_data)
  port_ret = weighted_returns.sum(axis=1)
  cumulative_ret = (port_ret + 1).cumprod()
  return cumulative_ret

def annual_volatility(stocks, wts, start_date, end_date):

  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']

  ret_data = price_data.pct_change()[1:]
  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret = (port_ret + 1).cumprod()
  annual_std = np.std(port_ret) * np.sqrt(252)
  print("Volatility (in %):")
  return annual_std*100

def sharpe_ratio(stocks, wts, start_date, end_date):

  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']

  ret_data = price_data.pct_change()[1:]
  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret = (port_ret + 1).cumprod()
  geometric_port_return = np.prod(port_ret + 1) ** (252/port_ret.shape[0]) - 1
  annual_std = np.std(port_ret) * np.sqrt(252)
  port_sharpe_ratio = geometric_port_return / annual_std
  print("Sharpe ratio :")
  return port_sharpe_ratio

def returns_benchmark(stocks, wts, benchmark, start_date, end_date):
  yf.pdr_override()

  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']

  df2 = web.get_data_yahoo(benchmark, start=start_date, end= end_date)

  ret_data = price_data.pct_change()[1:]
  return_df2 = df2.Close.pct_change()[1:]

  port_ret = (ret_data * wts).sum(axis = 1)

  plt.figure(figsize=(20,10))
  port_ret.plot()
  return_df2.plot()
  plt.ylabel("Daily return comparison")
  plt.show()

def cum_returns_benchmark(stocks, wts, benchmark, start_date, end_date):
  yf.pdr_override()

  price_data = web.get_data_yahoo(stocks,
                                start = start_date,
                                end = end_date)
  price_data = price_data['Adj Close']

  df2 = web.get_data_yahoo(benchmark, start=start_date, end= end_date)

  ret_data = price_data.pct_change()[1:]
  return_df2 = df2.Close.pct_change()[1:]

  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret_df1 = (port_ret + 1).cumprod()
  cumulative_ret_df2 = (return_df2 + 1).cumprod()
  print(cumulative_ret_df1)

  plt.figure(figsize=(20,10))
  cumulative_ret_df1.plot()
  cumulative_ret_df2.plot()
  plt.ylabel("Daily return comparison")
  plt.show()

def alpha_beta(stocks, wts, benchmark, start_date, end_date):
  yf.pdr_override()

  price_data = web.get_data_yahoo(stocks,
                                  start = start_date,
                                  end = end_date)
  price_data = price_data['Adj Close']

  df2 = web.get_data_yahoo(benchmark, start= start_date, end= end_date,)

  ret_data = price_data.pct_change()[1:]
  return_df2 = df2.Close.pct_change()[1:]

  port_ret = (ret_data * wts).sum(axis = 1)

  X = return_df2.values
  Y = port_ret.values

  def linreg(x,y):
    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y,x).fit()

    X = x[:,1]
    return model.params[0], model.params[1]

  alpha, beta = linreg(X,Y)
  print("alpha: "+ str(alpha))
  print("beta: "+ str(beta))

def efficient_frontier(stocks, start_date, end_date, iterations):

  stock_raw = web.DataReader(stocks, 'yahoo', "2020-01-01", "2021-01-01")
  stock = stock_raw['Close']
  df = pd.DataFrame(stock)
  port_ret = stock.sum(axis=1)
  log_ret = np.log(stock/stock.shift(1))
  num_runs = iterations

  all_weights = np.zeros((num_runs,len(stock.columns)))
  ret_arr = np.zeros(num_runs)
  vol_arr = np.zeros(num_runs)
  sharpe_arr = np.zeros(num_runs)

  for ind in range(num_runs):

      # Create Random Weights
      weights = np.array(np.random.random(len(stocks)))

      # Rebalance Weights
      weights = weights / np.sum(weights)

      # Save Weights
      all_weights[ind,:] = weights

      # Expected Return
      ret_arr[ind] = np.sum((log_ret.mean() * weights) *252)

      # Expected Variance
      vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))

      # Sharpe Ratio
      sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]

  max_sr_ret = ret_arr[sharpe_arr.argmax()]
  max_sr_vol = vol_arr[sharpe_arr.argmax()]

  print('Return with Maximum SR (in %):')
  print(max_sr_ret*100)
  print('Volality with Maximum SR (in %):')
  print(max_sr_vol*100)
  print('Max Sharpe Ratio:')
  print(sharpe_arr.max())
  print('Optimized allocation (in %):')
  allocation = [i * 100 for i in all_weights[sharpe_arr.argmax(),:] ]
  print(allocation)

  plt.figure(figsize=(14,8))
  plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
  plt.colorbar(label='Sharpe Ratio')
  plt.xlabel('Volatility')
  plt.ylabel('Return')

  # Add red dot for max SR
  plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')

def individual_cum_returns_graph(stocks, start_date, end_date):

  stock_raw = web.DataReader(stocks, 'yahoo', "2020-01-01", "2021-01-01")
  stock = stock_raw['Close']
  port_ret = stock.sum(axis=1)
  stock_normed = stock/stock.iloc[0]
  stock_normed.plot(figsize=(12,8))

def individual_cum_returns(stocks, start_date, end_date):

  stock_raw = web.DataReader(stocks, 'yahoo', "2020-01-01", "2021-01-01")
  stock = stock_raw['Close']
  port_ret = stock.sum(axis=1)
  stock_normed = stock/stock.iloc[0]
  return stock_normed

def individual_mean_daily_return(stocks, start_date, end_date):
  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Close']
  port_ret = stock.sum(axis=1)
  mean_daily_ret = stock.pct_change(1).mean()
  return mean_daily_ret

def portfolio_daily_mean_return(stocks,wts, start_date, end_date):
  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Close']
  port_ret = (stock * wts).sum(axis = 1)
  cum_port = port_ret.pct_change(1)
  mean_return_port = cum_port.mean()
  return mean_return_port

def VaR(stocks, start_date, end_date, confidence_level):
  df = yf.download(stocks, start_date, end_date)
  df = df[['Close']]
  df['returns'] = df.Close.pct_change()

  mean = np.mean(df['returns'])
  std_dev = np.std(df['returns'])

  df['returns'].hist(bins=40, density=True, histtype='stepfilled', alpha=0.5)
  x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
  plt.plot(x,x)
  plt.show()

  VaR = norm.ppf(1-confidence_level/100, mean, std_dev)


  print(tabulate([[confidence_level, VaR]], headers=['Confidence Level', 'Value at Risk']))
