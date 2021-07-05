import csv
import os

storedvalues = []
dates = []
monthlychange = []

#
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #loop through csv, put each section into separate lists
    for i, row in enumerate(csvreader):
        storedvalues.append(int(row[1]))
        dates.append(row[0])

#loop through stored results to record monthly changes to third list
d = 0
h = 1
while h <= len(storedvalues)-1:
    monthlychange.append(storedvalues[h] - storedvalues[d])
    d += 1
    h += 1

months = len(dates)
average = sum(monthlychange) / len(monthlychange)
maxval = max(monthlychange)
minval = min(monthlychange)
maxrow = monthlychange.index(max(monthlychange))+1
minrow = monthlychange.index(min(monthlychange))+1
maxdate = dates[maxrow]
mindate = dates[minrow]

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