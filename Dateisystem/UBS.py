# Zweck:    Archivierung der Nachrichten der UBS
# Status:   prod
# Stand:    22.05.2020


import os
from path import Path
import datetime
from datetime import date
import time
import pandas as pd
from pandas import ExcelWriter
import math
import shutil


# String umkehren.
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


# Zeitstempel
timestamp = datetime.datetime.now()
currentdate = str(date.today()).replace('-', '')

# Verzeichnis, das die zu verteilenden pdf-dokumente enthält.
root_in = Path(r'C:\Users\Azure\OneDrive - Busch Analytics\PRIVAT\02_Finanzen\01_UBS\99_Dokumente_Download')

# Output
root_out = r'C:\Users\Azure\OneDrive - Busch Analytics\PRIVAT\02_Finanzen\01_UBS\02_Dokumente_Archiv'
file = 'UBS_Files_' + currentdate + '.xlsx'
outfile = os.path.join(root_out, file)

df_files = pd.DataFrame(
    columns=['folder', 'full_path', 'file_name', 'last_mod', 'size',
             'Datum', 'Tag', 'Monat', 'Jahr',
             'prefix', 'mid', 'suffix',
             'pos1', 'pos2', 'pos3',
             'Zeitstempel'])

categories = ['Abrechnung',
              'Belastungsanzeige',
              'Bestaetigung',
              'Depotfuehrungspreis',
              'Gutschriftsanzeige',
              'Kapitalertragsteuer',
              'Kontoauszug',
              'Mandatspreis',
              'Transaktionsliste',
              'Vermoegensausweis']

# for category in categories:
#     path = Path(os.path.join(root_out, category))
#     print(type(path))
#     if not path.exists():
#         os.mkdir(path)

x = 0

# for file in root.files():
for root, dirs, files in os.walk(root_in):
    for file in files:

        x += 1
        print('file: ', file)
        full_path = os.path.join(root, file)
        print('full_path: ', full_path)
        last_mod = os.stat(full_path).st_ctime
        last_mod = datetime.datetime.strptime(time.ctime(last_mod), "%a %b %d %H:%M:%S %Y")
        # print(last_mod)
        size = os.stat(full_path).st_size
        pos1 = file.find('_') + 1
        prefix = file[:file.find('_')]

        file_reversed = reverse(file)
        pos2 = len(file) - file_reversed.find('_') - 1
        suffix = reverse(file_reversed[:file_reversed.find('_')])
        mid = file[pos1:pos2]

        pos3 = file.find('per_')
        # extrahiere Datum bei allen Filenames, die <per_> enthalten (z.B. Vermögensausweis_per_30042020)
        if pos3 != -1:  # wenn <per_> enthalten ist....
            datum = file[pos3 + 4:pos3 + 12]
            tag = datum[:2]
            monat = datum[2:4]
            jahr = datum[4:]
        else:  # in allen anderen Fällen
            datum = suffix[:8]
            jahr = datum[:4]
            monat = datum[4:6]
            tag = datum[6:]

        # Annahme: Der string <file> enthält maximal 1 Element aus der Liste <categories>.
        for category in categories:
            if category in file:
                folder = category
                # print('not diverse', file, category)
                # Die Liste <categories> wird durchlaufen. Wenn in einem Filenamen der String <category> enthalten ist,
                # wird dieser Wert der Variablen <folder> zugewiesen.
                # Wenn im Filenamen keine der Kategorienamen aus <categories> enthalten ist, passiert nichts.

        # Der string <file> enthält kein Element aus der Liste <categories>.
        if not any(category in file for category in categories):
            folder = 'Diverse'

        # Dateien auf Folder verteilen.

        # print(folder)
        if folder in ['Abrechnung', 'Bestaetigung', 'Kapitalertragsteuer']:
            # print('yes')
            quartal = math.ceil(int(monat) / 3)
            path_str = os.path.join(root_out, folder, jahr, 'Q' + str(quartal))

        else:
            if len(monat) == 1:
                monat_str = '0' + str(monat)
            else:
                monat_str = str(monat)
            path_str = os.path.join(root_out, folder, jahr, 'M' + monat_str)

        path_out = Path(path_str)

        # print(folder, jahr, quartal)
        # print(path_out)
        # print(path_str)

        if not path_out.exists():
            os.makedirs(path_out)  # makedirs erzeugt - im gegensatz zu mkdir - mehrere levels von directories
            print(path_out)
        # Copy nur dann, wenn der File im Ziel noch nicht vorhanden ist.
        shutil.copyfile(full_path, os.path.join(path_str, file))

        # path = Path(os.path.join(root_out, folder, Datum))
        # if not path.exists():
        #     os.mkdir(path)
        # # Copy nur dann, wenn der File im Ziel noch nicht vorhanden ist.
        # shutil.copyfile(full_path, os.path.join(root_out, folder, Datum, file))

        print(folder)

        data = {'folder': folder,
                'full_path': full_path,
                # 'file_name': full_path.replace(root + '\\', ''),
                'file_name': file,
                'last_mod': last_mod,
                'size': size,
                'prefix': prefix,
                'mid': mid,
                'suffix': suffix,
                'Datum': datum,
                'Tag': tag,
                'Monat': monat,
                'Jahr': jahr,
                'pos1': pos1,
                'pos2': pos2,
                'pos3': pos3,
                'Zeitstempel': timestamp}

        print(data)
        print(x)
        df_files = df_files.append(data, ignore_index=True)
        df_files.index = df_files.index + 1

    # Ausgabe
    # writer = ExcelWriter(outfile)
    # df_files.to_excel(writer, 'Files')
    #
    # # Close the Pandas Excel writer and output the Excel file.
    # writer.save()
    # writer.close()
    # writer.handles = None

    # Ausgabe
    with open(outfile, 'wb') as output:
        writer = pd.ExcelWriter(output, engine='openpyxl')
        df_files.to_excel(writer)
        writer.save()
