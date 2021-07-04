import csv
import os

votebox = []
candidates = set(())
tally = dict()
y = 0

#access csv 
poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #add each vote to votebox, add unique candidate to candidates
    for i, row in enumerate(csvreader): 
        candidates.add(row[2])
        votebox.append([row[2]])


#check each list and count each candidates votes, store in dict
for candidate in candidates:
    for vote in votebox:
        if candidate == ' '.join(vote):
            y += 1
    tally.update({candidate:y})
    y = 0

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
placing = {k: v for k, v in sorted(tally.items(), key=lambda item: item[1])}

totalvotes = (len(votebox))
print(placing)
print(totalvotes)



#Output_path = os.path.join(".", "Analysis", "pybankreport.txt")
#with open(output_path, 'w') as txtfile:
    #txtfile.write(output)
    #print(output)