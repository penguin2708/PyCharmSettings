# Status: Entwurf, fehlerhaft

import csv
import os

cwd = os.getcwd()
print(cwd)

# change current directory
path = 'C:/Users/Work/Documents/Python/Dateisystem/'
os.chdir(path)
cwd = os.getcwd()
print(cwd)


# output = open('output.csv', 'w')
# output.writelines(row)
# output.close()

with open('EXA_ALL_OBJECT_SIZES_202001221017.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

print(csv_reader)

file = "ItemReport_R1.csv"
print(file)

with open(file, "r",encoding='UTF8') as infile, open("output.csv", "w", newline='', encoding='UTF8') as outfile:
    line = 1
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    #EmptyList = []
    #row = next(reader)
    #row.insert(0, 'Line')
    #EmptyList.insert(0, row)
    #print(row)

    for row in reader:
        line += 1
        #row.append(line)
        #EmptyList.append(row)
        #print(row)

        if row[0]=='Source':
            writer.writerow(["Line"] + item.replace(",", "") for item in row)
        else:
            writer.writerow(str(line) + "," +  item.replace(",", "") for item in row)



if row[0] == "Name":
                writer.writerow(row+["Berry"])
            else:
                writer.writerow(str(row)+[row[0]])