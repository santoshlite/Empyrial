import yfinance as yf
import yahoo_fin.stock_info as si
from yahoofinancials import YahooFinancials
import pandas_datareader as web
import pandas as pd
from IPython.display import display
import math

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
    try:
      profit_margins = data['Value'].iloc[31]
    except KeyError:
      profit_margins = None

    #book value
    try:
      book_value = yahoo_financials.get_book_value() 
    except KeyError:
      book_value = None

    #operating income
    try:
      operating_income = yahoo_financials.get_operating_income()
    except KeyError:
      operating_income=None

    #net income
    try:
      net_income = yahoo_financials.get_net_income()
    except KeyError:
      net_income = None

    #D/E ratio
    try:
      debt_to_equity = data['Value'].iloc[46]
    except KeyError:
      debt_to_equity = None


    #total current liabilities
    tot_c_liab = df.iloc[:,0]['totalCurrentLiabilities']

    #total current assets
    try:
      tot_c_assets = df.iloc[:,0]['totalCurrentAssets']
    except KeyError:
      tot_c_assets = None   

    #inventory
    try:
      inventory = df.iloc[:,0]['inventory']
    except KeyError:
      inventory = None

    #total liabilities
    try:
      tot_liab = df.iloc[:,0]['totalLiab']
    except KeyError:
      tot_liab = None
  
    #total assets
    try:
      tot_assets = df.iloc[:,0]['totalAssets']
    except KeyError:
      tot_assets = None

    #quick ratio
    try:
      quick_ratio = (tot_c_assets-inventory)/tot_c_liab
    except TypeError:
      quick_ratio = "None"
    
    #total debts
    try:
      shortlongtermdebt = df.iloc[:,0]['shortLongTermDebt']
    except KeyError:
      shortlongtermdebt = None
      
    try:
      longtermdebt = df.iloc[:,0]['longTermDebt']
    except KeyError:
      longtermdebt = None

    try:
      tot_debt = shortlongtermdebt + longtermdebt
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
    except TypeError:
      controversy = "None"

    try:
      social_score = ticker.sustainability.iloc[:,0]['socialScore']
    except TypeError:
      social_score = "None"

    try:
      env_score = ticker.sustainability.iloc[:,0]['environmentScore']
    except TypeError:
      env_score = "None"

    try:
      gov_score = ticker.sustainability.iloc[:,0]['governanceScore']
    except TypeError:
      gov_score = "None"
    
    try:
      esg_perf = ticker.sustainability.iloc[:,0]['esgPerformance']
    except TypeError:
      esg_perf = "None"

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
