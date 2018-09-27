import csv
 
 
with open ('UNY.csv', "wb") as f:
    writer = csv.writer(f)
    with open('UNY Address.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            row2 = row[1]
            row3 = row2.split(' ')
            bnum = row3[0]
            state = row3[-1]
            city = row3[-2]
            street = row2.split(' ', 1)[1].rsplit(' ', 2)[0]
            ##print bnum
            ##print state
            ##print city
            ##print street
            writer.writerow([bnum, street, city, state])


