import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        
        #part 1 total number of months
        months = (row[0])
        total_months = count(months)
        print(months)
    
        #part 2 the net total of profit/losses
        profit_losses = int(row[1])
        total_profit = sum(profit_losses)
        print(total_profit)
    
        #part 3 calculate the changes in profit/losses, find the average of this change
        
        #part 4 greatest increase in profits
        
        #part 4 greatest decrease in profits 
        
        
    