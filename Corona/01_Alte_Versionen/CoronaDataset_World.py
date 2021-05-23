# COVID 19 - Daten
# Region: Global
# Quelle: Johns-Hopkins-University/ Github-Repository: https://github.com/CSSEGISandData/COVID-19

# Import der Rohdaten (3 Teildatensdtze)
# Transformationen und Zusammenführung in einen Datensatz.

# Stand:    05.05.2020
# Status:   final


import os
import pandas as pd
import datetime

# change working directory
cwd = os.getcwd()
print("current working directory : ", cwd)

# source folder for data
path = "C:/Users/Work/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series"
os.chdir(path)
cwd = os.getcwd()
print("sourcedata are in folder: ", cwd)

root = "C:/Users/Work/OneDrive - Busch Analytics/PROJEKTE/01_aktuell/corona/"
# source folder for lookuptables
path_LUT = root + "02_Lookup_Tables"

########################################################################################################################
# create dataset 'global.csv'

# Liste der einzulesenden Dateien.
files = ['time_series_covid19_confirmed_global.csv',
         'time_series_covid19_deaths_global.csv',
         'time_series_covid19_recovered_global.csv']

# Fall-Klassifizierung.
types = ['confirmed',
         'deaths',
         'recovered']

# leeren Dataframe erzeugen
df = pd.DataFrame()

for file in files:
    # step1: file als dataframe einlesen
    f = pd.read_csv(file)

    # step2: Typ des Datensatzes ermitteln, spalte 'casetype' hinzufügen und Typ zuweisen
    for type in types:
        if type in file:
            f['Casetype'] = type

    # step3: Entpivotisieren des Dataframes
    f1 = pd.melt(f, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long', 'Casetype'], var_name=['Date'],
                 value_name='Cases')

    # step4: Dataframes hintereinanderhangen
    df = df.append(f1)

# step5: Timestamp eintragen
df['ts_created'] = datetime.datetime.now()

# step6: Indexspalte labeln, Index bei 1 starten lassen.
df.index.name = 'row'
df.index += 1

# Kontrolle
list(df)

# step7: Spalten neu anordnen.
cols = ['Casetype', 'Province/State', 'Country/Region', 'Lat', 'Long', 'Date', 'Cases', 'ts_created']
df = df[cols]

# Ausgabe
path_out = root + "04_prepared_data"
outfile = 'Global.csv'
outfile = os.path.join(path_out, outfile)

# als csv exportieren.
df.to_csv(outfile, index=True, header=True, encoding='UTF8')
