import datetime as dt
import pandas as pd
from pandas import ExcelWriter
import os

# check the current directory
cwd = os.getcwd()
print(cwd)

day1 = "01.01.1990"
day2 = "31.12.2059"


def calendar(day1, day2):
    """ Erzeuge alle Daten zwischen day1 und day2 nach Tagen;
    Gib einen Dataframe, eine *.csv- und eine *.xlsx-Datei zurück """
    start = dt.datetime.strptime(day1, "%d.%m.%Y")
    end = dt.datetime.strptime(day2, "%d.%m.%Y")
    date_generated = [start + dt.timedelta(days=x) for x in range(0, (end - start).days)]

    # for date in date_generated:
    #     print(date.strftime("%d.%m.%Y"))

    df_calendar = pd.DataFrame(date_generated)
    df_calendar.columns = ['Date']
    df_calendar['Day'] = df_calendar['Date'].dt.day
    df_calendar['Month'] = df_calendar['Date'].dt.month
    df_calendar['Year'] = df_calendar['Date'].dt.year
    df_calendar.index = df_calendar.index + 1
    df_calendar['Date'] = df_calendar['Date'].dt.strftime('%d.%m.%Y')

    # Output
    outpath = r'C:\Users\Work\Desktop'
    file = 'calendar.xlsx'
    outfile_xls = os.path.join(outpath, file)
    outfile_csv = os.path.join(outpath, 'calendar.csv')
    writer = ExcelWriter(outfile_xls)

    df_calendar.to_excel(writer, 'calendar')
    df_calendar.to_csv(outfile_csv, index=True, header=True, index_label='rownumber', encoding='UTF8',
                       decimal=",",
                       sep=";")

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    return df_calendar


calendar(day1, day2)
