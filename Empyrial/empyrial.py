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
from darts.metrics import mape
import yahoo_fin.stock_info as si
from yahoofinancials import YahooFinancials
from pypfopt import EfficientFrontier, risk_models, expected_returns, HRPOpt, objective_functions
import logging
import warnings
from warnings import filterwarnings

# ------------------------------------------------------------------------------------------

today = dt.date.today()

# ------------------------------------------------------------------------------------------

class Engine:


  def __init__(self,start_date, portfolio, weights=None, benchmark=['SPY'], end_date=today, optimizer=None, max_vol=0.15):
    self.start_date = start_date
    self.end_date = end_date
    self.portfolio = portfolio
    self.weights = weights
    self.benchmark = benchmark
    self.optimizer = optimizer
    self.max_vol = max_vol

    if self.weights==None:
      self.weights = [1.0/len(self.portfolio)]*len(self.portfolio)

    if self.optimizer=="EF":
      self.weights = efficient_frontier(self, perf="False")

    if self.optimizer=="MV":
      self.weights = mean_var(self, vol_max=max_vol, perf="False")

    if self.optimizer=="HRP":
      self.weights = hrp(self, perf="False")
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
          shadow=False)
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

    if prediction_days==None:
      x = 1
      while x/(len(series)+x) < 0.3:
        x+=1
        prediction_days = x

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
  print("Assets returns prediction for the next "+str(prediction_days)+" days (in %)")
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
  print("Portfolio returns prediction for the next "+str(prediction_days)+" days  (in %)")
  display(portfolio_pred.iloc[0])
  

  logger.disabled = False

#---------------------------------------------------------------------
millnames = ['','k','M','B','T']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
#-------------------------------------------------------------------------
def fundlens(my_portfolio, period="annual"):

  appended_data = pd.DataFrame()

  for symbol in my_portfolio.portfolio:

    #loading datas from different sources
    yahoo_financials = YahooFinancials(symbol)
    ticker = yf.Ticker(symbol)
    data= si.get_stats(symbol)
    datas= si.get_financials(symbol)
    financial = yahoo_financials.get_financial_stmts(period, 'balance')
    stats = yahoo_financials.get_key_statistics_data()
    full = yahoo_financials.get_financial_stmts(period, 'cash')


    #tuning functions called depending on which period the user used : quarterly or annual
    if period=="annual":
      name = 'cashflowStatementHistory'
      df = datas['yearly_balance_sheet'] 
    if period=="quaterly":
      name = 'cashflowStatementHistoryQuarterly'
      df = datas['quarterly_balance_sheet']

    #FCF
    try:
      cash_operating = list(full[name][symbol][0].values())[0]['totalCashFromOperatingActivities']
      capx = list(full[name][symbol][0].values())[0]['capitalExpenditures']
      FCF = cash_operating - capx
    except TypeError and KeyError:
      FCF = "NaN"

    #profit margins
    profit_margins = data['Value'].iloc[31]

    #book value
    book_value = yahoo_financials.get_book_value() 

    #operating income
    operating_income = yahoo_financials.get_operating_income()

    #net income
    net_income = yahoo_financials.get_net_income()

    #D/E ratio
    debt_to_equity = data['Value'].iloc[46]


    #total current liabilities
    tot_c_liab = df.iloc[:,0]['totalCurrentLiabilities']

    #total current assets
    tot_c_assets = df.iloc[:,0]['totalCurrentAssets']

    #inventory
    inventory = df.iloc[:,0]['inventory']

    #total liabilities
    tot_liab = df.iloc[:,0]['totalLiab']
  
    #total assets
    tot_assets = df.iloc[:,0]['totalAssets']

    #quick ratio
    try:
      quick_ratio = (tot_c_assets-inventory)/tot_c_liab
    except TypeError:
      quick_ratio = "None"
    
    #total debts
    try:
      tot_debt = df.iloc[:,0]['shortLongTermDebt'] + df.iloc[:,0]['longTermDebt']
    except TypeError:
      tot_debt = "None"

    #debt to asset ratio
    try:
      debt_asset_ratio = tot_debt/tot_assets
    except:
      debt_asset_ratio = "None"

    #working capital
    try:
      working_capital = tot_c_assets - tot_c_liab
    except TypeError:
      working_capital = "None"

    #liquidation
    try:
      liquidation = tot_assets - tot_liab
    except TypeError:
      liquidation = "None"
    
    #market cap
    try:
      s = web.get_quote_yahoo(symbol)['marketCap']
      list(s)
      market_cap = millify(s[0])
    except Exception as e:
      market_cap = "None"

    try:
      controversy = ticker.sustainability.iloc[:,0]['highestControversy']
      social_score = ticker.sustainability.iloc[:,0]['socialScore']
      env_score = ticker.sustainability.iloc[:,0]['environmentScore']
      gov_score = ticker.sustainability.iloc[:,0]['governanceScore']
      esg_perf = ticker.sustainability.iloc[:,0]['esgPerformance']
    except AttributeError:
      pass

    datax = [ ['Market cap', market_cap], ['Current ratio', data['Value'].iloc[47]], ['Quick ratio', quick_ratio], ['Debt ratio', tot_liab/tot_assets],
                                                                                      
            ['Earnings per share', yahoo_financials.get_earnings_per_share()], ['P/E ratio', yahoo_financials.get_pe_ratio()], ['P/B ratio', stats[symbol]['priceToBook']], 
            
            ['P/S ratio', yahoo_financials.get_price_to_sales()], ['Free cash flow ', FCF],

            ['PEG ratio', stats[symbol]['pegRatio']], ['Return on Equity', data['Value'].iloc[34]], ['Return on Asset', data['Value'].iloc[33]], ['EBIT', millify(yahoo_financials.get_ebit())], ['EBITDA', data['Value'].iloc[39]], 
             
            ['Profit margins' , data['Value'].iloc[31]], ['Book value', millify(yahoo_financials.get_book_value())], ['Book value per share' , data['Value'].iloc[48]], ['Debt-to-equity ratio', debt_to_equity], 
             
            ['Debt-to-asset ratio', debt_asset_ratio], ['Net income', millify(net_income)], ['Operating income', millify(operating_income) ], ['Working capital', millify(working_capital) ], ['Liquidation', millify(liquidation) ], 
             
            ['Dividend yield', yahoo_financials.get_dividend_yield()], ['Payout ratio', yahoo_financials.get_payout_ratio()], ['Controversy', controversy], ['Social score', social_score], 
             
            ['Environmental score', env_score], ['Governance score', gov_score], ['ESG perf', esg_perf ]
               
            ]
    dfs = pd.DataFrame(datax, columns=['Attribute', symbol])
    appended_data = pd.concat([appended_data, dfs], axis=1, join='outer')

  appended_data = pd.DataFrame(appended_data)
  display(appended_data)

#--------------------------------------------------------------------------------
def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l
#-------------------------------------------------------------------------------

def graph_opt(my_portfolio, my_weights):
  fig1, ax1 = plt.subplots()
  ax1.pie(my_weights, labels=my_portfolio.portfolio, autopct='%1.1f%%',
          shadow=False)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title("Portfolio's allocation")
  plt.show()

#--------------------------------------------------------------------------
def equal_weighting(my_portfolio):
  return [1.0/len(my_portfolio.portfolio)]*len(my_portfolio.portfolio)
#------------------------------------------------------------------------
def efficient_frontier(my_portfolio, periods="max", perf=True):

  ohlc = yf.download(my_portfolio.portfolio, period=periods, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  df = prices.filter(my_portfolio.portfolio)

  mu = expected_returns.mean_historical_return(df)
  S = risk_models.sample_cov(df)

  #optimize for max sharpe ratio
  ef = EfficientFrontier(mu, S)
  weights = ef.max_sharpe()
  cleaned_weights = ef.clean_weights()
  wts = cleaned_weights.items()

  result = []
  for val in wts:
    a, b = map(list, zip(*[val]))
    result.append(b)
  

  if perf==True:
    pred = ef.portfolio_performance(verbose=True);
  
  return flatten(result)
#-------------------------------------------------------------------------------
def hrp(my_portfolio, periods="max", perf=True):

  ohlc = yf.download(my_portfolio.portfolio, period=periods, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  prices = prices.filter(my_portfolio.portfolio)

  rets = expected_returns.returns_from_prices(prices)
  hrp = HRPOpt(rets)
  hrp.optimize()
  weights = hrp.clean_weights()

  wts = weights.items()

  result = []
  for val in wts:
    a, b = map(list, zip(*[val]))
    result.append(b)
  
  if perf==True:
    hrp.portfolio_performance(verbose=True);

  return flatten(result)
#-----------------------------------------------------------------------------
def mean_var(my_portfolio, vol_max=0.15, periods="max", perf=True):
  
  ohlc = yf.download(my_portfolio.portfolio, period=periods, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  prices = prices.filter(my_portfolio.portfolio)

  mu = expected_returns.capm_return(prices)
  S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

  ef = EfficientFrontier(mu, S)
  ef.add_objective(objective_functions.L2_reg, gamma=0.1) 
  ef.efficient_risk(vol_max)
  weights = ef.clean_weights()

  wts = weights.items()

  result = []
  for val in wts:
    a, b = map(list, zip(*[val]))
    result.append(b)

  if perf==True:
    ef.portfolio_performance(verbose=True);

  return flatten(result)
#--------------------------------------------------------------------------------
def optimizer(my_portfolio, method, vol_max=0.15, periods="max"):

  returns1 = get_returns(my_portfolio.portfolio, my_portfolio.weights, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
  creturns1 = (returns1 + 1).cumprod()

  if method == "EF":
    wts = efficient_frontier(my_portfolio, periods)
  
  if method == "HRP":
    wts = hrp(my_portfolio, periods)

  if method == "MV":
    wts = mean_var(my_portfolio, vol_max, periods)

  if optimizer== "EW":
    wts = equal_weighting(my_portfolio, periods)

  print(wts)
  print("\n")

  graph_opt(my_portfolio, wts)

  print("\n")

  returns2 = get_returns(my_portfolio.portfolio, wts, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
  creturns2 = (returns2 + 1).cumprod()

  plt.figure(figsize=(12,5))
  plt.xlabel("Portfolio's cumulative return")

  ax1 = creturns1.plot(color='blue', label='Without optimization')
  ax2 = creturns2.plot(color='red', label='With optimization')

  h1, l1 = ax1.get_legend_handles_labels()
  h2, l2 = ax2.get_legend_handles_labels()


  plt.legend(l1+l2, loc=2)
  plt.show()
