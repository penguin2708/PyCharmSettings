import os

cwd = os.getcwd()
print(cwd)

# change current directory
path = "C:/Users/Work/Documents/Eigenes Tableau-Repository"
os.chdir(path)
cwd = os.getcwd()
print(cwd)

#-------------------------------------------------------
statinfo = os.stat(
    "C:/Users/Work/OneDrive - Busch Analytics/PROJEKTE/02_abgeschlossen\QuickSchuh/09_Präsentation/Korrelationen_ReduktionVariabenzahl.xlsx")
print(statinfo)
