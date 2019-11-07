import csv

with open("imdbtitles.csv", newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        if startYear == "2010":
            print(row-1)