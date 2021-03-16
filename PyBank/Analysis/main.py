import os
import csv
from itertools import count

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        
        profit_losses = int(row[1])
        
        months = count(row[0])
        print(months)
        
        #def total_profit():
        #    total_profit = sum()
        #total_profit(profit_losses)
        #print(total_months)
        
        #total_profit = sum(profit_losses)
        #print(total_profit)
        
        
    