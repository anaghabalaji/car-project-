import csv

with open('cardata.csv', 'r') as csv_file: #csv file accessed
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2], ',', line[3]) #labeled data, label printed

print('code is successful')

x = "Nissan Altima"

if x == "Nissan Altima":
    print ('jj')