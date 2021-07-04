import csv
import os
import collections

votelist = []
candidates = set(())

poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for i, row in enumerate(csvreader):
        candidates.add(row[2])
        votelist.append([row[2]])
        
totalvotes = (len(votelist))

# https://www.kite.com/python/answers/how-to-count-item-frequency-in-python#:~:text=Use%20a%20for%2Dloop%20to,value%20to%20which%20item%20maps.
tally = {}
votetuple = tuple(votelist)
for item in votelist:
    if item in tally:
        tally[item] += 1
    else:
        tally[item] = 1

print(tally)
#Output_path = os.path.join(".", "Analysis", "pybankreport.txt")
#with open(output_path, 'w') as txtfile:
    #txtfile.write(output)
    #print(output)