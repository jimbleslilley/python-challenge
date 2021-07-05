import csv
import os

votebox = []
candidates = set(())
results = dict()
y = 0

#access csv 
poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #add each vote to votebox, add unique candidate to candidates, store total votes
    for i, row in enumerate(csvreader): 
        candidates.add(row[2])
        votebox.append([row[2]])

totalvotes = (len(votebox))

#check each list and count each candidates votes, store in dict
for candidate in candidates:
    for vote in votebox:
        if candidate == ' '.join(vote):
            y += 1
    results.update({candidate:y})
    y = 0

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value, sorts the results dictionary by value ascending, instead of by key
tally = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}

#take the names from the ascending dictionary and put them in reverse order (so the list is ordered from first to last place for the upcoming loop)
tallylist = list(tally)
tallylist.reverse()

#header and footers
header = (f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------")
footer = (f"-------------------------\nWinner: {tallylist[0]}\n-------------------------")

#loop through sorted list, calculate percentage, print and write file to document
output_path = os.path.join(".", "Analysis", "pypollreport.txt")
with open(output_path, 'w') as txtfile:
    print(header)
    print(header, file = txtfile)
    for candidate in tallylist:
        average = "{:.3f}".format((tally.get(candidate) / totalvotes) * 100)
        print(f"{candidate}: {average}% ({tally.get(candidate)})")
        print(f"{candidate}: {average}% ({tally.get(candidate)})", file = txtfile)
    print(footer)
    print(footer, file = txtfile)