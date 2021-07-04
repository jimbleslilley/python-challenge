import csv
import os

storedvalues = []
monthlychange = []

#retrieve values for sum, count rows to get months
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for i, row in enumerate(csvreader):
        storedvalues.append(int(row[1]))
    months = i + 1

#use list to get relevant values/indexes
maxrow = storedvalues.index(max(storedvalues))+1
minrow = storedvalues.index(min(storedvalues))+1
maxval = max(storedvalues)
minval = min(storedvalues)

#average calculations and defined
d = 0
h = 1
while h < len(storedvalues):
    monthlychange.append(storedvalues[h] - storedvalues[d])
    d += 1
    h += 1  

average = sum(monthlychange) / len(monthlychange)

#go back through list to get the dates of max / min
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(csvreader):
        if i == maxrow:
            maxdate = row[0]
        elif i == minrow:
            mindate = row[0]

    #text for messages
    titleoutput = (f"Financial Analysis \n----------------------------\n")
    totaloutput = (f"Total Months: {months}\nTotal: ${sum(storedvalues)}\n")    
    averageoutput = (f"Average Change: ${round(average, 2)}\n")
    minmaxoutput = (f"Greatest Increase In Profits: {maxdate} (${maxval})\nGreatest Deacrease In Profits: {mindate} (${minval})")
    output = titleoutput + totaloutput + averageoutput + minmaxoutput 

#create txt file, print/send output
output_path = os.path.join(".", "Analysis", "pybankreport.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
    print(output)