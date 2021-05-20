import numpy as np
import pandas as pd
import statsmodels
import matplotlib.pyplot as plt
import seaborn 
from scipy.stats import norm
from pandas_datareader import data as web
import datetime as dt
from dateutil.relativedelta import relativedelta
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint, adfuller
from statsmodels import regression
from sklearn.linear_model import LinearRegression
from pykalman import KalmanFilter

# ------------------------------------------------------------------------------------------

years = {
    '1mo' : math.ceil(trading_year_days/12),
    '3mo' : math.ceil(trading_year_days/4),
    '6mo' : math.ceil(trading_year_days/2),
    '1y': trading_year_days,
    '2y' : 2*trading_year_days,
    '5y' : 5*trading_year_days,
    '10y' : 10*trading_year_days,
    'max' : len(yf.Ticker(stocks).history(**p)['Close'].pct_change())
  }

today = dt.date.today()

#-------------------------------------------------------------------------------------------
def graph_close(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Close']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  df.plot(figsize=(20,10))

# ------------------------------------------------------------------------------------------
def graph_open(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Open'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Open']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  df.plot(figsize=(20,10))

# ------------------------------------------------------------------------------------------

def graph_volume(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Volume'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Volume']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  df.plot(figsize=(20,10))

# ------------------------------------------------------------------------------------------

def graph_adj_close(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Adj Close'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Adj Close']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  df.plot(figsize=(20,10))

# ------------------------------------------------------------------------------------------

def close(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Close']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  return df

# ------------------------------------------------------------------------------------------

def open(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Open'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Open']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  return df

# ------------------------------------------------------------------------------------------

def adj_close(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Adj Close'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Adj Close']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  return df

# ------------------------------------------------------------------------------------------
def volume(stocks, period="max", trading_year_days=252):
    
  p = {"period": period}
  for stock in stocks:
    years = {  
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Volume'].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)['Volume']
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  return df

# ------------------------------------------------------------------------------------------
def returns(stocks,wts=1, period="max", benchmark= None, plot=True, pricing="Adj Close", trading_year_days=252):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  if len(stocks) > 1:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    if benchmark != None:
      df2 = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
      return_df2 = df2.pct_change()[1:]
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      ret_data = df.pct_change()[1:]
      port_ret = (ret_data * wts).sum(axis = 1)
      ret_data['Portfolio returns'] = port_ret
      ret_data['Benchmark'] = return_df2
      ret_data = pd.DataFrame(ret_data)
    else:     
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      ret_data = df.pct_change()[1:]
      port_ret = (ret_data * wts).sum(axis = 1)
      ret_data['Portfolio returns'] = port_ret
      ret_data = pd.DataFrame(ret_data)

    if plot==True:
      ret_data.plot(figsize=(20,10))
      plt.xlabel('Date') 
      plt.ylabel('Returns') 
      plt.title(period + 'Portfolio returns')
    else:
      return ret_data
  else:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    if benchmark != None:
      df2 = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
      return_df2 = df2.pct_change()[1:]
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      returns = df.pct_change()
      returns["benchmark"] = return_df2
      returns = pd.DataFrame(returns)
    else:
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      returns = df.pct_change()
      returns = pd.DataFrame(returns)

    if plot==True:
        returns.plot(figsize=(20,10))
        plt.xlabel('Date') 
        plt.ylabel('Returns') 
        plt.title(stocks[0] +' Returns (Period : '+ period+')')
    else:
        return returns
# ------------------------------------------------------------------------------------------

def covariance(stocks, period="max", pricing="Adj Close", trading_year_days=252):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)[pricing].pct_change())
    }
  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  returns = df.pct_change()
  cov_matrix_annual = returns.cov()*trading_year_days
  return cov_matrix_annual
# ------------------------------------------------------------------------------------------

def ohlcv(stocks, period="max", trading_year_days=252):

  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)
  df = pd.DataFrame(df)
  df = df.tail(years[period])
  df = pd.DataFrame(df)
  df = df.drop(['Adj Close'], axis=1)
  df = df[["Open", "High", "Low", "Close", "Volume"]]
  return df

# ------------------------------------------------------------------------------------------

def graph_creturns(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  if len(stocks) > 1:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    df = pd.DataFrame(df)
    df = df.tail(years[period])

    ret_data = df.pct_change()[1:]

    port_ret = (ret_data * wts).sum(axis = 1)
    cumulative_ret_df1 = (port_ret + 1).cumprod()

    
    plt.figure(figsize=(20,10))
    stock_raw = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    stock = pd.DataFrame(stock_raw)
    stock = stock.tail(years[period])
    port_ret = stock.sum(axis=1)
    stock_normed = stock/stock.iloc[0]
    stock_normed['Portfolio'] = cumulative_ret_df1
    stock_normed.plot(figsize=(12,8))

  else:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    df = pd.DataFrame(df)
    df = df.tail(years[period])
    ret_data = df.pct_change()[1:]
    weighted_returns = ret_data
    port_ret = weighted_returns.sum(axis=1)
    cumulative_ret = (port_ret + 1).cumprod()
    cumulative_ret = pd.DataFrame(cumulative_ret)
    cumulative_ret.columns = ['Cumulative returns']
    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(cumulative_ret)
    ax1.set_xlabel('Date')
    ax1.set_ylabel("Cumulative Returns")
    ax1.set_title("Portfolio Cumulative Returns")
    plt.show();

# ------------------------------------------------------------------------------------------

def creturns(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  if len(stocks) > 1:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    df = pd.DataFrame(df)
    df = df.tail(years[period])

    ret_data = df.pct_change()[1:]

    port_ret = (ret_data * wts).sum(axis = 1)
    cumulative_ret_df1 = (port_ret + 1).cumprod()

    
    plt.figure(figsize=(20,10))
    stock_raw = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    stock = pd.DataFrame(stock_raw)
    stock = stock.tail(years[period])
    port_ret = stock.sum(axis=1)
    stock_normed = stock/stock.iloc[0]
    stock_normed['Portfolio'] = cumulative_ret_df1
    return stock_normed

  else:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    df = pd.DataFrame(df)
    df = df.tail(years[period])
    ret_data = df.pct_change()[1:]
    weighted_returns = ret_data
    port_ret = weighted_returns.sum(axis=1)
    cumulative_ret = (port_ret + 1).cumprod()
    cumulative_ret = pd.DataFrame(cumulative_ret)
    cumulative_ret.columns = ['Cumulative returns']
    return cumulative_ret

# ------------------------------------------------------------------------------------------

def annual_volatility(stocks, wts=1, start_date, end_date):
  if len(stocks)>1:
    price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
    price_data = price_data['Adj Close']

    ret_data = price_data.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    cumulative_ret = (port_ret + 1).cumprod()
    annual_std = np.std(port_ret) * np.sqrt(252)
    return annual_std
  else:
    price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
    price_data = price_data['Adj Close']

    ret_data = price_data.pct_change()[1:]
    annual_std = np.std(ret_data) * np.sqrt(252)
    return annual_std

# ------------------------------------------------------------------------------------------

def sharpe(stocks, wts=1, rf=0.0, period='max', annualize=True, trading_year_days=253):

  p = {"period": period}

  for stock in stocks:
    years = {
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  start_date = today - relativedelta(days=years[period]) 

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)['Adj Close']
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    sharpe = qs.stats.sharpe(port_ret, rf=0.0, periods=period, annualize=True, trading_year_days=252)
    return sharpe
  else:
     _returns = yf.Ticker(stocks).history(**p)['Close'].pct_change()
     sharpe = qs.stats.sharpe(_returns, rf=0.0, periods=period, annualize=True, trading_year_days=252)
     return sharpe


# ------------------------------------------------------------------------------------------

def graph_rbenchmark(stocks, wts=1, benchmark, start_date, end_date):

  if len(stocks)>1 and len(wts)>1:

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
    plt.title('Comparison')
    plt.show()
  else:
    price_data = web.get_data_yahoo(stocks,
                                  start = start_date,
                                  end = end_date)
    price_data = price_data['Adj Close']

    df2 = web.get_data_yahoo(benchmark, start=start_date, end= end_date)

    ret_data = price_data.pct_change()[1:]
    return_df2 = df2.Close.pct_change()[1:]
    ret_data["benchmark"] = return_df2
    ret_data.plot(figsize=(20,10))
#----------------------------------------------------------------------------------------
def rbenchmark(stocks, wts=1, benchmark, start_date, end_date):

  if len(stocks)>1 and len(wts)>1:

    price_data = web.get_data_yahoo(stocks,
                                  start = start_date,
                                  end = end_date)
    price_data = price_data['Adj Close']

    df2 = web.get_data_yahoo(benchmark, start=start_date, end= end_date)

    ret_data = price_data.pct_change()[1:]
    return_df2 = df2.Close.pct_change()[1:]

    port_ret = (ret_data * wts).sum(axis = 1)
    ret_data['benchmark'] = return_df2
    ret_data['portfolio'] = port_ret
    ret_data = pd.DataFrame(ret_data)
    return ret_data

  else:
    price_data = web.get_data_yahoo(stocks,
                                  start = start_date,
                                  end = end_date)
    price_data = price_data['Adj Close']

    df2 = web.get_data_yahoo(benchmark, start=start_date, end= end_date)

    ret_data = price_data.pct_change()[1:]
    return_df2 = df2.Close.pct_change()[1:]
    ret_data["benchmark"] = return_df2
    ret_data = pd.DataFrame(ret_data)
    return ret_data

# ------------------------------------------------------------------------------------------

def creturns(stocks,wts=1, period="max", benchmark= None, plot=True, pricing="Adj Close", trading_year_days=252):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1mo' : math.ceil(trading_year_days/12),
      '3mo' : math.ceil(trading_year_days/4),
      '6mo' : math.ceil(trading_year_days/2),
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  if len(stocks) > 1:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    if benchmark != None:
      df2 = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      df2 = df2.tail(years[period])
      return_df2 = df2.pct_change()[1:]
      ret_data = df.pct_change()[1:]
      ret_data = (ret_data + 1).cumprod()
      port_ret = (ret_data * wts).sum(axis = 1)
      return_df2 = (return_df2 + 1).cumprod()
      ret_data['Portfolio'] = port_ret
      ret_data['Benchmark'] = return_df2
      ret_data = pd.DataFrame(ret_data)
    else:     
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      ret_data = df.pct_change()[1:]
      ret_data = (ret_data + 1).cumprod()
      port_ret = (ret_data * wts).sum(axis = 1)
      ret_data['Portfolio'] = port_ret
      ret_data = pd.DataFrame(ret_data)

    if plot==True:
      ret_data.plot(figsize=(20,10))
      plt.xlabel('Date') 
      plt.ylabel('Returns') 
      plt.title(period + 'Portfolio Cumulative Returns')
    else:
      return ret_data
  else:
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    if benchmark != None:
      df2 = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
      return_df2 = df2.pct_change()[1:]
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      df2 = df2.tail(years[period])
      return_df2 = df2.pct_change()[1:]
      returns = df.pct_change()
      returns = (returns + 1).cumprod()
      return_df2 = (return_df2 + 1).cumprod()
      returns["benchmark"] = return_df2
      returns = pd.DataFrame(returns)
    else:
      df = pd.DataFrame(df)
      df = df.tail(years[period])
      returns = df.pct_change()
      returns = (returns + 1).cumprod()
      returns = pd.DataFrame(returns)

    if plot==True:
        returns.plot(figsize=(20,10))
        plt.axvline(x=1)
        plt.xlabel('Date') 
        plt.ylabel('Returns') 
        plt.title(stocks[0] +' Cumulative Returns (Period : '+ period+')')

    else:
        return returns

# ------------------------------------------------------------------------------------------

def efficient_frontier(stocks, start_date, end_date, iterations):

  stock_raw = web.DataReader(stocks, 'yahoo', start= start_date, end = end_date)
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

  data = {'stats': ['Expected Return (in %)','Volality','Sharpe ratio'],
        'value': [max_sr_ret*100,max_sr_vol,sharpe_arr.max()]
        }

  print('Optimized allocation (in %):')
  allocation = [i * 100 for i in all_weights[sharpe_arr.argmax(),:] ]
  print(allocation)

  df = pd.DataFrame(data)
  print(df)
  
  plt.figure(figsize=(14,8))
  plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
  plt.colorbar(label='Sharpe Ratio')
  plt.xlabel('Volatility')
  plt.ylabel('Return')

  # Add red dot for max SR
  plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')

# ------------------------------------------------------------------------------------------
def mean_daily_return(stocks,wts=1, start_date, end_date):
  
  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = (stock * wts).sum(axis = 1)
  cum_port = port_ret.pct_change(1)
  mean_return_port = cum_port.mean()

  stock_raw = web.DataReader(stocks, 'yahoo', start_date, end_date)
  stock = stock_raw['Adj Close']
  port_ret = stock.sum(axis=1)
  mean_daily_ret = stock.pct_change(1).mean()
  mean_daily_ret["Portfolio"] = mean_return_port
  mean_daily_ret = pd.DataFrame(mean_daily_ret)
  
  return mean_daily_ret

# ------------------------------------------------------------------------------------------

def var(value_invested, stocks, wts=1, alpha, start_date, end_date):
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
def alpha(stocks, wts=1, benchmark, start_date, end_date):
  if len(stocks) > 1:
      assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      benchmark = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      ret_data = assets.pct_change()[1:]
      r_a = (ret_data * wts).sum(axis = 1)
      r_b = benchmark.pct_change()[1:]

      X = r_b.values # Get just the values, ignore the timestamps
      Y = r_a.values

      def linreg(x,y):
          # We add a constant so that we can also fit an intercept (alpha) to the model
          # This just adds a column of 1s to our data
          x = sm.add_constant(x)
          model = regression.linear_model.OLS(y,x).fit()
          # Remove the constant now that we're done
          x = x[:, 1]
          return model.params[0], model.params[1]

      alpha, beta = linreg(X,Y)
      return alpha
  else:
      asset = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      benchmark = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']

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
      return alpha

#-------------------------------------------------------------------------------------------------
def beta(stocks, wts=1, benchmark, start_date, end_date):
  if len(stocks) > 1:
      assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      benchmark = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      ret_data = assets.pct_change()[1:]
      r_a = (ret_data * wts).sum(axis = 1)
      r_b = benchmark.pct_change()[1:]

      X = r_b.values # Get just the values, ignore the timestamps
      Y = r_a.values

      def linreg(x,y):
          # We add a constant so that we can also fit an intercept (alpha) to the model
          # This just adds a column of 1s to our data
          x = sm.add_constant(x)
          model = regression.linear_model.OLS(y,x).fit()
          # Remove the constant now that we're done
          x = x[:, 1]
          return model.params[0], model.params[1]

      alpha, beta = linreg(X,Y)
      return beta
  else:
      asset = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
      benchmark = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']

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
      return beta
#-------------------------------------------------------------------------------------------------------------------

def corr(stocks, period="max", method="pearson", pricing="Adj Close", trading_year_days=252):
    p = {"period": period}
    for stock in stocks:
      years = {
        '1y': trading_year_days,
        '2y' : 2*trading_year_days,
        '5y' : 5*trading_year_days,
        '10y' : 10*trading_year_days,
        'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
      }
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
    df = pd.DataFrame(df)
    df = df.tail(years[period])
    returns = df.pct_change()
    corr_matrix = returns.corr(method)
    return corr_matrix
#-----------------------------------------------------------------------------------------------------
def correlation(stocks, period="max", plot=True, method="pearson", pricing="Adj Close", trading_year_days=252):
    if plot==False:
      return corr(stocks, period, method, pricing, trading_year_days)
    else:
      corr_mat = corr(stocks, period, method, pricing, trading_year_days)
      seaborn.heatmap(corr_mat, annot=True)
      plt.show()

#-----------------------------------------------------------------------------------------------------
def graph_kalman(stocks, start_date, end_date, noise_value):
  x = web.DataReader(stocks, data_source='yahoo', start = start_date, end = end_date)['Adj Close']
  # Construct a Kalman filter
  kf = KalmanFilter(transition_matrices = [1],
                    observation_matrices = [1],
                    initial_state_mean = x[0],
                    initial_state_covariance = 1,
                    observation_covariance=1,
                    transition_covariance= noise_value)

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

def kalman(stocks, start_date, end_date, noise_value):
  x = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']

  # Construct a Kalman filter
  kf = KalmanFilter(transition_matrices = [1],
                    observation_matrices = [1],
                    initial_state_mean = x[0],
                    initial_state_covariance = 1,
                    observation_covariance=1,
                    transition_covariance= noise_value)

  # Use the observed values of the price to get a rolling mean
  state_means, _ = kf.filter(x.values)
  state_means = pd.Series(state_means.flatten(), index=x.index)
  state_means = pd.DataFrame(state_means)
  return state_means

#---------------------------------------------------------------------------------------------------------------
def capm(stocks, wts=1, start_date, end_date):

  assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  ret_data = assets.pct_change()[1:]

  R = (ret_data * wts).sum(axis = 1)

  R_F = web.DataReader('BIL', data_source='yahoo', start = start_date, end = end_date)['Adj Close'].pct_change()[1:]
  
  # find it's beta against market
  M = web.DataReader('SPY', data_source='yahoo', start = start_date, end = end_date)['Adj Close'].pct_change()[1:]

  results = regression.linear_model.OLS(R-R_F, sm.add_constant(M)).fit()
  beta = results.params[1]
  alpha = results.params[0]
  return results.summary()
  #--------------------------------------------------------------------------------------------------------------
def cointegration(stock1, stock2, start_date, end_date):
    X1 = web.DataReader(stock1, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    X2 = web.DataReader(stock2, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
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
#--------------------------------------------------------------------------------------------------------------------------
def stationarity(stock, start_date, end_date):
  X = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
  def check_for_stationarity(X, cutoff=0.01):
    # H_0 in adfuller is unit root exists (non-stationary)
    # We must observe significant p-value to convince ourselves that the series is stationary
    pvalue = adfuller(X)[1]
    if pvalue < cutoff:
        print('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely stationary.')
    else:
        print('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely non-stationary.')

  plt.plot(X)
  plt.xlabel('Time')
  plt.ylabel('Series Value')
  plt.legend(['Z']);
  return check_for_stationarity(X)
#---------------------------------------------------------------------------------------------------------------------

def graph_rvolatility(stock, wts=1, start_date, end_date, window_time):
  if len(stock)==1:
    asset = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    # Compute the logarithmic returns using the Closing price 
    asset['Log_Ret'] = np.log(asset['Adj Close'] / asset['Adj Close'].shift(1))
    # Compute Volatility using the pandas rolling standard deviation function
    asset['Volatility'] = asset['Log_Ret'].rolling(window=window_time).std() * np.sqrt(252)
    asset = pd.DataFrame(asset)
    # Plot the NIFTY Price series and the Volatility
    asset[['Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))
  else:
    asset = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    port_ret = (asset * wts).sum(axis = 1)
    asset['Adj Close'] = port_ret
    # Compute the logarithmic returns using the Closing price 
    asset['Log_Ret'] = np.log(asset['Adj Close'] / asset['Adj Close'].shift(1))
    # Compute Volatility using the pandas rolling standard deviation function
    asset['Volatility'] = asset['Log_Ret'].rolling(window=window_time).std() * np.sqrt(252)
    # Plot the NIFTY Price series and the Volatility
    asset[['Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))
#------------------------------------------------------------------------------------------------------------------------
def rvolatility(stock, wts=1, start_date, end_date, window_time):
  if len(stock)==1:
    asset = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    # Compute the logarithmic returns using the Closing price 
    asset['Log_Ret'] = np.log(asset['Adj Close'] / asset['Adj Close'].shift(1))
    # Compute Volatility using the pandas rolling standard deviation function
    asset['Volatility'] = asset['Log_Ret'].rolling(window=window_time).std() * np.sqrt(252)
    df = asset['Volatility']
    df = pd.DataFrame(df)
    return df

  else:
    asset = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    port_ret = (asset * wts).sum(axis = 1)
    asset['Adj Close'] = port_ret
    # Compute the logarithmic returns using the Closing price 
    asset['Log_Ret'] = np.log(asset['Adj Close'] / asset['Adj Close'].shift(1))
    print(asset['Adj Close'])
    # Compute Volatility using the pandas rolling standard deviation function
    asset['Volatility'] = asset['Log_Ret'].rolling(window=window_time).std() * np.sqrt(252)
    df = asset['Volatility']
    df = pd.DataFrame(df)
    return df
#------------------------------------------------------------------------------------------------------------------------------------------

def graph_ralpha(stock,wts=1, benchmark, start_date, end_date, window_time):

  if len(stock)==1:
    # get the closing price of AMZN Stock
    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    amzn = pd.DataFrame(amzn)
    amzn['amzn_return'] = amzn['Adj Close'].pct_change()
    amzn['amzn_log_return'] = np.log(amzn['Adj Close']) - np.log(amzn['Adj Close'].shift(1))
    amzn.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)

    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(amzn.amzn_return, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = amzn.index
    plt.figure(figsize=(12,8))
    results.alpha.plot.line()
    plt.title("Market Alpha: Rolling Window of "+str(window_time)+" Days")
  else:

    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    amzn['Adj Close'] = (amzn * wts).sum(axis = 1)
    df = returns(stock, wts, start_date, end_date)
    df['Adj Close'] = amzn[['Adj Close']]
    df1 = df[['Adj Close', 'Portfolio returns']]
    df1.columns = ['Adj Close', 'returns' ]
    df1['log_return'] = np.log(df1['Adj Close']) - np.log(df1['Adj Close'].shift(1))
    df.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)
    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(df1.returns, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = df1.index
    plt.figure(figsize=(12,8))
    results.alpha.plot.line()
    plt.title("Market Alpha: Rolling Window of "+ str(window_time) + " Days")

  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def graph_rbeta(stock,wts=1, benchmark, start_date, end_date, window_time):

  if len(stock)==1:
    # get the closing price of AMZN Stock
    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    amzn = pd.DataFrame(amzn)
    amzn['amzn_return'] = amzn['Adj Close'].pct_change()
    amzn['amzn_log_return'] = np.log(amzn['Adj Close']) - np.log(amzn['Adj Close'].shift(1))
    amzn.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)

    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(amzn.amzn_return, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = amzn.index
    plt.figure(figsize=(12,8))
    results.beta.plot.line()
    plt.title("Market Beta: Rolling Window of "+str(window_time) + " Days")
  else:

    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    amzn['Adj Close'] = (amzn * wts).sum(axis = 1)
    df = returns(stock, wts, start_date, end_date)
    df['Adj Close'] = amzn[['Adj Close']]
    df1 = df[['Adj Close', 'Portfolio returns']]
    df1.columns = ['Adj Close', 'returns' ]
    df1['log_return'] = np.log(df1['Adj Close']) - np.log(df1['Adj Close'].shift(1))
    df.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)
    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(df1.returns, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = df1.index
    plt.figure(figsize=(12,8))
    results.beta.plot.line()
    plt.title("Market Beta: Rolling Window of " +str(window_time)+ " Days")


#--------------------------------------------------------------------------------------------------------------------------------
def rbeta(stock,wts=1, benchmark, start_date, end_date, window_time):

  if len(stock)==1:
    # get the closing price of AMZN Stock
    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    amzn = pd.DataFrame(amzn)
    amzn['amzn_return'] = amzn['Adj Close'].pct_change()
    amzn['amzn_log_return'] = np.log(amzn['Adj Close']) - np.log(amzn['Adj Close'].shift(1))
    amzn.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)

    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(amzn.amzn_return, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = amzn.index
    df = results['beta']
    df = pd.DataFrame(df)
    return df
  else:

    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    amzn['Adj Close'] = (amzn * wts).sum(axis = 1)
    df = returns(stock, wts, start_date, end_date)
    df['Adj Close'] = amzn[['Adj Close']]
    df1 = df[['Adj Close', 'Portfolio returns']]
    df1.columns = ['Adj Close', 'returns' ]
    df1['log_return'] = np.log(df1['Adj Close']) - np.log(df1['Adj Close'].shift(1))
    df.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)
    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(df1.returns, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = df1.index
    df = results['beta']
    df = pd.DataFrame(df)
    return df
#--------------------------------------------------------------------------------------------------------------------------------------
def ralpha(stock,wts=1, benchmark, start_date, end_date, window_time):

  if len(stock)==1:
    # get the closing price of AMZN Stock
    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)
    amzn = pd.DataFrame(amzn)
    amzn['amzn_return'] = amzn['Adj Close'].pct_change()
    amzn['amzn_log_return'] = np.log(amzn['Adj Close']) - np.log(amzn['Adj Close'].shift(1))
    amzn.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)

    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(amzn.amzn_return, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = amzn.index
    df = results['alpha']
    df = pd.DataFrame(df)
    return df
  else:

    amzn = web.DataReader(stock, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    amzn['Adj Close'] = (amzn * wts).sum(axis = 1)
    df = returns(stock, wts, start_date, end_date)
    df['Adj Close'] = amzn[['Adj Close']]
    df1 = df[['Adj Close', 'Portfolio returns']]
    df1.columns = ['Adj Close', 'returns' ]
    df1['log_return'] = np.log(df1['Adj Close']) - np.log(df1['Adj Close'].shift(1))
    df.dropna(inplace=True)
    
    
    nasdaq = web.DataReader(benchmark, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    nasdaq = pd.DataFrame(nasdaq)
    nasdaq['nasdaq_return'] = nasdaq['Adj Close'].pct_change()
    nasdaq['nasdaq_log_return'] = np.log(nasdaq['Adj Close']) - np.log(nasdaq['Adj Close'].shift(1))
    nasdaq.dropna(inplace=True)
    def market_beta(X,Y,N):
        """ 
        X = The independent variable which is the Market
        Y = The dependent variable which is the Stock
        N = The length of the Window
        
        It returns the alphas and the betas of
        the rolling regression
        """
        
        # all the observations
        obs = len(X)
        
        # initiate the betas with null values
        betas = np.full(obs, np.nan)
        
        # initiate the alphas with null values
        alphas = np.full(obs, np.nan)
        
        
        for i in range((obs-N)):
            regressor = LinearRegression()
            regressor.fit(X.to_numpy()[i : i + N+1].reshape(-1,1), Y.to_numpy()[i : i + N+1])
            
            betas[i+N]  = regressor.coef_[0]
            alphas[i+N]  = regressor.intercept_
    
        return(alphas, betas)
      
    results = market_beta(df1.returns, nasdaq.nasdaq_return, window_time)
    
    results = pd.DataFrame(list(zip(*results)), columns = ['alpha', 'beta'])
    
    results.index = df1.index
    df = results['alpha']
    df = pd.DataFrame(df)
    return df
    return results.alpha
#--------------------------------------------------------------------------------------------------------------------
def backtest(stocks, wts=1, benchmark, start_date, end_date):

  price_data = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date )
  price_data = price_data['Adj Close']


  ret_data = price_data.pct_change()[1:]

  port_ret = (ret_data * wts).sum(axis = 1)
  cumulative_ret_df1 = (port_ret + 1).cumprod()

  total_return = (cumulative_ret_df1.iloc[-1]-1)*100
  total_return = round(total_return, 2)
  total_return = str(total_return) + '%'
  volatility = annual_volatility(stocks, wts,start_date, end_date)*100
  volatility = round(volatility, 2)
  volatility = str(volatility) + '%'
  s_ratio = sharpe_ratio(stocks, wts ,start_date, end_date)
  s_ratio = round(s_ratio, 2)
  alpha_port = alpha(stocks, wts, benchmark, start_date, end_date)
  alpha_port = round(alpha_port, 4)
  beta_port = beta(stocks, wts, benchmark, start_date, end_date)
  beta_port = round(beta_port, 2)

  data = {'Backtest': ['Return','Annual volatility','Sharpe ratio','Alpha', 'Beta'],
        'Portfolio': [total_return,volatility,s_ratio, alpha_port, beta_port]
        }

  df = pd.DataFrame(data)
  df2 = mean_daily_return(stocks,wts, start_date, end_date)
  df2 = pd.DataFrame(df2)
  print("Mean daily return of the portfolio")
  print(df2)
  graph_cbenchmark(stocks, wts, benchmark, start_date, end_date)
  graph_creturns(stocks, wts, start_date, end_date)
  graph_returns(stocks,wts, start_date, end_date)
  graph_rbenchmark(stocks, wts, benchmark, start_date, end_date)
  graph_rvolatility(stocks,wts, start_date, end_date, 180)
  graph_rbeta(stocks,wts, benchmark, start_date, end_date, 180)
  print(capm(stocks, wts, start_date, end_date))
  return df
