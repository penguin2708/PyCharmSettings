import os

for path, dirs, files in os.walk("U:/01_aktuell/gedk/01_Umsatzanalyse"):
  print(path)
  for f in files:
    print(f)