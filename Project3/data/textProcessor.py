import csv
import os
import textcleaner as tc

os.chdir('C:/workdir/visual-interfaces/Project3/data')

rows = []
with open('showData.csv', 'r', newline='', encoding='utf-8-sig') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        data = tc.document(row[1])
        cleanData1 = data.remove_stpwrds()
        cleanData2 = cleanData1.main_cleaner()
        # print(cleanData)
        newRow = [row[0], cleanData2, row[2], row[3]]
        rows.append(newRow)

with open('cleanedShowData.csv', 'w', newline='', encoding='utf-8-sig') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Character', 'Line', 'Season', 'Episode'])
    for row in rows:
        writer.writerow(row)