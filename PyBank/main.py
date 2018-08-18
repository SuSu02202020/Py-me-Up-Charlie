import os
import csv

budget_csv = os.path.join('Resources/budget_data.csv')

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
        
    great_inc_profit = float(max(change_months))
    
    great_dec_profit = float(min(change_months))
    
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months: " + str(len(date)))  
    print("Total: " + str(sum(profit_loss)))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(date[change_months.index(max(change_months))+1]) + "(" + str(great_inc_profit) + ")")
    print("Greatest Decrease in Profits: " + str(date[change_months.index(min(change_months))+1]) + "(" + str(great_dec_profit) + ")")
      
with open("output_file.txt", "w") as datafile:
    
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------------\n")
    datafile.write("Total Months: " + str(len(date)) + "\n")  
    datafile.write("Total: " + str(sum(profit_loss)) + "\n")
    datafile.write("Average Change: $" + str(average_change) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(date[change_months.index(max(change_months))+1]) + "(" + str(great_inc_profit) + ")\n")
    datafile.write("Greatest Decrease in Profits: " + str(date[change_months.index(min(change_months))+1]) + "(" + str(great_dec_profit) + ")\n")
    

