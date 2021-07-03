#my script needs to convert the second column to an integer / float and calculate the average
#my script needs to find the largest and smallest number on a given row
#my script needs to figure out the number of months on the sheet, by counting the number of unqiue rows

import csv
import os

storedvalues = []


i = 0

budget_csv = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        storedvalues.append(int(row[1]))
        i = i + 1

months = i

print(storedvalues.index(max(storedvalues)))
print(storedvalues.index(min(storedvalues)))
print(max(storedvalues))
print(min(storedvalues))