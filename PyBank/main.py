# import the necessary library for working with CSV files
import os
import csv

# set the path to the budget_data.csv file
csv_path = os.path.join("Resources", "budget_data.csv")

# initialize variables to store financial analysis results
total_months = 0
total_profit = 0
previous_profit = 0
profit_changes = []
months = []

# read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # skip the header row
    next(csvreader)

    # loop through each row in the CSV file
    for row in csvreader:
        
        # extract the date and profit/loss for the current row
        date = row[0]
        profit_loss = int(row[1])

        # increase the total_months variable by 1 for each row
        total_months += 1
        
        # add the profit/loss value to total_profit
        total_profit += profit_loss

        # calculate the change in profit/loss since the previous month
        if total_months > 1:
            change = profit_loss - previous_profit
            profit_changes.append(change)
            months.append(date)

        previous_profit = profit_loss

# calculate the average change in profit/loss
average_change = round(sum(profit_changes) / len(profit_changes), 2)

# find the greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# get the corresponding dates for the greatest increase and decrease
increase_date = months[profit_changes.index(greatest_increase)]
decrease_date = months[profit_changes.index(greatest_decrease)]

# print the financial analysis to the terminal
print("Financial Analysis")
print("----------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# write the financial analysis results to a text file
output_path = os.path.join("Analysis", "financial_analysis.txt")
with open(output_path, "w") as result:
    result.write("Financial Analysis\n")
    result.write("----------\n")
    result.write(f"Total Months: {total_months}\n")
    result.write(f"Total: ${total_profit}\n")
    result.write(f"Average Change: ${average_change}\n")
    result.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    result.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

print("----------")
print("End of Financial Analysis")
