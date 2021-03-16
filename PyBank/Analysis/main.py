import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")    
    
    for row in csvreader:
        months = row[0]
        profit_losses = int(row[1])
        #print(row[1])
        
        #total_months =
        #print(total_months)
        
        #total_profit = sum(profit_losses)
        #print(total_profit)
        
        
    