# Ausgabe aller Directories unterhalb eines Start-Pfades
# Stand: ok
# Status: 12.12.2020


import os
import pandas as pd
from pandas import ExcelWriter

# Was ist das aktuelle Arbeitsverzeichnis?
cwd = os.getcwd()
print(cwd)

# Konfiguration
df_tree = pd.DataFrame(columns=['directory', 'level', 'no of files'])
startpath = r'C:\Users\Work\OneDrive - Busch Analytics\PROJEKTE\01_aktuell\gedk\01_Umsatzanalyse'
outpath = r'C:\Users\Work\Desktop'
file = 'DIRECTORIES_GedK_Umsatzanalyse.xlsx'
outfile = os.path.join(outpath, file)

for root, dirs, files in os.walk(startpath):
    df_tree = df_tree.append({'directory': root, 'level': root.count('\\'), 'no of files': len(files)},
                             ignore_index=True)

df_tree.index = df_tree.index + 1

# Ausgabe
writer = ExcelWriter(outfile)
df_tree.to_excel(writer, 'DIRECTORIES')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
