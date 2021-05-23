# Zweck des Programms:

# Autor:    Klaus Busch
# Stand:    17.12.2020
# Status:   dev


import os.path
import pandas as pd
from pandas import ExcelWriter
import time
import datetime;

# cwd:          current working directory
# segment:
# root:         absolute folder to be searched, e.g. "C:/Users/Work/"
# anzahl:
# FullPath:     absolute path inclusive filename
# file:         filename (basename + extension)
# RelativePath: relative path inclusive filename (absolute path without root)
# ctime:
# mtime:


# change current directory
path = r'C:\Users\Work\Desktop'
os.chdir(path)
cwd = os.getcwd()
print(cwd)

# Creating an empty dataframe with column names only
dfObj = pd.DataFrame(
    columns=['Timestamp', 'Segment', 'Root', 'Number', 'RelativePath', 'FileName', 'FullPath', 'FileSize',
             'Creation Date',
             'Modification Date'])

dfObj = dfObj[0:0]  # dataframe leeren

# zu untersuchende Verzeichnisse (hierarchical list)
# folder = {'PROJEKTE': ["U:/", "C:/Users/Work/OneDrive - Busch Analytics/PROJEKTE/"],
#           'RESEARCH': ["W:/", "C:/Users/Work/OneDrive - Busch Analytics/RESEARCH/"],
#           'DATEN': ["Y:/", "C:/Users/Work/OneDrive - Busch Analytics/DATEN/"],
#           'PRIVAT': ["Z:/", "C:/Users/Work/OneDrive - Busch Analytics/PRIVAT/"]}

folder = {'P7S1': [r'C:\Users\Work\OneDrive - ProSiebenSat.1 Media SE']}

for key, value in folder.items():
    for root in value:
        splitat = len(root)

        anzahl = 0

        # Achtung! os.walk setzt den Wert des Arbeitsverzeichnisses (cwd)
        for path, directories, files in os.walk(root):
            for file in files:
                ts = datetime.datetime.now()
                anzahl += 1
                Segment = key
                FullPath = os.path.join(path, file)
                RelativePath = FullPath[splitat:]
                size = os.path.getsize(FullPath)
                ctime = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(os.path.getctime(FullPath)))
                mtime = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(os.path.getmtime(FullPath)))
                dfObj = dfObj.append(
                    {'Timestamp': ts,
                     'Segment': Segment,
                     'Root': root,
                     'Number': anzahl,
                     'RelativePath': RelativePath,
                     'FileName': file,
                     'FullPath': FullPath,
                     'FileSize': size,
                     'Creation Date': ctime,
                     'Modification Date': mtime},
                    ignore_index=True)
                print('Segment: ', Segment, 'Root: ', root, 'Pfad: ', RelativePath, 'Anzahl: ', anzahl)

# Reihenfolge Spalten anpassen
dfObj = dfObj[
    ['Timestamp', 'Segment', 'Root', 'Number', 'RelativePath', 'FileName', 'FullPath', 'FileSize', 'Creation Date',
     'Modification Date']]

dfObj.index = dfObj.index + 1

writer = ExcelWriter('FILES.xlsx')
dfObj.to_excel(writer, 'Files')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
