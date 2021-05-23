# Projekt: Analyse COVID 19 - data from Johns-Hopkins-University
# Source: Johns-Hopkins-University/ Github-Repository: https://github.com/CSSEGISandData/COVID-19

# Zweck:    Check, welche Country/Region - Province/States auf der LUT UID_ISO_FIPS_LookUp_Table.csv
#           in den time-series Global und US vorkommen.
# Stand:    16.01.2021
# Status:   work in progress


import os
import pandas as pd
import datetime

# configuration ********************************************************************************************************
root_git = "C:/Users/Work/Documents/GitHub/COVID-19/csse_covid_19_data/"
root_out = "C:/Users/Work/Desktop/Privat/corona/03_Johns_Hopkins/"

# source folder for raw data
path_timeseries = root_git + "csse_covid_19_time_series/"
print("\n" * 4, "raw data are in folder : ", path_timeseries)

path_lut = root_git

# output folder
path_out = root_out + "02_Exploration/"
print("output is redirected to : ", path_out)

# import data **********************************************************************************************************
# lookup-tables to import
DataIn_PopulationWorld = "UID_ISO_FIPS_LookUp_Table.csv"
infile = os.path.join(path_lut, DataIn_PopulationWorld)
df_Population = pd.read_csv(infile, converters={'code3': str, 'FIPS': str}, encoding='UTF8')
df_Population.rename(columns=({'Long_': 'Long'}), inplace=True)

# time-series to import
DataIn_Files = ['time_series_covid19_deaths_US.csv',
                'time_series_covid19_deaths_global.csv']

for DataIn_File in DataIn_Files:
    infile = os.path.join(path_timeseries, DataIn_File)

    if 'US' in DataIn_File:
        # US-Daten
        print(datetime.datetime.now(), ': Importiere ', infile)
        # step1: read as dataframe
        df_US = pd.read_csv(infile, decimal='.', sep=',', converters={'FIPS': str, 'UID': str})

    else:
        print(datetime.datetime.now(), ': Importiere ', infile)
        # step1: file als dataframe einlesen
        df_Global = pd.read_csv(infile)

cols_to_delete = list(range(12, len(df_US.columns)))
df_US.drop(df_US.columns[cols_to_delete], axis=1, inplace=True)
df_US.rename(columns=({'Long_': 'Long'}), inplace=True)

cols_to_delete = list(range(4, len(df_Global.columns)))
df_Global.drop(df_Global.columns[cols_to_delete], axis=1, inplace=True)
df_Global.rename(columns=({'Province/State': 'Province_State', 'Country/Region': 'Country_Region'}), inplace=True)
# zeilenweise über df_Global iterieren, Spalten Province_State und Country_Region verknüpfen, NaN ignorieren.
df_Global['Combined_Key'] = df_Global[['Province_State', 'Country_Region']].apply(lambda x: ', '.join(x.dropna()),
                                                                                  axis=1)

sources = {'UID_ISO_FIPS': df_Population,
           'US': df_US,
           'Global': df_Global}

for name, df in sources.items():
    df['source'] = name
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    print(cols)
    # df = df.reindex(columns=[cols])
    df = df[cols]

print('df_Population - dimensions: ', df_Population.shape, '\n', 'df_Population  number of rows: ', '\n',
      df_Population.count(axis=0))
print('df_Global - dimensions: ', df_Global.shape, '\n', 'df_Global  number of rows: ', df_Global.count(axis=0))
print('df_US - dimensions: ', df_US.shape, '\n', 'df_US  number of rows: ', df_US.count(axis=0))

df_Global_US = pd.concat([df_Global, df_US], ignore_index=True, sort=False)
df_Global_US_Population = pd.merge(df_Population, df_Global_US, on=['Combined_Key'], how='left')

DataOut_Regions = os.path.join(path_out, 'Regions.xlsx')

with pd.ExcelWriter(DataOut_Regions) as writer:
    df_Population.to_excel(writer, sheet_name='UID_ISO_FIPS', index=False, header=True)
df_US.to_excel(writer, sheet_name='US', index=False, header=True)
df_Global.to_excel(writer, sheet_name='Global', index=False, header=True)
df_Global_US.to_excel(writer, sheet_name='Global + US', index=False, header=True)
df_Global_US_Population.to_excel(writer, sheet_name='merged data', index=False, header=True)

#######################################################################################################################
##### 02_Tests
obj_shape = df_US.shape

# print('df_Global - dimensions: {0}'.format(df_Global.shape))
obj_count = df_US.count(axis=0)
for element in obj_count:
    print('df_Global  labels: {0} Werte {1}'.format(element, element.values))

obj_count_list = obj_count.tolist()
obj_count_frame = obj_count.to_frame()

print(obj_count.index.values)
print(obj_count.values)
print(type(obj_count.index))
print(obj_count.index)
print(obj_count.index.tolist())

for key, value in obj_count.items:
    print(key, value)

for element in obj_count:
    print(element)

for element in obj_count.index.tolist():
    print(element)

for element in obj_count_frame:
    print(element)

print(obj_count_frame.index.values)
print(obj_count_frame.values)

print('df_Global  labels: {0} Werte {1}'.format(obj_count.index.tolist(), obj_count.values))
print('df_Global  labels: {0} Werte {1}'.format(obj_count_frame, obj_count.values))
