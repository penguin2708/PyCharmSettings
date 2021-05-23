# COVID 19 - data (time series data, population data)
# Region: US, global
# Source: Johns-Hopkins-University/ Github-Repository: https://github.com/CSSEGISandData/COVID-19

# Import time series raw data
# Transformationen und Zusammenführung in einen Datensatz.

# Stand: 03.10.2020
# Status: work in progress


import os
import pandas as pd
import datetime
import csv


def set_first_value(df_x):
    df_x.at[df_x.index[0], 'new cases'] = df_x.at[df_x.index[0], 'Cases']
    # oder alternativ:
    # df_x['new cases'].iloc[0] = df_x['Cases'].iloc[0]
    return df_x


def print_log(message):
    print("{0:<30} {1:<50}".format(f'{datetime.datetime.now()}' + ' :', message))


# change working directory
# # The current working directory is the folder in which the Python script is operating.
# cwd = os.getcwd()
# print("current working directory : ", cwd)


# DATEN EINLESEN.

# root paths
root_project = r'C:\Users\Work\OneDrive - Busch Analytics\PROJEKTE\01_aktuell\corona'  # project home
root_data = r'C:\Users\Work\GitHub\COVID-19'  # Johns-Hopkins-University raw data git-repository

# source paths for data
folder_timeseries = r'csse_covid_19_data\csse_covid_19_time_series'
path_timeseries = os.path.join(root_data, folder_timeseries)
folder_lut1 = r'csse_covid_19_data'
path_lut1 = os.path.join(root_data, folder_lut1)
folder_lut2 = r'02_raw_data\02_Lookup_Tables'
path_lut2 = os.path.join(root_project, folder_lut2)

# output folder for prepared data
path_out = root_project + r'\04_prepared_data'

# os.chdir(path_in)
# cwd = os.getcwd()

print("{:<20} {:<15}".format('root raw data :', root_data))
print("{:<20} {:<15}".format('lookup-tables JHU:', path_lut1))
print("{:<20} {:<15}".format('time series data :', path_timeseries))
print("{:<20} {:<15}".format('root project :', root_project))
print("{:<20} {:<15}".format('own lookup-tables:', path_lut2))
print("{:<20} {:<15}".format('output to:', path_out))

# read lookup-tables
DataIn_PopulationWorld = "UID_ISO_FIPS_LookUp_Table.csv"
infile = os.path.join(path_lut1, DataIn_PopulationWorld)
# Die Spalten "lat", "long" und "population" werden beim Einlesen korrekt als Float erkannt.
# Problem hierbei: das Dezimalzeichen ist ein Punkt "." und würde ohne weitere Maßnahmen auch als solcher ausgegeben.
# Lösung: bei der Ausgabe nach *.csv Dezimalzeichen explizit festlegen.
df_pop_world = pd.read_csv(infile, converters={'code3': str, 'FIPS': str}, encoding='UTF8')

DataIn_US_StateCodes = "LUT_US_State_Codes.xlsx"
infile_StateCodes = os.path.join(path_lut2, DataIn_US_StateCodes)
df_US_StateCodes = pd.read_excel(infile_StateCodes, sheet_name="StateCodes")

DataIn_LUT_Countries = "Länderliste.xlsx"
infile = os.path.join(path_lut2, DataIn_LUT_Countries)
df_countries = pd.read_excel(infile, sheet_name="countries")

#
#
#
# df_pop_world['Lat'] = df_pop_world['Lat'].fillna('')
# df_pop_world.fillna('', inplace=True)


# DATEN VORBEREITEN.


# Länderdaten vorbereiten.
# df_pop_world['code3'] = df_pop_world['code3'].str.split('.', n=-1, expand=True)[0]  # nur linken Teil behalten.
# df_pop_world['FIPS'] = df_pop_world['FIPS'].str.split('.', n=-1, expand=True)[0]
df_pop_world.rename(columns={"Long_": "Long"}, inplace=True)

# Erweiterung der regionalen Klassifizierung um Kontinent/ Länderliste mit Bevölkerungsdaten verknüpfen.
df_pop_world = pd.merge(df_pop_world, df_countries, left_on='Country_Region', right_on='Country', how='left')

# DataOut_PopulationWorld = "Population_World.csv"
# outfile = os.path.join(path_out, DataOut_PopulationWorld)


DataOut_PopulationWorld = os.path.join(path_out, "Population_World.csv")
# decimal="," bewirkt, dass der Punkt "." in einer Zahl als Dezimalzeichen interpretiert wird.
df_pop_world.to_csv(DataOut_PopulationWorld, index=True, header=True, index_label='rownumber', decimal=",", sep=";")
#

# **************************************************************************************************************
# Population_World_Countries
# Es sollen nur Datensätze auf dem Level Country/Region behalten werden.
# Wenn Admin2 und Province_State den Wert 'nan' haben, dann enthält Country/Region aggregierte Daten.
# Die folgende Zeile liefert einen Slice und damit einen View und keine Copy!
df_pop_world_countries = df_pop_world.loc[df_pop_world['Admin2'].isna() & df_pop_world['Province_State'].isna()]
#
#
# Nicht benötigte Spalten entfernen.
# df_pop_world_countries.drop(['FIPS', 'Admin2', 'Province_State', 'Combined_Key'], axis=1, inplace=True)
# Die Variante mit "inplace = True" funktioniert, erzeugt aber eine Warnung (SettingwithCopyWarning):
# "A value is trying to be set on a copy of a slice from a DataFrame".

# https://stackoverflow.com/questions/43893457/understanding-inplace-true
# The inplace parameter:  df.dropna(axis='index', how='all', inplace=True) in Pandas and in general means:
# 1. Pandas creates a copy of the original data
# 2. ... does some computation on it
# 3. ... assigns the results to the original data.
# 4. ... deletes the copy.

df_pop_world_countries = df_pop_world_countries.drop(['FIPS', 'Admin2', 'Province_State', 'Combined_Key'], axis=1)

# Kontrolle
series_pop_world_freq = df_pop_world['Country_Region'].value_counts()
print('\n' * 2, 'Statistiken df_pop_world: Anzahl Werte Country_Region', '\n',
      'Maximale Häufigkeit =', series_pop_world_freq.max(), '\n',
      'Minimale Häufigkeit = ', series_pop_world_freq.min(), '\n',
      'Anzahl Zeilen =', series_pop_world_freq.count()), '\n''*4'

DataOut_PopulationWorldCountries = os.path.join(path_out, "Population_World_Countries.csv")
# decimal="," bewirkt, dass der Punkt "." in einer Zahl als Dezimalzeichen interpretiert wird.
df_pop_world_countries.to_csv(DataOut_PopulationWorldCountries, index=True, header=True, index_label='rownumber',
                              decimal=",", sep=";")
#
#
#

########################################################################################################################
# create datasets

# list of files to import
DataIn_Files = ['time_series_covid19_deaths_US.csv',
                'time_series_covid19_confirmed_US.csv',
                'time_series_covid19_confirmed_global.csv',
                'time_series_covid19_deaths_global.csv',
                'time_series_covid19_recovered_global.csv']

# # Fall-Klassifizierung.
CaseTypes = ['confirmed',
             'deaths',
             'recovered']

# leere Dataframes erzeugen
df_US_wide = pd.DataFrame()
df_global_wide = pd.DataFrame()

print(datetime.datetime.now(), ': Start Datenimport')
print_log('Start Datenimport')

for DataIn_File in DataIn_Files:
    infile = os.path.join(path_timeseries, DataIn_File)

    if 'US' in DataIn_File:
        # US-Daten
        print(datetime.datetime.now(), ': Importiere ', infile)

        # step1: read as dataframe
        df_US_in = pd.read_csv(infile, decimal='.', sep=',', converters={'FIPS': str, 'UID': str})
        print(datetime.datetime.now(), ': ', len(df_US_in), ' Zeilen eingelesen', '\n')

        # remove all characters at the end starting with '.'
        # df_US_in['UID'] = df_US_in['UID'].str.split('.', n=-1, expand=True)[0]
        # df_US_in['FIPS'] = df_US_in['FIPS'].str.split('.', n=-1, expand=True)[0]

        # FIPS-Code (US-Counties, iso2 = 'US') muss 5 stellig sein, falls nicht führende 0 anfügen.
        # noch zu klären: wie sind FIPS-Codes für iso2 <> 'US' zu handhaben?
        # df_US_in['FIPS'] = df_US_in['FIPS'].apply(lambda x: x if len(x) > 4 else '0' + x)
        # apply kann auch auf einen ganzen dataframe angewendet werden.
        df_US_in['FIPS'] = df_US_in.apply(
            lambda x: x['FIPS'] if (x['iso2'] != 'US') | (x['FIPS'] == '') | (
                    (x['iso2'] == 'US') & (len(x['FIPS']) > 4)) else '0' + x[
                'FIPS'], axis=1)
        # df_US_in.loc[(df_US_in['iso2'] == 'US'), df_US_in['FIPS'].str.zfill(15)]

        # step2: Typ des Datensatzes ermitteln, spalte 'casetype' hinzufügen und Typ zuweisen

        # if CaseType = deaths: extract population data, remove column 'Population' and write 'FIPS' and 'Population'
        # to separate file
        # dropping passed columns

        #  "deaths" file version contains population data
        # for CaseType in CaseTypes:
        if 'deaths' in DataIn_File:
            df_pop_us = df_US_in[['Country_Region', 'Province_State', 'Admin2', 'FIPS', 'Population']]
            # 'inplace = True' produziert SettingwithCopyWarning!
            # df_pop_us.rename(columns={'Admin2': 'County'}, inplace=True)
            df_pop_us = df_pop_us.rename(columns={'Admin2': 'County'})
            df_pop_us = pd.merge(df_pop_us, df_US_StateCodes, on='Province_State', how='left')
            df_pop_us['County'] = df_pop_us['County'].fillna('')

            df_pop_us.index = df_pop_us.index + 1

            DataOut_Population_US = os.path.join(path_out, 'Population_US.csv')
            df_pop_us.to_csv(DataOut_Population_US, index=True, index_label='rownumber', header=True,
                             encoding='UTF8',
                             decimal=",",
                             sep=";")
            print(datetime.datetime.now(), ': US-Bevölkerungsdaten auf Ebene FIPS nach File ', DataOut_Population_US,
                  ' exportiert.', '\n' * 2)

            df_US_in['Casetype'] = 'deaths'

        else:
            df_US_in['Casetype'] = 'confirmed'

        # step4: Dataframes hintereinanderhängen
        df_US_wide = df_US_wide.append(df_US_in)

    elif 'global' in DataIn_File:
        print(datetime.datetime.now(), ': Importiere ', infile)

        # step1: file als dataframe einlesen
        df_global_in = pd.read_csv(infile)
        print(datetime.datetime.now(), ': ', len(df_global_in), ' Zeilen eingelesen', '\n')

        # step2: casetype des Datensatzes ermitteln, spalte 'casetype' hinzufügen und Wert von 'casetype' zuweisen
        for CaseType in CaseTypes:
            if CaseType in DataIn_File:
                df_global_in['Casetype'] = CaseType

            # step4: Dataframes hintereinanderhangen
            df_global_wide = df_global_wide.append(df_global_in)

########################################################################################################################

print('\n' * 2)
print('-' * 80)
print(datetime.datetime.now(), ': Starte Transformation der US-Daten')
print(datetime.datetime.now(), ': df_US_wide hat', len(df_US_wide), ' Zeilen.')

df_US_wide.rename(columns={'Long_': 'Long', 'Admin2': 'County'}, inplace=True)

# Damit die anonyme Funktion läuft, darf es keine NaNs geben.
df_US_wide['County'] = df_US_wide['County'].fillna('')
df_US_wide['County_Include'] = df_US_wide['County'].apply(
    lambda x: 'False' if ('Unassigned' in x or 'Out of' in x) else 'True')

df_US_wide.drop(['UID', 'iso2', 'iso3', 'code3'], axis=1, inplace=True)

# step3: Entpivotisieren des Dataframes (wide-format ==> long-format)
print(datetime.datetime.now(), ': Unpivot df_US_wide nach df_US_long.')
df_US_long = pd.melt(df_US_wide,
                     id_vars=['FIPS', 'County', 'County_Include', 'Province_State', 'Country_Region', 'Lat',
                              'Long',
                              'Combined_Key', 'Population', 'Casetype'], var_name=['Date'],
                     value_name='Cases')
print(datetime.datetime.now(), ': df_US_long hat ', len(df_US_long), 'Zeilen.')

# step4: Timestamp eintragen/ Spalte 'Date' als Datum deklarieren.
# Achtung! Python kennt keinen Datentyp DATE !!
df_US_long['ts_created'] = datetime.datetime.now()
# df_US_long['Date'] = df_US_long['Date'].apply(pd.to_datetime).dt.date # Benötigt bei 1 Mio. Datensätzen etwa 5 Minuten!

# schnellste Methode, jedoch wird time mit ausgegeben.
df_US_long['Date'] = pd.to_datetime(df_US_long['Date'], format='%Y/%m/%d', infer_datetime_format=True)
df_US_long['Date'] = df_US_long['Date'].dt.date  # nur Datum extrahieren

# laufen auf Fehler

# d2 = datetime.datetime.strptime(d1, '%d.%m.%y').strftime('%Y-%m-%d')
# df_US_long['Date'] = datetime.datetime.strptime(df_US_long['Date'], '%m/%d/%y').strftime('%Y-%m-%d')
# d.to_datetime(df['mydate'], format='%Y-%m-%d %H:%M:S').dt.strftime('%Y%m%d')
# besser
# df_US_long['Date'] = pd.to_datetime(df_US_long['Date'], format='%m/%d/%y').dt.strftime('%Y-%m-%d')

print(datetime.datetime.now(), ': Sortiere df_US_long nach Country-Province-County-Casetype-Date')
df_US_long.sort_values(by=['Country_Region', 'Province_State', 'County', 'County_Include', 'Casetype', 'Date'],
                       inplace=True)

# step5: Spalten neu anordnen.
cols = ['Country_Region', 'Province_State', 'County', 'County_Include', 'FIPS', 'Lat', 'Long', 'Casetype',
        'Date', 'Population',
        'Cases', 'ts_created']
df_US_long = df_US_long[cols]

# verdichten
# df_US_long = df_US_long.groupby(
#    ['Country_Region', 'Province_State', 'County', 'County_Include', 'FIPS', 'Lat', 'Long', 'Casetype',
#     'Date']).sum().reset_index()

print(datetime.datetime.now(), ': df_US_long auf das Level FIPS-Casetype-Date verdichten.')
df_US_long = (df_US_long
              .groupby(
    ['Country_Region', 'Province_State', 'County', 'County_Include', 'FIPS', 'Lat', 'Long', 'Casetype',
     'Date'])
              .agg({'FIPS': 'size', 'Population': 'sum', 'Cases': 'sum'})
              .rename(columns={'FIPS': 'Anzahl Zeilen'})
              .reset_index()
              )
print(datetime.datetime.now(), ': df_US_long hat nach der Verdichtung ', len(df_US_long), 'Zeilen.', '\n')

# Spalte "new cases" erzeugen.
# Berechne für jede Teilgruppe die Differenz der Spalte 'Cases' zur Vorgänger-Zeile und schreibe in
# die erste Zeile jeder Gruppe eine 0.
df_US_long['new cases'] = \
    df_US_long.groupby(['Country_Region', 'Province_State', 'County', 'County_Include', 'FIPS', 'Lat', 'Long',
                        'Casetype'])['Cases'].diff().fillna(0)

# Ersetze den Wert von 'new cases' in der ersten Zeile durch den entsprechenden Wert von 'Cases'.


df_US_long = df_US_long.groupby(
    ['Country_Region', 'Province_State', 'County', 'County_Include', 'FIPS', 'Lat', 'Long',
     'Casetype']).apply(set_first_value)

# export as csv

DataOut_JHU_US = os.path.join(path_out, 'JHU_US.csv')
print(datetime.datetime.now(), ': Start Export ', DataOut_JHU_US)
df_US_long.to_csv(DataOut_JHU_US, index=True, header=True, index_label='rownumber', encoding='UTF8', decimal=",",
                  sep=";")
print(datetime.datetime.now(), ': Ende Export ', DataOut_JHU_US)
print(datetime.datetime.now(), ': ', len(df_US_long), 'Zeilen nach ', DataOut_JHU_US, 'exportiert.')
print(datetime.datetime.now(), ':  Transformation der US-Daten beendet', '\n', '-' * 80, '\n', '\n')

print('-' * 80, '\n', datetime.datetime.now(), ': Starte Transformation der Global-Daten.')
# step3: Entpivotisieren des Dataframes (Datumswerte sind Spalten ==> Spalte "Datum", Zeilen = Datumswerte
print(datetime.datetime.now(), ': Unpivot df_global_wide')
df_global_long = pd.melt(df_global_wide,
                         id_vars=['Province/State', 'Country/Region', 'Lat', 'Long', 'Casetype'],
                         var_name=['Date'],
                         value_name='Cases')

# step5: Timestamp eintragen/ Spalte 'Date' als Datum deklarieren.
# Achtung! Python kennt keinen Datentyp DATE !!
df_global_long['ts_created'] = datetime.datetime.now()
# df_global_long['Date'] = df_global_long['Date'].apply(pd.to_datetime).dt.date  # zu langsam
df_global_long['Date'] = pd.to_datetime(df_global_long['Date'], format='%Y/%m/%d', infer_datetime_format=True)
df_global_long['Date'] = df_global_long['Date'].dt.date  # nur Datum extrahieren

# step6: Indexspalte labeln, Index bei 1 starten lassen.
df_global_long.index.name = 'row'  # scheint nichts zu bringen...
df_global_long.index += 1
# print(list(df_global_long.columns))

# Kontrolle
# list(df_global_long)

# step7: Spalten neu anordnen.
cols = ['Casetype', 'Province/State', 'Country/Region', 'Lat', 'Long', 'Date', 'Cases', 'ts_created']
df_global_long = df_global_long[cols]
# print(list(df_global_long.columns))

# Merge with population data: Hinzufügen der Spalte "Population"
print(datetime.datetime.now(), ': Merge df_global_long with population data')
df_global_long = pd.merge(df_pop_world_countries, df_global_long, left_on=['Country_Region'],
                          right_on=['Country/Region'],
                          how='right')

# nicht benötigte Spalten entfernen
df_global_long.drop(
    ['UID', 'iso2', 'iso3', 'code3', 'Country_Region', 'Country', 'Province/State', 'Lat_y', 'Long_y'], axis=1,
    inplace=True)

# Spalten neu anordnen
cols = ['AreaType', 'Continent', 'Country/Region', 'Lat_x', 'Long_x', 'Population', 'Date', 'Casetype', 'Cases',
        'ts_created']
df_global_long = df_global_long[cols]

# Spalten umbenennen
df_global_long.rename(columns=({'Lat_x': 'Lat', 'Long_x': 'Long'}), inplace=True)

# Dataframe sortieren/ WICHTIG! 'Date' muss als Datum deklariert sein, sonst falsche Sortierung.
df_global_long.sort_values(by=['Country/Region', 'Casetype', 'Date'], inplace=True)

# *************************************************************************************************************
# Dataframe nach Country/Region, Casetype und Date aggregieren;
# Ziel: Reduktion der regionalen Gliederung von "Continent/Country/Province" zu "Continent/Country";
#
# reset_index ist notwendig,
# sonst werden alle Gruppierungsdimensionen zu einem kombinierten Wert zusammengefasst.
# Zurückgegeben wird im Folgenden nach "split-apply-combine" wieder ein Dataframe
df_global_long = df_global_long.groupby(
    ['AreaType', 'Continent', 'Country/Region', 'Lat', 'Long', 'Casetype', 'Date']).sum().reset_index()

# Spalte "new cases" erzeugen.
# Berechne für jede Teilgruppe die Differenz der Spalte 'Cases' zur Vorgänger-Zeile und schreibe in
# die erste Zeile jeder Gruppe eine 0.
df_global_long['new cases'] = \
    df_global_long.groupby(['AreaType', 'Continent', 'Country/Region', 'Lat', 'Long',
                            'Casetype'])['Cases'].diff().fillna(0)

# Ersetze den Wert von 'new cases' in der ersten Zeile durch den entsprechenden Wert von 'Cases'.


# def set_first_value(df_x):
#     df_x.at[df_x.index[0], 'new cases'] = df_x.at[df_x.index[0], 'Cases']
#     # oder alternativ:
#     # df_x['new cases'].iloc[0] = df_x['Cases'].iloc[0]
#     return df_x


df_global_long = df_global_long.groupby(['AreaType', 'Continent', 'Country/Region', 'Lat', 'Long',
                                         'Casetype']).apply(set_first_value)
# *****************************************************************************************


# Prüfung, ob Indices unique sind. Umwandlung in ein set entfernt alle Duplikate
print('Anzahl unique values df_global_long.index', len(set(
    df_global_long.index.values)))

# Ausgabe
# Granularität des Zielfiles: 'Continent', 'Country/Region', 'Casetype', 'Date'
#
# path_out = r'C:\Users\Work\Desktop\corona\03_Johns_Hopkins\01_Daten'

DataOut_JHU_Global = os.path.join(path_out, 'JHU_Global_New.csv')

# als csv exportieren.
print(datetime.datetime.now(), ': Start Export ', DataOut_JHU_Global)
df_global_long.to_csv(DataOut_JHU_Global, index=True, header=True, index_label='rownumber', encoding='UTF8',
                      decimal=",",
                      sep=";")
print(datetime.datetime.now(), ': Ende Export ', DataOut_JHU_Global)
print(datetime.datetime.now(), ': Transformation der Global-Daten beendet.', '\n', '-' * 80, '\n')
