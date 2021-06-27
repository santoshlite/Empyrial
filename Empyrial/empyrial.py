import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as web
import datetime as dt
from empyrical import*
import quantstats as qs
from pypfopt import EfficientFrontier, risk_models, expected_returns, HRPOpt, objective_functions
from IPython.display import display
from pypfopt import EfficientFrontier, risk_models, expected_returns, HRPOpt, objective_functions
import matplotlib.pyplot as plt
import copy
import yfinance as yf


# ------------------------------------------------------------------------------------------

today = dt.date.today()

# ------------------------------------------------------------------------------------------

class Engine:


  def __init__(self,start_date, portfolio, weights=None, rebalance=None, benchmark=['SPY'], end_date=today, optimizer=None, max_vol=0.15):
    self.start_date = start_date
    self.end_date = end_date
    self.portfolio = portfolio
    self.weights = weights
    self.benchmark = benchmark
    self.optimizer = optimizer
    self.max_vol = max_vol
    self.rebalance = rebalance

    if self.weights==None:
      self.weights = [1.0/len(self.portfolio)]*len(self.portfolio)

    if self.optimizer=="EF":
      self.weights = efficient_frontier(self, perf="False")

    if self.optimizer=="MV":
      self.weights = mean_var(self, vol_max=max_vol, perf="False")

    if self.optimizer=="HRP":
      self.weights = hrp(self, perf="False")
      
    if self.rebalance!=None:
      self.rebalance = make_rebalance(self.start_date, self.end_date, self.optimizer, self.portfolio, self.rebalance)
    
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

#reformat
def creturns(stocks,wts=1, period="max", benchmark= None, plot=True, pricing="Adj Close", trading_year_days=252, end_date = today):
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
    df = web.DataReader(stocks, data_source='yahoo', start = "1980-01-01", end= end_date)[pricing]
    if benchmark != None:
      df2 = web.DataReader(benchmark, data_source='yahoo', start = "1980-01-01", end= end_date)[pricing]
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
#initialize a variable that we be set to false
def empyrial(my_portfolio, rf=0.0, sigma_value=1, confidence_value=0.95, rebalance=False):

  #standard emyrial output
  if rebalance == False:
      
      #standard returns calculation
      returns = get_returns(my_portfolio.portfolio, my_portfolio.weights, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
      
  #when we want to do the rebalancing
  if rebalance == True:
      
      print("")
      print('rebalance hit')
      
      #we want to get the dataframe with the dates and weights
      rebalance_schedule = my_portfolio.rebalance
      
      #then want to make a list of the dates and start with our first date
      dates = [my_portfolio.start_date]
      
      #then our rebalancing dates into that list 
      dates = dates + rebalance_schedule.columns.to_list()
      
      #this will hold returns
      returns = pd.Series()
      
      #then we want to be able to call the dates like tuples
      for i in range(len(dates) - 1):
          
          #get our weights
          weights = rebalance_schedule[str(dates[i+1])]
          
          #then we want to get the returns
          add_returns = get_returns(my_portfolio.portfolio, weights, start_date = dates[i], end_date = dates[i+1])
          
          #then append those returns
          returns = returns.append(add_returns)
  

  benchmark = get_returns(my_portfolio.benchmark, wts=[1], start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)

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

  empyrial.SR = SR

  CR =  qs.stats.calmar(returns)
  CR = CR.tolist()
  CR = str(round(CR,2))

  empyrial.CR = CR

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
  empyrial.df = data
  
  if rebalance == True:
      df

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

  empyrial.returns = returns
  empyrial.benchmark = benchmark
  empyrial.CAGR = CAGR
  empyrial.CUM = CUM
  empyrial.VOL = VOL
  empyrial.SR = SR
  empyrial.win_ratio = win_ratio
  empyrial.CR = CR
  empyrial.IR = IR
  empyrial.STABILITY = STABILITY
  empyrial.MD = MD
  empyrial.SOR = SOR
  empyrial.SK = SK
  empyrial.KU = KU
  empyrial.TA = TA
  empyrial.CSR = CSR
  empyrial.VAR = VAR
  empyrial.AL = AL
  empyrial.BTA = BTA


  return qs.plots.returns(returns,benchmark, cumulative=True), qs.plots.monthly_heatmap(returns), qs.plots.drawdown(returns), qs.plots.drawdowns_periods(returns), qs.plots.rolling_volatility(returns), qs.plots.rolling_sharpe(returns), qs.plots.rolling_beta(returns, benchmark)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
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

def graph_opt(my_portfolio, my_weights, pie_size, font_size):
  fig1, ax1 = plt.subplots()
  fig1.set_size_inches(pie_size, pie_size)
  ax1.pie(my_weights, labels=my_portfolio, autopct='%1.1f%%',
          shadow=False)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.rcParams['font.size'] = font_size
  plt.title("Portfolio's allocation")
  plt.show()
#--------------------------------------------------------------------------
def equal_weighting(my_portfolio):
  return [1.0/len(my_portfolio.portfolio)]*len(my_portfolio.portfolio)
#------------------------------------------------------------------------
def efficient_frontier(my_portfolio, perf=True):

  #changed to take in desired timeline, the problem is that it would use all historical data
  ohlc = yf.download(my_portfolio.portfolio, start = my_portfolio.start_date, end = my_portfolio.end_date, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  df = prices.filter(my_portfolio.portfolio)
  
  #sometimes we will pick a date range where company isn't public we can't set price to 0 so it has to go to 1
  df = df.fillna(1)

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
def hrp(my_portfolio, perf=True):

  #changed to take in desired timeline, the problem is that it would use all historical data
  ohlc = yf.download(my_portfolio.portfolio, start = my_portfolio.start_date, end = my_portfolio.end_date, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  prices = prices.filter(my_portfolio.portfolio)
  
  #sometimes we will pick a date range where company isn't public we can't set price to 0 so it has to go to 1
  prices = prices.fillna(1)

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
def mean_var(my_portfolio, vol_max=0.15, perf=True):
  
  #changed to take in desired timeline, the problem is that it would use all historical data
  ohlc = yf.download(my_portfolio.portfolio, start = my_portfolio.start_date, end = my_portfolio.end_date, progress=False)
  prices = ohlc["Adj Close"].dropna(how="all")
  prices = prices.filter(my_portfolio.portfolio)
  
  #sometimes we will pick a date range where company isn't public we can't set price to 0 so it has to go to 1
  prices = prices.fillna(1)

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
def optimizer(my_portfolio, method, vol_max=0.15, pie_size=5, font_size=14):

  
  returns1 = get_returns(my_portfolio.portfolio, my_portfolio.weights, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
  creturns1 = (returns1 + 1).cumprod()

  port = copy.deepcopy(my_portfolio.portfolio)

  if method == "EF":
    wts = efficient_frontier(my_portfolio)
  
  if method == "HRP":
    wts = hrp(my_portfolio)

  if method == "MV":
    wts = mean_var(my_portfolio, vol_max)

  if optimizer== "EW":
    wts = equal_weighting(my_portfolio)

  print(wts)
  print("\n")

  indices = [i for i, x in enumerate(wts) if x == 0.0]

  while 0.0 in wts: wts.remove(0.0)



  for i in sorted(indices, reverse=True):
    del port[i]

    
  graph_opt(port, wts, pie_size, font_size)

  print("\n")

  returns2 = get_returns(port, wts, start_date=my_portfolio.start_date,end_date=my_portfolio.end_date)
  creturns2 = (returns2 + 1).cumprod()

  plt.figure(figsize=(20,10))
  plt.xlabel("Portfolio's cumulative return")

  ax1 = creturns1.plot(color='blue', label='Without optimization')
  ax2 = creturns2.plot(color='red', label='With optimization')

  h1, l1 = ax1.get_legend_handles_labels()
  h2, l2 = ax2.get_legend_handles_labels()


  plt.legend(l1+l2, loc=2)
  plt.show()
#-------------------------------------------------------------------------------------------------

def check_schedule(rebalance):
    
    #this is the list of acceptable rebalancing schedules
    acceptable_schedules = ["6mo","1y","2y", "quarterly", "monthly"]
    
    #we want to loop through the acceptable schedules to see if the user inputted the right rebalance
    for i in acceptable_schedules:
        
        #want to make this a try with an error if it is incorrect
        
        #check if the inputted rebalance is an acceptable
        if i == rebalance:
            
            #if the inputted rebalancing is in the acceptable schedule set to true
            valid_schedule = True
            return valid_schedule
            break
        
        #if the inputted value isn't in our accepted rebalancing schedule
        else:
            valid_schedule = False
         
    #return that back
    return valid_schedule

#--------------------------------------------------------------------------------
def valid_range(start_date, end_date, rebalance):
    
    #make the start date to a datetime
    start_date = dt.datetime.strptime(start_date, "%Y-%M-%d")
    
    #have to make end date a datetime because strptime is not supported for date
    end_date = dt.datetime(end_date.year, end_date.month, end_date.day)
    
    #gets the number of days
    days = (end_date - start_date).days
    
    #all of this is for checking the length
    
    if rebalance == "6mo" and days <= (int(365/2)):
        raise KeyError("Date Range does not encompass rebalancing interval")
        
    if rebalance == "1y" and days <= int(365):
        raise KeyError("Date Range does not encompass rebalancing interval")
        
    if rebalance == "2y" and days <= int(365 * 2):
        raise KeyError("Date Range does not encompass rebalancing interval")
        
    if rebalance == "quarterly" and days <= int(365 / 4):
        raise KeyError("Date Range does not encompass rebalancing interval")
        
    if rebalance == "monthyl" and days <= int(30):
        raise KeyError("Date Range does not encompass rebalancing interval")
        
    #we will needs these dates later on so we'll return them back
    return start_date, end_date

#--------------------------------------------------------------------------------
def get_date_range(start_date, end_date, rebalance):
    
    #this will keep track of the rebalancing dates and we want to start on the first date
    rebalance_dates = [start_date]
    input_date = start_date
    
    if rebalance == "6mo":
        
        #run for an arbitrarily large number we'll resolve this by breaking when we break the equality
        for i in range(1000):
        
            #this gives us the future date
            input_date = input_date + dt.timedelta(days = 365/2)
            
            #then we want to compare dates
            if input_date < end_date:
                
                #if the dates are less than the final date we put that into our date list 
                rebalance_dates.append(input_date)
              
            #when the rebalance date is greater than our final date
            else:
                break

    if rebalance == "1y":
        
        #run for an arbitrarily large number we'll resolve this by breaking when we break the equality
        for i in range(1000):
        
            #this gives us the future date
            input_date = input_date + dt.timedelta(days = 365)
            
            #then we want to compare dates
            if input_date < end_date:
                
                #if the dates are less than the final date we put that into our date list 
                rebalance_dates.append(input_date)
              
            #when the rebalance date is greater than our final date
            else:
                break

    if rebalance == "2y":
        
        #run for an arbitrarily large number we'll resolve this by breaking when we break the equality
        for i in range(1000):
        
            #this gives us the future date
            input_date = input_date + dt.timedelta(days = 365 * 2)
            
            #then we want to compare dates
            if input_date < end_date:
                
                #if the dates are less than the final date we put that into our date list 
                rebalance_dates.append(input_date)
              
            #when the rebalance date is greater than our final date
            else:
                break
            
    if rebalance == "quarterly":
        
        #run for an arbitrarily large number we'll resolve this by breaking when we break the equality
        for i in range(1000):
        
            #this gives us the future date
            input_date = input_date + dt.timedelta(days = 365 / 4)
            
            #then we want to compare dates
            if input_date < end_date:
                
                #if the dates are less than the final date we put that into our date list 
                rebalance_dates.append(input_date)
              
            #when the rebalance date is greater than our final date
            else:
                break
            
    if rebalance == "monthly":
        
        #run for an arbitrarily large number we'll resolve this by breaking when we break the equality
        for i in range(1000):
        
            #this gives us the future date
            input_date = input_date + dt.timedelta(days = 30)
            
            #then we want to compare dates
            if input_date < end_date:
                
                #if the dates are less than the final date we put that into our date list 
                rebalance_dates.append(input_date)
              
            #when the rebalance date is greater than our final date
            else:
                break
    
    #then we want to return those dates
    return rebalance_dates

#--------------------------------------------------------------------------------
def make_rebalance(start_date, end_date, optimizer, portfolio_input, rebalance):
    
    print("")
    print("If failed downloads appear they occur because you are querying for a stock that isn't listed for the desired range, no worries we've worked it out.")
    
    #makes sure that the value passed through for rebalancing is a valid one
    valid_schedule = check_schedule(rebalance)
        
    if valid_schedule == False:
        raise KeyError("Not an accepted rebalancing schedule")
        
    #this checks to make sure that the date range given works for the rebalancing
    start_date, end_date = valid_range(start_date, end_date, rebalance)
    
    #this function will get us the specific dates
    dates = get_date_range(start_date, end_date, rebalance)
    
    #we are going to make columns with the end date and the weights
    columns = ["end_date"] + portfolio_input
    
    #then make a dataframe with the index being the tickers
    output_df = pd.DataFrame(index = portfolio_input)
    
    #I don't think I need to make a function to make sure the date we have is a trading day because yfinance will fix that 
    
    for i in range(len(dates) - 1):
        
        portfolio = Engine(
          start_date = dates[0],
          end_date = dates[i+1],
          portfolio = portfolio_input,
          optimizer = "{}".format(optimizer))

        output_df["{}".format(dates[i+1])] = portfolio.weights
        
    
    #we have to run it one more time to get what the optimization is for up to today's date
    portfolio = Engine(
      start_date = dates[0],
      portfolio = portfolio_input,
      optimizer = "{}".format(optimizer))
    
    output_df['{}'.format(today)] = portfolio.weights
    
    return output_df
