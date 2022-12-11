from apyori import apriori, load_transactions
import csv
import pandas as pd

def Confidence(item):
    return str(item[2][0][2])

def Alphanumeric(item):
    return str(item.items)

fields = []
rows = []

#read in dataset as list from csv
with open('./WonderTrade.csv', 'r') as csvfile:
    records = csv.reader(csvfile, delimiter=',')
    # extracting field names through first row
    fields = next(records)
    # extracting each data row one by one
    for row in records:
        rows.append(row)

#adjust values to make them comparable
for row in rows:
    time = row[0].split(':')
    row[0] = time[0] + ':00'
    if (row[2] == ''):
        row[2] = 'ENG'
    row[3] = str((int(row[3]) - (int(row[3]) % 10)))
    row[4] = row[4] + ' IVs'
    row[5] = 'Stage' + row[5]
 
#write adjusted data to csv
outfile = open('adjustedData.csv', 'w')
writer = csv.writer(outfile)
writer.writerow(['Time','Pokemon','Pokemon Region','Level','Perfect IVs','Evolution Stage'])
for dataList in rows:
    writer.writerow(dataList)
outfile.close()

 #read in file as csv
file = open('./adjustedData.csv', 'r')

with open('./adjustedData.csv') as csvfile:
    readcsv =csv.reader(csvfile, delimiter=",")

data = pd.read_csv('./adjustedData.csv', header = None)
data.head()

data.dropna()
data.head()
data.info()

records = []
rows = data.shape[0]
cols = data.shape[0]

for i in range (0, 500):
    records.append([str(data.values[i,j]) for j in range(0, 6)])

rules = apriori(records, min_support=0.003, min_confience = 0.4, max_length = 2)
results = list(rules)

outfile = open("./outfile.txt", 'w')

results.sort(key=Alphanumeric)
results.sort(reverse=True, key=Confidence)

for item in results:
    pair = item[0]
    items = [x for x in pair]
    if (len(items) > 1):
        outfile.write(items[0] + " " + items[1] + " " + str(item[2][0][2]) + '\n')