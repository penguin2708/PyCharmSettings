# COVID 19 - data (time series data, population data)
# Region: US
# Source: Johns-Hopkins-University/ Github-Repository: https://github.com/CSSEGISandData/COVID-19

# Import time series raw data (3 datasets)
# Transformationen und Zusammenführung in einen Datensatz.

# Stand: 05.05.2020 -- international version
# Status: work in progress


import os
import pandas as pd
import datetime

# change working directory
# The current working directory is the folder in which the Python script is operating.
cwd = os.getcwd()
print("current working directory : ", cwd)

# source folder for raw data
path_in = "C:/Users/Work/Documents/GitHub/COVID-19/csse_covid_19_data"
os.chdir(path_in)
cwd = os.getcwd()
print("raw data are in folder : ", cwd)

# source folder for Lookup-Tables
path_lut = "C:/Users/Work/Desktop/corona/02_Lookup_Tables"

# output folder
path_out = r'C:\Users\Work\Desktop\corona\03_Johns_Hopkins\01_Daten'
print("output is redirected to : ", path_out)

########################################################################################################################
# create dataset 'US.csv'

# list of files to import
files_US = ['csse_covid_19_time_series/time_series_covid19_deaths_US.csv',
            'csse_covid_19_time_series/time_series_covid19_confirmed_US.csv']

# # Fall-Klassifizierung.
# types = ['confirmed',
#          'deaths',
#          'recovered']


# leeren Dataframe erzeugen
df_wide = pd.DataFrame()

for file in files_US:
    # step1: read as dataframe
    df_in = pd.read_csv(file, decimal='.', sep=',', converters={'FIPS': str, 'UID': str})

    # remove all characters at the end starting with '.'
    df_in['UID'] = df_in['UID'].str.split('.', n=-1, expand=True)[0]
    df_in['FIPS'] = df_in['FIPS'].str.split('.', n=-1, expand=True)[0]

    # step2: Typ des Datensatzes ermitteln, spalte 'casetype' hinzufügen und Typ zuweisen

    # if type = deaths: extract population data, remove column 'Population' and write 'FIPS' and 'Population' to separate file
    # dropping passed columns

    #  "deaths" file version contains population data
    if 'deaths' in file:
        df_pop_us = df_in[['FIPS', 'Population']]
        outfile_name = 'Population_US.csv'
        outfile = os.path.join(path_out, outfile_name)
        df_pop_us.to_csv(outfile, index=True, header=True, encoding='UTF8', sep=';')

        df_in['Casetype'] = 'deaths'

    else:
        df_in['Casetype'] = 'confirmed'

    df_in.rename(columns={'Long_': 'Long'}, inplace=True)

    # step4: Dataframes hintereinanderhängen
    df_wide = df_wide.append(df_in)

    # step3: Entpivotisieren des Dataframes
    df_long = pd.melt(df_wide,
                      id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region',
                               'Lat',
                               'Long', 'Combined_Key', 'Population', 'Casetype'], var_name=['Date'],
                      value_name='Cases')

# export as csv
outfile = 'US.csv'
outfile = os.path.join(path_out, outfile)
df_long.to_csv(outfile, index=True, header=True, encoding='UTF8', sep=';')

# population world
population_world_in = "UID_ISO_FIPS_LookUp_Table.csv"
population_world_out = "Population_World.csv"

infile = os.path.join(path_in, population_world_in)
df_pop_world = pd.read_csv(infile, converters={'code3': str, 'FIPS': str})

df_pop_world['code3'] = df_pop_world['code3'].str.split('.', n=-1, expand=True)[0]
df_pop_world['FIPS'] = df_pop_world['FIPS'].str.split('.', n=-1, expand=True)[0]
df_pop_world.rename(columns={"Long_": "Long"}, inplace=True)
r, c = df_pop_world.shape

lut_countries = "Länderliste.xlsx"
infile = os.path.join(path_lut, lut_countries)
df_countries = pd.read_excel(infile, sheet_name="countries")
r, c = df_countries.shape

df_pop_world = pd.merge(df_pop_world, df_countries, left_on='Country_Region', right_on='country', how='left')
r, c = df_pop_world.shape

outfile = os.path.join(path_out, population_world_out)
df_pop_world.to_csv(outfile, index=True, header=True, encoding='UTF8')
