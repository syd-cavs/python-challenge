import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

print('Election Results')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        #part 1 total number of votes
        votes = row[0]
        
        #part 2 list of candidates who received votes
        candidates = row[2]
        khan = 0
        correy = 0
        li = 0
        otooley = 0
        
        if candidates == "Khan":
            khan = khan + 1
        elif candidates == "Correy":
            correy == correy + 1
        elif candidates == "Li":
            li = li + 1
        elif candidates == "O'Tooley":
            otooley = otooley + 1
            
        print(khan)
            
        
        #part 3 percentage of votes each candidate won
        
        #part 4 winner of the election 
        
        
        
        
        
        # row [0] is the voter ID number, row[1] is the county, row[2] is the candidate