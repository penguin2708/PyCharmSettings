# Stand:    19.03.2021
# Status:   dev

import yfinance as yf
import pandas as pd
from pandas import ExcelWriter
import os
import datetime as dt
from datetime import date


def calendar(start, end):
    """ Erzeuge alle Daten zwischen day1 und day2 nach Tagen;
    Gib einen Dataframe, eine *.csv- und eine *.xlsx-Datei zurück """
    # start = dt.datetime.strptime(day1, "%d.%m.%Y")
    # end = dt.datetime.strptime(day2, "%d.%m.%Y")
    date_generated = [start + dt.timedelta(days=x) for x in range(0, (end.date() - start.date()).days)]

    # for date in date_generated:
    #     print(date.strftime("%d.%m.%Y"))

    df = pd.DataFrame(date_generated)
    df.columns = ['Date']
    # df['Date'] = pd.to_date(df['Date'])
    # df['Date'] = df['Date'].astype(str)
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df.index = df.index + 1
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # Output
    outpath = r'C:\Users\Work\OneDrive - Busch Analytics\Desktop'
    file = 'calendar.xlsx'
    outfile_xls = os.path.join(outpath, file)
    outfile_csv = os.path.join(outpath, 'calendar.csv')
    writer = ExcelWriter(outfile_xls)

    df.to_excel(writer, 'calendar')
    df.to_csv(outfile_csv, index=True, header=True, index_label='rownumber', encoding='UTF8',
              decimal=",",
              sep=";")

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    return df


def map_symbols_to_calendar(symbols):
    df_ticker_symbols = pd.DataFrame(symbols)
    df_ticker_symbols.columns = ['Ticker']
    df_ticker_symbols['key'] = 1

    df_calendar = calendar(firstday, CurrentDate)
    df_calendar['key'] = 1

    df_alldaysxticker = pd.merge(df_calendar, df_ticker_symbols, on='key').drop("key", 1)
    return df_alldaysxticker


def fetch_historical_data(symbols):
    df = pd.DataFrame()
    # Beachte: Datum = Index, daher nicht unique, da mehrere symbols.
    for symbol in symbols:
        df_symbols = yf.download(symbol,
                                 start=firstday,
                                 end=CurrentDate,
                                 progress=False)
        df_symbols['Ticker'] = symbol
        df = df.append(df_symbols)
    return df


def prepare_data(df):
    df['Date'] = df.index  # Index in Spalte verwandeln
    # df['Date'] = df['Date'].apply(pd.to_datetime).dt.date
    df['Date'] = df['Date'].astype(str)
    df.reset_index(drop=True, inplace=True)  # eindeutigen Index von 0 - n herstellen.

    df['Close chg %'] = df.groupby('Ticker')['Close'].diff().fillna(0) / df.groupby('Ticker')[
        'Close'].shift(
        1)
    df['prev. Close'] = df.groupby('Ticker')['Close'].shift(1)

    # weitere Spalten hinzufügen.
    df['Index'] = df['Ticker'].map(dictSymbols)
    df['Category'] = df['Ticker'].map(dictCategory)
    return df


def output_result(df):
    """Schreibe Ergebnis als lange und als pivotisierte Version in je eine csv-Datei"""
    outfile1 = os.path.join(path, file1)
    df.to_csv(outfile1, index=True, header=True, index_label='index', encoding='UTF8', decimal=',', sep=';')

    # Pivotisierung/ Zweck: Datenbasis für eine Korrelationsanalyse
    table = pd.pivot_table(df, values='Close', index=['Date'],
                           columns=['Index'], fill_value=None)

    table = table.reset_index()  # alter Index wird zu neuer Spalte, neuer Index ist von 0 bis 2 durchnummeriert;

    outfile2 = os.path.join(path, file2)
    table.to_csv(outfile2, index=True, header=True, index_label='index', encoding='UTF8', decimal=',', sep=';')


#
#
# Konfiguration
root = r'C:\Users\Work\OneDrive - Busch Analytics\Desktop\Privat'
folder = r'\StockIndices_V2'
path = root + folder
file1 = 'StockData.csv'
file2 = 'StockDataPivot.csv'
firstday = dt.datetime.strptime("2000-01-01", '%Y-%m-%d')
CurrentDate = dt.datetime.today()
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


df_data = fetch_historical_data(tickerSymbols)
df_data = prepare_data(df_data)
df_AllDaysXTicker = map_symbols_to_calendar(tickerSymbols)
df_data1 = pd.merge(df_AllDaysXTicker, df_data, on=['Date', 'Ticker'], how='left')
output_result(df_data1)