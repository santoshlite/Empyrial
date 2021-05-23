import numpy as np
import pandas as pd
import math
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
from empyrical import*
import quantstats as qs

# ------------------------------------------------------------------------------------------

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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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
      '20y' : 20*trading_year_days,
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

def creturns(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252, plot=True):
  p = {"period": period}
  for stock in stocks:
    years = {
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      '20y' : 20*trading_year_days,
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

    if plot!=True:
      return stock_normed
    else:
      stock_normed.plot(figsize=(20,10))
      plt.xlabel('Date')
      plt.ylabel('Returns')
      plt.title('Portfolio Cumulative Returns (Period : '+ period+')')

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
    if plot!=True:
      return cumulative_ret
    else:
      cumulative_ret.plot(figsize=(20,10))
      plt.xlabel('Date')
      plt.ylabel('Returns')
      plt.title(stocks[0] +' Cumulative Returns (Period : '+ period+')')

# ------------------------------------------------------------------------------------------

def volatility(stocks, wts=1, period='max', pricing='Adj Close', annualize=True, trading_year_days=253):

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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  start_date = today - relativedelta(days=years[period])

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)[pricing]
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    vol = qs.stats.volatility(port_ret, periods=period, annualize=True, trading_year_days=252)
    return vol
  else:
     stock = qs.utils.download_returns(stocks[0])
     stock = stock.tail(years[period])
     vol = qs.stats.volatility(stock, periods=period, annualize=True, trading_year_days=252)
     return vol
# ------------------------------------------------------------------------------------------

def sharpe(stocks, wts=1, risk_free=0.0, period='max',pricing='Adj Close', annualize=True, trading_year_days=253):

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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  start_date = today - relativedelta(days=years[period])

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)[pricing]
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    sharpe = qs.stats.sharpe(port_ret, rf=risk_free, periods=period, annualize=True, trading_year_days=252)
    return sharpe
  else:
     stock = qs.utils.download_returns(stocks[0])
     stock = stock.tail(years[period])
     sharpe = qs.stats.sharpe(stock, rf=risk_free, periods=period, annualize=True, trading_year_days=252)
     return sharpe
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
      '20y' : 20*trading_year_days,
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
def efficient_frontier(stocks, period="max", pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  df = pd.DataFrame()
  for stock in stocks:
    df[stock] = web.DataReader(stock, data_source='yahoo', start = "1980-01-01", end=today)[pricing]
    df[stock] = df[stock].tail(years[period])
  mu = expected_returns.mean_historical_return(df)
  S = risk_models.sample_cov(df)

  #optimize for max sharpe ratio
  ef = EfficientFrontier(mu, S)
  weights = ef.max_sharpe()
  cleaned_weights = ef.clean_weights()
  print(cleaned_weights)
  ef.portfolio_performance(verbose=True)

# ------------------------------------------------------------------------------------------
def mean_daily_return(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252):

  p = {"period": period}
  for stock in stocks:
    years = {
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  stock_raw = web.DataReader(stocks, 'yahoo', "1980-01-01", today)
  stock_raw = stock_raw.tail(years[period])
  stock = stock_raw[pricing]
  port_ret = (stock * wts).sum(axis = 1)
  cum_port = port_ret.pct_change(1)
  mean_return_port = cum_port.mean()

  stock_raw = web.DataReader(stocks, 'yahoo', "1980-01-01", today)
  stock_raw = stock_raw.tail(years[period])
  stock = stock_raw[pricing]
  port_ret = stock.sum(axis=1)
  mean_daily_ret = stock.pct_change(1).mean()
  mean_daily_ret["Portfolio"] = mean_return_port
  mean_daily_ret = pd.DataFrame(mean_daily_ret)
  mean_daily_ret.columns = ['Mean daily return (in %)']
  return mean_daily_ret*100

# ------------------------------------------------------------------------------------------
def var(stocks, wts=1, confidence=0.95, period='max', pricing='Adj Close',trading_year_days=253):

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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  start_date = today - relativedelta(days=years[period])

  if confidence > 1:
      confidence = confidence/100

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)[pricing]
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    var = qs.stats.var(port_ret, sigma=1, confidence=confidence)
    print("Note : Result is in %")
    return var*100
  else:
     stock = qs.utils.download_returns(stocks[0])
     stock = stock.tail(years[period])
     var = qs.stats.var(stock, sigma=1, confidence=confidence)
     print("Note : Result is in %")
     return var*100

# ------------------------------------------------------------------------------------------
def alpha(stocks, wts=1, benchmark='SPY', period='10y', pricing='Close', trading_year_days=253):

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
      '20y' : 20*trading_year_days,
    }

  start_date = today - relativedelta(days=years[period])

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)[pricing]
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    alpha_beta = qs.stats.greeks(port_ret, benchmark)
    return alpha_beta
  else:
     _returns = yf.Ticker(stocks[0]).history(**p)[pricing].pct_change()
     _returns = _returns.iloc[1:]
     benchmark = yf.Ticker(benchmark).history(**p)[pricing].pct_change()
     benchmark = benchmark.iloc[1:]
     alpha_beta = qs.stats.greeks(_returns, benchmark)
  return alpha_beta[1]

#-------------------------------------------------------------------------------------------------
def beta(stocks, wts=1, benchmark='SPY', period='10y', pricing='Close', trading_year_days=253):

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
      '20y' : 20*trading_year_days,
    }

  start_date = today - relativedelta(days=years[period])

  if wts != 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= today)[pricing]
    ret_data = assets.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    alpha_beta = qs.stats.greeks(port_ret, benchmark)
    return alpha_beta
  else:
     _returns = yf.Ticker(stocks[0]).history(**p)[pricing].pct_change()
     _returns = _returns.iloc[1:]
     benchmark = yf.Ticker(benchmark).history(**p)[pricing].pct_change()
     benchmark = benchmark.iloc[1:]
     alpha_beta = qs.stats.greeks(_returns, benchmark)
  return alpha_beta[0]
#-------------------------------------------------------------------------------------------------------------------

def corr(stocks, period="max", method="pearson", pricing="Adj Close", trading_year_days=252):
    p = {"period": period}
    for stock in stocks:
      years = {
        '1y': trading_year_days,
        '2y' : 2*trading_year_days,
        '5y' : 5*trading_year_days,
        '10y' : 10*trading_year_days,
        '20y' : 20*trading_year_days,
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
def kalman(stocks, noise_value=0.01, period="max", plot=True, pricing="Adj Close", trading_year_days=252):

  p = {"period": period}
  for stock in stocks:
    years = {
      '1y': trading_year_days,
      '2y' : 2*trading_year_days,
      '5y' : 5*trading_year_days,
      '10y' : 10*trading_year_days,
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }
  x = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end = today)[pricing]
  x = x.tail(years[period])

  # Construct a Kalman filter
  kf = KalmanFilter(transition_matrices = [1],
                    observation_matrices = [1],
                    initial_state_mean = x[stocks].iloc[0],
                    initial_state_covariance = 1,
                    observation_covariance=1,
                    transition_covariance= noise_value)

  # Use the observed values of the price to get a rolling mean
  state_means, _ = kf.filter(x.values)
  state_means = pd.Series(state_means.flatten(), index=x.index)
  x = pd.DataFrame(state_means)

  if plot==False:
    return x
  else:
    plt.plot(state_means)
    plt.plot(x)

    plt.title('Kalman filter estimate of average')
    plt.legend(['Kalman Estimate', 'X'])
    plt.xlabel('Day')
    plt.ylabel('Price');
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
def cointegration(stocks, period="max", cutoff_value=0.01, pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }
    X1 = web.DataReader(stocks[0], data_source='yahoo', start = "1980-01-01", end= today)['Adj Close']
    X2 = web.DataReader(stocks[1], data_source='yahoo', start = "1980-01-01", end= today)['Adj Close']
    X1.name = str(stocks[0])
    X2.name = str(stocks[1])
    X1 = X1.tail(years[period])
    X2 = X2.tail(years[period])
    def check_for_stationarity(X, cutoff=cutoff_value):
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
def stationarity(stocks, period="max", cutoff_value=0.1, pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }
  X = web.DataReader(stocks[0], data_source='yahoo', start = "1980-01-01", end= today)[pricing]
  X = X.tail(years[period])

  def check_for_stationarity(X, cutoff=cutoff_value):
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
def rvolatility(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]

  if len(stocks) > 1:
    df = df.tail(years[period])
    port_ret = (df * wts).sum(axis = 1)
    portfolio = port_ret.pct_change()[1:]

    qs.plots.rolling_volatility(portfolio)
  else:
    stock = qs.utils.download_returns(stocks[0])
    qs.plots.rolling_volatility(stock)

#------------------------------------------------------------------------------------------------------------------------------------------

def ralpha(stocks,wts=1, period="10y", benchmark="SPY", window=180, pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
    }

  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]

  if len(stocks) > 1:
    df = df.tail(years[period])
    port_ret = (df * wts).sum(axis = 1)
    returns = port_ret.pct_change()[1:]
  else:
    returns = qs.utils.download_returns(stocks[0])
    returns = returns.tail(years[period])

  dfb = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= today)[pricing]
  dfb = pd.DataFrame(dfb)
  dfb = dfb.tail(years[period])
  benchmark = dfb.pct_change()
  benchmark = pd.DataFrame(benchmark)
  ralpha = roll_alpha_beta(returns, benchmark, window=window)
  plt.plot(ralpha[0])

#--------------------------------------------------------------------------------------------------------------------------------
def rbeta(stocks,wts=1, period="max", pricing="Adj Close", benchmark="SPY", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]

  if len(stocks) > 1:
    df = df.tail(years[period])
    port_ret = (df * wts).sum(axis = 1)
    portfolio = port_ret.pct_change()[1:]

    qs.plots.rolling_beta(portfolio, benchmark)
  else:
    stock = qs.utils.download_returns(stocks[0])
    qs.plots.rolling_beta(stock, benchmark)
#--------------------------------------------------------------------------------------------------------------------------------------
def rsharpe(stocks,wts=1, period="max", pricing="Adj Close", trading_year_days=252):
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
      '20y' : 20*trading_year_days,
      'max' : len(yf.Ticker(stock).history(**p)['Close'].pct_change())
    }

  df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= today)[pricing]

  if len(stocks) > 1:
    df = df.tail(years[period])
    port_ret = (df * wts).sum(axis = 1)
    portfolio = port_ret.pct_change()[1:]

    qs.plots.rolling_sharpe(portfolio)
  else:
    stock = qs.utils.download_returns(stocks[0])
    qs.plots.rolling_sharpe(stock)
#------------------------------------------------------------------------------------------------------------------------------------------------------
def lens(returns, benchmark):

  print("Start date: "+ str(returns.index[0]))
  print("End date: "+ str(returns.index[-1]))
  CAGR = cagr(returns, period=DAILY, annualization=None)
  CAGR = round(CAGR,2)
  CAGR = CAGR.tolist()
  CAGR = str(CAGR[0]*100) + '%'

  CUM = cum_returns(ret, starting_value=0, out=None)*100
  CUM = round(CUM,2)
  CUM = CUM.iloc[-1]
  CUM = CUM.tolist()
  CUM = str(CUM[0]) + '%'


  VOL = qs.stats.volatility(returns, annualize=True, trading_year_days=252)
  VOL = round(VOL,2)
  VOL = VOL.tolist()
  VOL = str(VOL[0])+' %'

  SR = sharpe_ratio(returns, risk_free=0, period=DAILY)
  SR = np.round(SR, decimals=2)
  SR = str(SR[0])

  CR =  qs.stats.calmar(returns)
  CR = round(CR,2)
  CR = CR.tolist()
  CR = str(CR[0])+'%'

  STABILITY = stability_of_timeseries(returns)
  STABILITY = round(STABILITY,2)
  STABILITY = str(STABILITY)


  MD = max_drawdown(ret, out=None)
  MD = round(MD,2)
  MD = MD.tolist()
  MD = str(MD[0])+' %'

  '''
  OR = omega_ratio(returns, risk_free=0.0, required_return=0.0)
  OR = round(OR,2)
  OR = str(OR)
  print(OR)'''

  SOR = sortino_ratio(returns, required_return=0, period=DAILY)
  SOR = round(SOR,2)
  SOR = SOR.tolist()
  SOR = str(SOR[0])


  SK = qs.stats.skew(returns)
  SK = round(SK,2)
  SK = SK.tolist()
  SK = str(SK[0])


  KU = qs.stats.kurtosis(returns)
  KU = round(KU,2)
  KU = KU.tolist()
  KU = str(KU[0])

  TA = tail_ratio(returns)
  TA = round(TA,2)
  TA = str(TA)


  CSR = qs.stats.common_sense_ratio(returns)
  CSR = round(CSR,2)
  CSR = CSR.tolist()
  CSR = str(CSR[0])


  VAR = qs.stats.value_at_risk(ret, sigma=1, confidence=0.95)
  VAR = np.round(VAR, decimals=2)
  VAR = str(VAR[0])+' %'

  AL = alpha_beta(ret, benchmark, risk_free=0.0)
  AL = AL[0]
  AL = round(AL,2)

  BTA = alpha_beta(ret, benchmark, risk_free=0.0)
  BTA = BTA[1]
  BTA = round(BTA,2)

  data = {'':['Annual return', 'Cumulative return', 'Annual volatility', 'Sharpe ratio','Calmar ratio', 'Stability', 'Max Drawdown','Sortino ratio','Skew', 'Kurtosis', 'Tail Ratio', 'Common sense ratio', 'Daily value at risk',
              'Alpha', 'Beta'

  ],
        'Backtest':[CAGR, CUM, VOL, SR, CR, STABILITY, MD, SOR, SK, KU, TA, CSR, VAR, AL, BTA]}

  # Create DataFrame

  df = pd.DataFrame(data)
  df.set_index('', inplace=True)
  df.style.set_properties(**{'background-color': 'white',
                           'color': 'black',
                           'border-color':'black'})
  return df
