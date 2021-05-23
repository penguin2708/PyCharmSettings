# import os
# os.listdir("C:/Users/Work/Documents/")

# with os.scandir() as dir_entries:
#     for entry in dir_entries:
#         info = entry.stat()
#         print(info.st_mtime)


import os
from path import Path
import datetime
import time

# check the current directory
cwd = os.getcwd()

# change current directory
cwd = Path('C:/Users/Work/Documents/')

for file in cwd.files():
    file_name = file
    last_Mod = os.stat(file).st_ctime
    size = os.stat(file).st_size
    print(file_name)
    print(size)
    print(datetime.datetime.strptime(time.ctime(last_Mod), "%a %b %d %H:%M:%S %Y"))

print(file_name)
