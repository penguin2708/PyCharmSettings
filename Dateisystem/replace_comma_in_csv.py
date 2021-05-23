# Status: fertig, getestet und fehlerfrei
# Stand: 25.01.2020

# Zweck dieses Programms:
# Dieses Programm entfernt Kommas innerhalb von Feldern eines *.csv-Dokuments
# Beispiel: "Z:\", "Projekte, Aufgaben.xlsx" ==> "Z:\", "Projekte Aufgaben.xlsx"

import csv
import os

cwd = os.getcwd()
print(cwd)

# change current directory
path = "C:/Users/Work/AppData/Roaming/Microsoft/MigrationTool/busch-analytics.de/WF_c732ae73/Report/TaskReport_16cbb020"
os.chdir(path)
cwd = os.getcwd()
print(cwd)

file = "ItemReport_R1.csv"

with open(file, "r", encoding='UTF8') as infile, open("output.csv", "w", newline='', encoding='UTF8') as outfile:
    line = 0
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(item.replace(",", "") for item in row)
