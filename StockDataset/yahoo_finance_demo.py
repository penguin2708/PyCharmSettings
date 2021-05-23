import yfinance as yf
import pandas as pd
import os
import datetime
import lxml

# define the ticker symbol
tickerSymbol = '^GSPC'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
type(tickerData)

df_tickerDate = pd.DataFrame(tickerData)

# diverse Metadaten
tickerData.ticker
tickerData.get_isin()
tickerData.info
print(tickerData.get_info())

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-6-4')

# see your data
tickerDf
#
#
#
#