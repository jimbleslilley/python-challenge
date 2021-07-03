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

maxrow = storedvalues.index(max(storedvalues))+1
minrow = storedvalues.index(min(storedvalues))+1
maxval = max(storedvalues)
minval = min(storedvalues)
average = sum(storedvalues) / months

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(csvreader):
        if i == maxrow:
            maxdate = row[0]
        elif i == minrow:
            mindate = row[0]

    titleoutput = (f"Financial Analysis \n----------------------------\n")
    totaloutput = (f"Total Months: {months}\nTotal: ${sum(storedvalues)}\n")    
    averageoutput = (f"Average Change: ${round(average, 2)}\n")
    minmaxoutput = (f"Greatest Increase In Profits: {maxdate} (${maxval})\nGreatest Deacrease In Profits: {mindate} (${minval})")
    output = titleoutput + totaloutput + averageoutput + averageoutput + minmaxoutput 

output_path = os.path.join(".", "Analysis", "pybankreport.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
    print(output)
    