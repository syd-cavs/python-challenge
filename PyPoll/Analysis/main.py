import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

print('Election Results')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    total_votes = 0
        
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    
    for row in csvreader:
        #part 1 total number of votes, make a counter
        votes = int(row[0])
        if votes > 1:
            total_votes = total_votes + 1
                    
        #part 2 list of candidates who received votes
        candidates = row[2]
        
        if candidates == "Khan":
           khan = khan + 1
        elif candidates == "Correy":
           correy = correy + 1
        elif candidates == "Li":
           li = li + 1
        elif candidates == "O'Tooley":
           otooley = otooley + 1  
            
#part 3 percentage of votes each candidate won
khan_percent = round((int(khan) / int(total_votes)) * 100, 2)
correy_percent = round((int(correy) / int(total_votes)) * 100, 2)
li_percent = round((int(li) / int(total_votes)) * 100, 2)
otooley_percent = round((int(otooley) / int(total_votes)) * 100, 2)     
        
        #part 4 winner of the election 
        #publishing the candidate with the most votes




        
        
        
        
        # row [0] is the voter ID number, row[1] is the county, row[2] is the candidate
print(total_votes)
print(khan, correy, li, otooley)
print(khan_percent, correy_percent, li_percent, otooley_percent)