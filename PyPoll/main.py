import csv
import os

votebox = set(())

poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for i, row in enumerate(csvreader):
        votebox.add(row[2])

print(votebox)
#Output_path = os.path.join(".", "Analysis", "pybankreport.txt")
#with open(output_path, 'w') as txtfile:
    #txtfile.write(output)
    #print(output)