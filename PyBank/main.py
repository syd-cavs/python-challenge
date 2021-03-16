import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimer=',')
    
    for column in csvreader:
        months = column[0]
        profit = column[1]
        
print(months)
print (profit)
    