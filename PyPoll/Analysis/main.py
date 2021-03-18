import os
import csv

f= open("PyBank.txt", "w+") 
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
if ((khan > correy) and (khan > li) and (khan > otooley)):
      winner = "Khan"
elif ((correy > khan) and (correy > li) and (correy > otooley)):
      winner = "Correy"
elif ((li > khan) and (li > correy) and (li > otooley)):
      winner = "Li"
elif ((otooley > khan) and (otooley > correy) and (otooley > li)):
      winner = "O'Tooley"

      #bring it all together

otoole = "O'Tooley"

print(total_votes)
print('---------------------------')
print(f'Khan: {khan_percent}00% ({khan}')
print(f'Correy: {correy_percent}00% ({correy}')
print(f'Li: {li_percent}00% ({li})')
print(f'{otoole}: {otooley_percent}00% ({otooley})')
print('---------------------------')     
print(winner)
print('---------------------------')

#text file exports
f.write('Election Results')
f.write('---------------------------')
f.write(f'{total_votes}')
f.write('---------------------------')
f.write(f'Khan: {khan_percent}00% ({khan}')
f.write(f'Correy: {correy_percent}00% ({correy}')
f.write(f'Li: {li_percent}00% ({li})')
f.write(f'{otoole}: {otooley_percent}00% ({otooley})')
f.write('---------------------------')     
f.write(f'{winner}')
f.write('---------------------------')

f.close()