import os
import csv

f= open("PyBank.txt", "w+") 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print('Financial Analysis')
print('---------------------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    total_months = 0
    total_profit = 0
    
    previous = 0
    change_list = []
    
    max_value = 0
    max_date = ""
    min_value = 0
    min_date = ""

    for row in csvreader:
        
        #part 1 total number of months
        months = (row[0])
        if len(months) > 1:
            total_months = total_months + 1
        
        #part 2 the net total of profit/losses
        net_total = int(row[1])
        total_profit = total_profit + net_total
    
        #part 3 calculate the changes in profit/losses, find the average of this change
        change = net_total - previous
        change_list.append(change)
        previous = int(row[1])
        
        #part 4 greatest increase in profits, decrease in profits
        if change > max_value:
            max_value = change
            max_date = row[0]
        if change < min_value:   
            min_value = change
            min_date = row[0]
                     
    length = len(change_list) - 1
    average_change = sum(change_list[1:]) / length
             
    print(f'Total Months: {total_months}')  
    print(f'Total: ${total_profit}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {max_date} ({max_value})')
    print(f'Greatest Decrease in Profits: {min_date} ({min_value})')
    
    #text file exports
    f.write('Financial Analysis')
    f.write('---------------------------')  
    f.write(f'Total Months: {total_months}')
    f.write(f'Total: ${total_profit}')
    f.write(f'Average Change: {average_change}')
    f.write(f'Greatest Increase in Profits: {max_date} ({max_value})')
    f.write(f'Greatest Decrease in Profits: {min_date} ({min_value})')


f.close()
