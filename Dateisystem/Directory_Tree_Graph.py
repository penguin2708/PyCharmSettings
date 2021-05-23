import os

startpath = r'C:\Users\Work\OneDrive - Busch Analytics\PROJEKTE\01_aktuell\gedk\01_Umsatzanalyse'


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        file_count = 0
        for f in files:
            file_count += 1
        # print(file_count)
        print('{}{}{}'.format(subindent, file_count, ' Dateien'))


list_files(startpath)
