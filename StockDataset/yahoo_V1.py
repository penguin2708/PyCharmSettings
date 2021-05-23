# Stand:    26.02.2021
# Status:   dev

import yfinance as yf
import pandas as pd
import os
import datetime

tickerSymbols = ['^GSPC', '^IXIC', '^DJI', '^VIX', '^FTSE', '^GDAXI', '^STOXX50E', '^N225', '^HSI', '^RLV', '^RLG',
                 '^KS11', 'AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT', 'NFLX', 'DX-Y.NYB', 'EURUSD=X', 'USDEUR=X', '^TNX']

dictSymbols = {
    '^GSPC': 'S&P 500',
    '^IXIC': 'NASDAQ Composite',
    '^DJI': 'Dow Jones Industrial Average',
    '^FTSE': 'FTSE 100',
    '^GDAXI': 'DAX Performance Index',
    '^STOXX50E': 'ESTX 50 PR.EUR',
    '^N225': 'Nikkei 225',
    '^HSI': 'HANG SENG INDEX',
    '^RLV': 'Russell 1000 Value',
    '^RLG': 'Russell 1000 Growth',
    '^KS11': 'KOSPI Composite Index',
    '^VIX': 'CBOE Volatility Index',
    'AAPL': 'Apple',
    'AMZN': 'Amazon',
    'FB': 'Facebook',
    'GOOGL': 'Google',
    'MSFT': 'Microsoft',
    'NFLX': 'Netflix',
    'DX-Y.NYB': 'Dollar-Index',
    'EURUSD=X': 'EURUSD',
    'USDEUR=X': 'USDEUR',
    '^TNX': 'Treasury Yield 10 Years'}
#
# Kategorien
#
dictCategory = {'AAPL': 'Share',
                'AMZN': 'Share',
                'FB': 'Share',
                'GOOGL': 'Share',
                'MSFT': 'Share',
                'NFLX': 'Share',
                '^DJI': 'Index',
                '^FTSE': 'Index',
                '^GDAXI': 'Index',
                '^GSPC': 'Index',
                '^HSI': 'Index',
                '^IXIC': 'Index',
                '^N225': 'Index',
                '^KS11': 'Index',
                '^RLG': 'Indicator',
                '^RLV': 'Indicator',
                '^STOXX50E': 'Index',
                '^VIX': 'Indicator',
                'DX-Y.NYB': 'Currencies',
                'EURUSD=X': 'Currencies',
                'USDEUR=X': 'Currencies',
                '^TNX': 'Bond'}
#
# print(category)
# category.keys()
# category.values()

#
#
#
path = r'C:\Users\Work\OneDrive - Busch Analytics\Desktop\Privat\StockIndices_V1'
file1 = 'StockData.csv'
file2 = 'StockDataPivot.csv'

data = pd.DataFrame()

CurrentDate = datetime.datetime.today().strftime('%Y-%m-%d')

# Beachte: Datum = Index, daher nicht unique, da mehrere symbols.
for symbol in tickerSymbols:
    df = yf.download(symbol,
                     start='2000-01-01',
                     end=CurrentDate,
                     progress=False)
    df['Ticker'] = symbol
    data = data.append(df)

data['Date'] = data.index  # Index in Spalte verwandeln
data['Date'] = data['Date'].apply(pd.to_datetime).dt.date
data.reset_index(drop=True, inplace=True)  # eindeutigen Index von 0 - n herstellen.

data['Close chg %'] = data.groupby('Ticker')['Close'].diff().fillna(0) / data.groupby('Ticker')['Close'].shift(1)
data['prev. Close'] = data.groupby('Ticker')['Close'].shift(1)

# weitere Spalten hinzufügen.
data['Index'] = data['Ticker'].map(dictSymbols)
data['Category'] = data['Ticker'].map(dictCategory)

outfile1 = os.path.join(path, file1)
data.to_csv(outfile1, index=True, header=True, index_label='index', encoding='UTF8', decimal=',', sep=';')

# Pivotisierung/ Zweck: Datenbasis für eine Korrelationsanalyse
table = pd.pivot_table(data, values='Close', index=['Date'],
                       columns=['Index'], fill_value=None)

table = table.reset_index()  # alter Index wird zu neuer Spalte, neuer Index ist von 0 bis 2 durchnummeriert;

outfile2 = os.path.join(path, file2)
table.to_csv(outfile2, index=True, header=True, index_label='index', encoding='UTF8', decimal=',', sep=';')
