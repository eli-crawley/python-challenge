# import required modules
import csv
import os

# path to csv
csv_file = os.path.join("/Users/rmwc_/Data_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv")

# set variables to store data
months = []
profit_losses = []
monthly_changes = []

# read the csv and skip the header
with open(csv_file) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# calculate the total number of months
total_months = len(months)

# calculate the total amout of "Profit/Losses" for entire time period
total_profit_loss = sum(profit_losses)

# calculate the changes of "Profit/Losses" for entire time period 
for i in range(1,len(profit_losses)):
    change = profit_losses[i] - profit_losses[i-1]
    monthly_changes.append(change)

# calculate the greatest increase in profit for entire time period
greatest_profit = max(monthly_changes)
greatest_profit_month = months[monthly_changes.index(greatest_profit) +1]

# calculate the greatest decrease in profit for entire time period
greatest_loss = min(monthly_changes)
greatest_loss_month = months[monthly_changes.index(greatest_loss) +1]

# calculate the average change
average_change = sum(monthly_changes)/len(monthly_changes) if monthly_changes else 0

# print results
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})")      

# define output csv
output_csv = os.path.join("/Users/rmwc_/Data_Bootcamp/python-challenge/PyBank/analysis/financial_analysis_results.csv")

# export results to csv
with open(output_csv, mode='w') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${total_profit_loss}"])
    writer.writerow([f"Average Change: ${average_change:.2f}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})"])   