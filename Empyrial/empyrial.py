import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as web
import datetime as dt
from empyrical import*
import quantstats as qs
from darts.models import*
from darts import TimeSeries
from darts.utils.missing_values import fill_missing_values
from darts.metrics import mape, mase
import logging
import warnings
from warnings import filterwarnings

# ------------------------------------------------------------------------------------------

today = dt.date.today()

# ------------------------------------------------------------------------------------------

class Engine:

  def __init__(self,start_date, portfolio, weights, benchmark=['SPY'], end_date=today):
    self.start_date = start_date
    self.end_date = end_date
    self.portfolio = portfolio
    self.weights = weights
    self.benchmark = benchmark

#-------------------------------------------------------------------------------------------
def get_returns(stocks,wts, start_date, end_date=today):
  if len(stocks) > 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    ret_data = assets.pct_change()[1:]
    returns = (ret_data * wts).sum(axis = 1)
    return returns
  else:
    df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)['Adj Close']
    df = pd.DataFrame(df)
    returns = df.pct_change()
    return returns
# ------------------------------------------------------------------------------------------
def get_pricing(stocks, start_date, end_date=today, pricing="Adj Close", wts=1):
  if len(stocks) > 1:
    assets = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)[pricing]
    return assets
  else:
    df = web.DataReader(stocks, data_source='yahoo', start = start_date, end= end_date)[pricing]
    return df
# ------------------------------------------------------------------------------------------

def get_data(stocks, period="max", trading_year_days=252):

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
def information_ratio(returns, benchmark_returns, days=252):
 return_difference = returns - benchmark_returns
 volatility = return_difference.std() * np.sqrt(days)
 information_ratio = return_difference.mean() / volatility
 return information_ratio

def graph_allocation(my_portfolio):
  fig1, ax1 = plt.subplots()
  ax1.pie(my_portfolio.weights, labels=my_portfolio.portfolio, autopct='%1.1f%%',
          shadow=False, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title("Portfolio's allocation")
  plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------
def empyrial(my_portfolio, rf=0.0, sigma_value=1, confidence_value=0.95):

  returns = get_returns(my_portfolio.portfolio, my_portfolio.weights, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
  benchmark = get_returns(my_portfolio.benchmark, wts=[1], start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)

  print("Start date: "+ str(returns.index[0]))
  print("End date: "+ str(returns.index[-1]))
  CAGR = cagr(returns, period=DAILY, annualization=None)
  CAGR = round(CAGR,2)
  CAGR = CAGR.tolist()
  CAGR = str(round(CAGR*100,2)) + '%'

  CUM = cum_returns(returns, starting_value=0, out=None)*100
  CUM = CUM.iloc[-1]
  CUM = CUM.tolist()
  CUM = str(round(CUM,2)) + '%'


  VOL = qs.stats.volatility(returns, annualize=True, trading_year_days=252)
  VOL = VOL.tolist()
  VOL = str(round(VOL*100,2))+' %'

  SR = sharpe_ratio(returns, risk_free=rf, period=DAILY)
  SR = np.round(SR, decimals=2)
  SR = str(SR)

  CR =  qs.stats.calmar(returns)
  CR = CR.tolist()
  CR = str(round(CR,2))

  STABILITY = stability_of_timeseries(returns)
  STABILITY = round(STABILITY,2)
  STABILITY = str(STABILITY)


  MD = max_drawdown(returns, out=None)
  MD = str(round(MD,2))+' %'

  
  '''OR = omega_ratio(returns, risk_free=0.0, required_return=0.0)
  OR = round(OR,2)
  OR = str(OR)
  print(OR)'''

  SOR = sortino_ratio(returns, required_return=0, period=DAILY)
  SOR = round(SOR,2)
  SOR = str(SOR)


  SK = qs.stats.skew(returns)
  SK = round(SK,2)
  SK = SK.tolist()
  SK = str(SK)


  KU = qs.stats.kurtosis(returns)
  KU = round(KU,2)
  KU = KU.tolist()
  KU = str(KU)

  TA = tail_ratio(returns)
  TA = round(TA,2)
  TA = str(TA)


  CSR = qs.stats.common_sense_ratio(returns)
  CSR = round(CSR,2)
  CSR = CSR.tolist()
  CSR = str(CSR)


  VAR = qs.stats.value_at_risk(returns, sigma=sigma_value, confidence=confidence_value)
  VAR = np.round(VAR, decimals=2)
  VAR = str(VAR*100)+' %'

  AL = alpha_beta(returns, benchmark, risk_free=rf)
  AL = AL[0]
  AL = round(AL,2)

  BTA = alpha_beta(returns, benchmark, risk_free=rf)
  BTA = BTA[1]
  BTA = round(BTA,2)

  def condition(x):
    return x > 0

  win = sum(condition(x) for x in returns)
  total = len(returns)
  win_ratio = win/total
  win_ratio = win_ratio*100
  win_ratio = round(win_ratio,2)

  IR = information_ratio(returns, benchmark.iloc[:,0])
  IR = round(IR,2)



  data = {'':['Annual return', 'Cumulative return', 'Annual volatility','Winning day ratio', 'Sharpe ratio','Calmar ratio', 'Information ratio', 'Stability', 'Max Drawdown','Sortino ratio','Skew', 'Kurtosis', 'Tail Ratio', 'Common sense ratio', 'Daily value at risk',
              'Alpha', 'Beta'

  ],
        'Backtest':[CAGR, CUM, VOL,f'{win_ratio}%', SR, CR, IR, STABILITY, MD, SOR, SK, KU, TA, CSR, VAR, AL, BTA]}

  # Create DataFrame

  df = pd.DataFrame(data)
  df.set_index('', inplace=True)
  df.style.set_properties(**{'background-color': 'white',
                           'color': 'black',
                           'border-color':'black'})

  display(df)

  y = []
  for x in returns:
    y.append(x)

  arr = np.array(y)
  arr
  returns.index
  my_color = np.where(arr>=0, 'blue', 'grey')
  plt.figure(figsize=(30,8))
  plt.vlines(x=returns.index, ymin=0, ymax=arr, color=my_color, alpha=0.4)
  plt.title('Returns')


  return qs.plots.returns(returns,benchmark, cumulative=True), qs.plots.monthly_heatmap(returns), qs.plots.drawdown(returns), qs.plots.drawdowns_periods(returns), qs.plots.rolling_volatility(returns), qs.plots.rolling_sharpe(returns), qs.plots.rolling_beta(returns, benchmark)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def oracle(my_portfolio, prediction_days=None, based_on='Adj Close'):
  logger = logging.getLogger()
  warnings.simplefilter(action='ignore', category=FutureWarning)
  filterwarnings('ignore')
  
  logging.disable(logging.INFO)

  mape_df = pd.DataFrame()
  mape_df = mape_df.append({'Exponential smoothing' : 0, 'Prophet' : 0, 'Auto-ARIMA' :  0, 'Theta(2)':0, 'ARIMA' : 0, 'FFT' : 0, 'FourTheta' :  0, 'NaiveDrift':0, 'NaiveMean' :  0, 'NaiveSeasonal':0 }, 
                ignore_index = True)

  final_df = pd.DataFrame()
  final_df = final_df.append({'Exponential smoothing' : 0, 'Prophet' : 0, 'Auto-ARIMA' :  0, 'Theta(2)':0, 'ARIMA' : 0, 'FFT' : 0, 'FourTheta' :  0, 'NaiveDrift':0, 'NaiveMean' :  0, 'NaiveSeasonal':0 },
                ignore_index = True)

  for asset in my_portfolio.portfolio:

    result = pd.DataFrame()

    df = web.DataReader(asset, data_source='yahoo', start = my_portfolio.start_date, end= my_portfolio.end_date)
    df = pd.DataFrame(df)
    df.reset_index(level=0, inplace=True)

    if prediction_days==None:
      x = 1
      while x/(len(df)+x) < 0.3:
        x+=1
        prediction_days = x

    def eval_model(model):
      model.fit(train)
      forecast = model.predict(len(val))
      result[model] = [mape(val, forecast)]

    prediction = pd.DataFrame()
    def predict(model):
      model.fit(train)
      forecast = model.predict(len(val))
      pred = model.predict(prediction_days)

      b = [str(pred[-1])]
      b = [words for segments in b for words in segments.split()]
      b = float(b[2])
      prediction[model] = [str(round(((b-start_value)/start_value)*100,3))+' %']

    series = TimeSeries.from_dataframe(df, 'Date', based_on, freq='D')
    series = fill_missing_values(series)

    train_index = round(len(df.index)*0.7)
    train_date = df.loc[[train_index]]['Date'].values
    date = str(train_date[0])[:10]
    date = date.replace('-', '') 
    timestamp = date+'000000'
    train, val = series.split_before(pd.Timestamp(timestamp))
    eval_model(ExponentialSmoothing())
    eval_model(Prophet())
    eval_model(AutoARIMA())
    eval_model(Theta())
    eval_model(ARIMA())
    eval_model(FFT())
    eval_model(FourTheta())
    eval_model(NaiveDrift())
    eval_model(NaiveMean())
    eval_model(NaiveSeasonal())
    result.columns = ['Exponential smoothing','Prophet', 'Auto-ARIMA', 'Theta(2)', 'ARIMA', 'FFT','FourTheta','NaiveDrift','NaiveMean', 'NaiveSeasonal']
    result.index = [asset]
    mape_df = pd.concat([result, mape_df])
    start_pred = str(df["Date"].iloc[-2])[:10]
    start_value = df[based_on].iloc[-2]
    start_pred = start_pred.replace('-', '') 
    timestamp = start_pred+'000000'
    train, val = series.split_before(pd.Timestamp(timestamp))

    predict(ExponentialSmoothing())
    predict(Prophet())
    predict(AutoARIMA())
    predict(Theta())
    predict(ARIMA())
    predict(FFT())
    predict(FourTheta())
    predict(NaiveDrift())
    predict(NaiveMean())
    predict(NaiveSeasonal())

    prediction.columns = ['Exponential smoothing','Prophet', 'Auto-ARIMA', 'Theta(2)', 'ARIMA', 'FFT','FourTheta','NaiveDrift','NaiveMean', 'NaiveSeasonal']
    prediction.index = [asset]
    final_df = pd.concat([prediction, final_df])

  print("Assets MAPE (accuracy score)")
  with pd.option_context('display.max_rows', None, 'display.max_columns', None) and pd.option_context('expand_frame_repr', False):
    print(mape_df.iloc[:-1,:])
  mape_df = pd.DataFrame(mape_df.iloc[:-1,:])
  print("\n")
  print("Assets returns prediction for the next "+str(prediction_days)+" days")
  with pd.option_context('display.max_rows', None, 'display.max_columns', None) and pd.option_context('expand_frame_repr', False):
    print(final_df.iloc[:-1,:])
  final_df = pd.DataFrame(final_df.iloc[:-1,:])
  
  portfolio_pred = pd.DataFrame()

  for column in final_df.columns:
    rets = []
    for index in final_df.index:
      place = my_portfolio.portfolio.index(index)
      returns = float(final_df[column][index][:-1])
      wts = my_portfolio.weights[my_portfolio.portfolio.index(index)]
      ret = (returns*wts)
      rets.append(ret)
    portfolio_pred[column] = rets
    portfolio_pred[column] = portfolio_pred[column].sum()

  print("\n")
  print("Portfolio returns prediction for the next "+str(prediction_days)+" days")
  display(portfolio_pred.iloc[0])
  

  logger.disabled = False
