#python librairies
# Data manipulation
import numpy as np
import pandas as pd
import statsmodels
# Plotting
import matplotlib.pyplot as plt
import seaborn 
# Statistical calculation
from scipy.stats import norm
# Tabular data output
from pandas_datareader import data as web
from datetime import datetime
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint, adfuller
from statsmodels import regression
plt.style.use('fivethirtyeight')

# ------------------------------------------------------------------------------------------

def graph_close(stock, start_date, end_date):

  """
  Source and plot Close prices from yahoo for any given stock/s & period

  Parameters
  ----------
  stock : str,list
      Either a single stock ticker or list of tickers.
  start_date : str
      Date in yyyy-mm-dd format
  end_date : str
      Date in yyyy-mm-dd format
  """
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

# ------------------------------------------------------------------------------------------

def graph_open(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Open']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Open Price from "+start_date + " to "+ end_date)

# ------------------------------------------------------------------------------------------

def graph_volume(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Volume']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

# ------------------------------------------------------------------------------------------

def graph_adj_close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  plt.figure(figsize=(20,10))
  plt.plot(df.index, df[stock])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(" Close Price from "+start_date + " to "+ end_date)

# ------------------------------------------------------------------------------------------

def close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Close']
  df = pd.DataFrame(df)
  return df

# ------------------------------------------------------------------------------------------

def open(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Open']
  df = pd.DataFrame(df)
  return df

# ------------------------------------------------------------------------------------------

def adj_close(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  return df

# ------------------------------------------------------------------------------------------

def volume(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Volume']
  df = pd.DataFrame(df)
  return df

# ------------------------------------------------------------------------------------------

def returns(stocks, start_date, end_date):
  df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  return returns

# ------------------------------------------------------------------------------------------

def returns_graph(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  plt.figure(figsize=(20,10))
  plt.plot(returns.index, returns['Close'])
  plt.xlabel("Date")
  plt.ylabel("$ price")
  plt.title(stock + " Adj Revenues from "+start_date + " to "+ end_date)

# ------------------------------------------------------------------------------------------

def covariance(stocks, start_date, end_date, days):
  df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )['Adj Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  cov_matrix_annual = returns.cov()*days
  return cov_matrix_annual


# ------------------------------------------------------------------------------------------

def correlation_graph(stocks, start_date, end_date):
    corr_mat = correlation(stocks, start_date, end_date)
    seaborn.heatmap(corr_mat, annot=True)
    plt.show()

# ------------------------------------------------------------------------------------------

def ohlcv(stock, start_date, end_date):
  df = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date )
  df = pd.DataFrame(df)
  df = df.drop(['Adj Close'], axis=1)
  df = df[["Open", "High", "Low", "Close", "Volume"]]
  return df

# ------------------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------------------

def annual_volatility(stocks, wts, start_date, end_date):

  price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
  price_data = price_data['Adj Close']

  ret_data = price_data.pct_change()[1:]
  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret = (port_ret + 1).cumprod()
  annual_std = np.std(port_ret) * np.sqrt(252)
  return annual_std*100

# ------------------------------------------------------------------------------------------

def sharpe_ratio(stocks, wts, start_date, end_date):

  price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
  price_data = price_data['Adj Close']

  ret_data = price_data.pct_change()[1:]
  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret = (port_ret + 1).cumprod()
  geometric_port_return = np.prod(port_ret + 1) ** (252/port_ret.shape[0]) - 1
  annual_std = np.std(port_ret) * np.sqrt(252)
  port_sharpe_ratio = geometric_port_return / annual_std
  return 1+port_sharpe_ratio

# ------------------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------------------

def graph_cum_returns_benchmark(stocks, wts, benchmark, start_date, end_date):
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

# ------------------------------------------------------------------------------------------
def cum_returns_benchmark(stocks, wts, benchmark, start_date, end_date):
  yf.pdr_override()

  price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
  price_data = price_data['Adj Close']

  df2 = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date )

  ret_data = price_data.pct_change()[1:]
  return_df2 = df2.Close.pct_change()[1:]

  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret_df1 = (port_ret + 1).cumprod()
  cumulative_ret_df2 = (return_df2 + 1).cumprod()

  df1 = pd.DataFrame(cumulative_ret_df1)
  df2 = pd.DataFrame(cumulative_ret_df2)
  df = pd.concat([df1,df2], axis=1)
  df = pd.DataFrame(df)
  df.columns = ['portfolio', 'benchmark']
  return df


# ------------------------------------------------------------------------------------------

def efficient_frontier(stocks, start_date, end_date, iterations):

  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
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
  plt.show()

# ------------------------------------------------------------------------------------------

def individual_cum_returns_graph(stocks, start_date, end_date):

  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = stock.sum(axis=1)
  stock_normed = stock/stock.iloc[0]
  stock_normed.plot(figsize=(12,8))

# ------------------------------------------------------------------------------------------

def individual_cum_returns(stocks, start_date, end_date):

  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = stock.sum(axis=1)
  stock_normed = stock/stock.iloc[0]
  return stock_normed

# ------------------------------------------------------------------------------------------

def individual_mean_daily_return(stocks, start_date, end_date):
  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = stock.sum(axis=1)
  mean_daily_ret = stock.pct_change(1).mean()
  return mean_daily_ret

# ------------------------------------------------------------------------------------------

def portfolio_daily_mean_return(stocks,wts, start_date, end_date):
  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = (stock * wts).sum(axis = 1)
  cum_port = port_ret.pct_change(1)
  mean_return_port = cum_port.mean()
  return mean_return_port

# ------------------------------------------------------------------------------------------

def var(value_invested, stocks, wts, alpha, start_date, end_date):
  price_data = web.DataReader(stocks, 'yahoo', start_date, end_date)
  price_data = price_data['Adj Close']
  ret_data = price_data.pct_change()[1:]
  weighted_returns = (wts * ret_data)
  port_ret = weighted_returns.sum(axis=1)
  #df = pd.concat([return_fb, return_aapl], axis=1)
  port_ret = port_ret.fillna(0.0)

    # Compute the correct percentile loss and multiply by value invested
  return np.percentile(port_ret, 100 * (1-alpha)) * value_invested

# ------------------------------------------------------------------------------------------
def alpha(stock, benchmark, start_date, end_date):
  asset = web.DataReader('TSLA', data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  benchmark = web.DataReader('SPY', data_source='yahoo', start = start_date, end= end_date)['Adj Close']

  r_a = asset.pct_change()[1:]
  r_b = benchmark.pct_change()[1:]
  X = r_b.values
  Y = r_a.values
  def linreg(x,y):
      x = sm.add_constant(x)
      model = regression.linear_model.OLS(y,x).fit()
 
      x = x[:, 1]
      return model.params[0], model.params[1]

  alpha, beta = linreg(X,Y)
  print(alpha)
  #--------------------------------------------------------------------------------------------
def beta(stock, benchmark, start_date, end_date):
  asset = web.DataReader('TSLA', data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  benchmark = web.DataReader('SPY', data_source='yahoo', start = start_date, end= end_date)['Adj Close']

  r_a = asset.pct_change()[1:]
  r_b = benchmark.pct_change()[1:]

  X = r_b.values 
  Y = r_a.values

  def linreg(x,y):

      x = sm.add_constant(x)
      model = regression.linear_model.OLS(y,x).fit()
      x = x[:, 1]
      return model.params[0], model.params[1]

  alpha, beta = linreg(X,Y)
  print(beta)
  #-------------------------------------------------------------------------------------------------
def correlation(stocks, start_date, end_date):
  df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )['Adj Close']
  df = pd.DataFrame(df)
  returns = df.pct_change()
  corr_matrix = returns.corr('pearson')
  return corr_matrix

#-----------------------------------------------------------------------------------------------------
def graph_kalman(stocks, start, end):
  x = web.DataReader(stocks, data_source='yahoo', start = start, end= end)['Adj Close']

  # Construct a Kalman filter
  kf = KalmanFilter(transition_matrices = [1],
                    observation_matrices = [1],
                    initial_state_mean = 0,
                    initial_state_covariance = 1,
                    observation_covariance=1,
                    transition_covariance=.01)

  # Use the observed values of the price to get a rolling mean
  state_means, _ = kf.filter(x.values)
  state_means = pd.Series(state_means.flatten(), index=x.index)
  x = pd.DataFrame(x)

  plt.plot(state_means)
  plt.plot(x)

  plt.title('Kalman filter estimate of average')
  plt.legend(['Kalman Estimate', 'X'])
  plt.xlabel('Day')
  plt.ylabel('Price');
#------------------------------------------------------------------------------------------------------------

def kalman(stocks, start_date, end_date):
  x = web.DataReader(stocks, data_source='yahoo', start = start, end= end)['Adj Close']

  # Construct a Kalman filter
  kf = KalmanFilter(transition_matrices = [1],
                    observation_matrices = [1],
                    initial_state_mean = 0,
                    initial_state_covariance = 1,
                    observation_covariance=1,
                    transition_covariance=.01)

  # Use the observed values of the price to get a rolling mean
  state_means, _ = kf.filter(x.values)
  state_means = pd.Series(state_means.flatten(), index=x.index)
  state_means = pd.DataFrame(state_means)
  return state_means

#---------------------------------------------------------------------------------------------------------------
def capm(stocks, wts, start_date, end_date):

  R = portfolio_ret(stocks, wts, start_date, end_date)
  R_F = web.DataReader('BIL', data_source='yahoo', start = start_date, end = end_date)['Adj Close'].pct_change()[1:]
  
  # find it's beta against market
  M = web.DataReader('SPY', data_source='yahoo', start = start_date, end = end_date)['Adj Close'].pct_change()[1:]

  results = regression.linear_model.OLS(R-R_F, sm.add_constant(M)).fit()
  beta = results.params[1]
  return results.summary()
  #--------------------------------------------------------------------------------------------------------------
  def cointegration(stock1, stock2, start_date, end_date):
  X1 = web.DataReader("MSFT", data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  X2 = web.DataReader("GOOG", data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  X1.name = str(stock1)
  X2.name = str(stock2)
  def check_for_stationarity(X, cutoff=0.01):
    # H_0 in adfuller is unit root exists (non-stationary)
    # We must observe significant p-value to convince ourselves that the series is stationary
    pvalue = adfuller(X)[1]
    if pvalue < cutoff:
        print('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely stationary.')
        return True
    else:
        print('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely non-stationary.')
        return False
  Z = X2 - X1
  Z.name = 'Z'

  plt.plot(Z)
  plt.xlabel('Time')
  plt.ylabel('Series Value')
  plt.legend(['Z']);

  check_for_stationarity(Z);
  #------------------------------------------------------------------------------------------------------------------
  
  

