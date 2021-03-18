import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    total_months = 0
    total_profit = 0

    for row in csvreader:
        
        #part 1 total number of months
        months = (row[0])
        if len(months) > 1:
            total_months = total_months + 1
        
        #part 2 the net total of profit/losses
        net_total = int(row[1])
        if net_total > 1:
            total_profit = total_profit + sum(net_total)
    
        #part 3 calculate the changes in profit/losses, find the average of this change
        #average_change = total_profit / total_months
        
        #part 4 greatest increase in profits
        #finding the max
        
        #part 4 greatest decrease in profits 
        #finding the min
        
print(total_months)  
print(total_profit)