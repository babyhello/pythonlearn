import csv

sampleFile = open('data/data47.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
sampleFile.close()

print(type(sampleData))

for row in sampleData:
    for col in row:
        print(col)