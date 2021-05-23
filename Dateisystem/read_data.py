# Status: fertig, getestet und fehlerfrei
# Stand: 25.01.2020

# Zweck dieses Programms:
# Dieses Programm entfernt Kommas innerhalb von Feldern eines *.csv-Dokuments
# Beispiel: "Z:/", "Projekte, Aufgaben.xlsx" ==> "Z:/", "Projekte Aufgaben.xlsx"

import csv
import os

cwd = os.getcwd()
print(cwd)

# change current directory
path = "C:/Users/Work/Documents/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series"
os.chdir(path)
cwd = os.getcwd()
print(cwd)

file = "time_series_covid19_confirmed_global.csv"

with open(file, "r", encoding='UTF8') as infile:
    reader = csv.reader(infile)

print(reader)

