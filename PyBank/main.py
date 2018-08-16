import os
import csv

budget_csv = os.path.join('/Users/sueliyahara/Desktop/CWCL201807DATA2-Class-Repository-DATA/Homework/hmw3Python/PyBank/Resources/budget_data.csv')

date = []
profit_loss = []
change_months = []

with open (budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(float(row[1]))
        
    for i in range(1, len(profit_loss)):
        change_months.append(float(profit_loss[i]) - float(profit_loss[i-1]))
        average_change = sum(change_months)/len(change_months)
        average_change =round(average_change, 2)
        
    great_inc_profit = max(change_months)
    
    great_dec_profit = min(change_months)
    
    print("Financial Analysis")
    print("----------------------------------")
    #print("Total Months: " + str(len(date))  
    print("Total: " + sum(profit_loss))
    print("Average Change: $" + average_change)
    print("Greatest Increase in Profits: " + str(date[change_months.index(max(change_months)]) + "(" + great_inc_profit + ")")
    print("Greatest Decrease in Profits: " + str(date[change_months.index(min(change_months)]) + "(" + great_dec_profit + ")")
      
   