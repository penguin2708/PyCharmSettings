# Ausgabe aller Files, deren Namen bzw. Extension bestimmte Strings enthalten
# Status: OK
# Stand: 12.12.2020


import os
from path import Path
import datetime
import time
import pandas as pd
from pandas import ExcelWriter

# check the current directory
cwd = os.getcwd()

# change current directory
cwd = Path(r'C:\Users\Work\OneDrive - ProSiebenSat.1 Media SE')
# cwd = Path(r'C:\Users\Work\OneDrive - Busch Analytics\PROJEKTE\01_aktuell\gedk\01_Umsatzanalyse')

# Output
outpath = r'C:\Users\Work\Desktop'
file = 'Inventory_P7S1_20201217.xlsx'
outfile = os.path.join(outpath, file)

df_files = pd.DataFrame(columns=['selector', 'file_name', 'last_mod', 'size'])
x = 0
select = 'no'

# Suchbegriffe
if select == 'yes':
    selectors = ['*']
else:
    selectors = ['.doc', '.ppt', '.xls', '.pdf', '.vsdx', '.twb', '.sql', '.csv', '.tsv', '.txt', '.dat']

# for file in cwd.files():
for root, dirs, files in os.walk(cwd):
    for file in files:
        for selector in selectors:
            if selector in file:
                x += 1
                print(file)
                filename = os.path.join(root, file)
                last_mod = os.stat(filename).st_ctime
                last_mod = datetime.datetime.strptime(time.ctime(last_mod), "%a %b %d %H:%M:%S %Y")
                print(last_mod)
                size = os.stat(filename).st_size
                data = {'selector': selector, 'file_name': filename.replace(cwd + '\\', ''), 'last_mod': last_mod,
                        'size': size}
                print(data)
                print(x)
                df_files = df_files.append(data, ignore_index=True)
                df_files.index = df_files.index + 1

# Ausgabe
writer = ExcelWriter(outfile)
df_files.to_excel(writer, 'Files')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
