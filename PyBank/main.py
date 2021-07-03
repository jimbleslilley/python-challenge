#my script needs to convert the second column to an integer / float and calculate the average
#my script needs to find the largest and smallest number on a given row
#my script needs to figure out the number of months on the sheet, by counting the number of unqiue rows

#consider assigning values to dict, searching dict for value then returning date? 

import csv
import os

storedvalues = []

budget_csv = os.path.join("Resources", "budget_data.csv")


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for i, row in enumerate(csvreader):
        storedvalues.append(int(row[1]))

    months = i + 1

    maxval = max(storedvalues)
    minval = min(storedvalues)
    maxrow = storedvalues.index(max(storedvalues))+2
    minrow = storedvalues.index(min(storedvalues))+2

    average = sum(storedvalues) / months