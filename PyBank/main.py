import os
import csv

# To establish filepath
budget_csv = os.path.join("..", "Resources", "budget_data.csv")


# Variable for list of months
months_list = []

# Variable for net total
net_total = 0

# Variable for list of net change months
net_change_months = []

# Variable of list of Profit/Loss for each month
Profit_Loss_Per_Month = []


# Read csv file
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    header = next(csvreader)

    # To iterate through csv
    for row in csvreader:

        months_list.append(row[0])

        # Calcuate Total
        net_total = net_total + int(row[1])

        Profit_Loss_Per_Month.append(row[1])

        net_change_months.append(row[0])


# Variable to store total number of months
total_months = len(months_list)

# Variable to store month-to-month net change
net_change_month_to_month = []

# Iteration to calculate month-to-month net change
for x in range(len(Profit_Loss_Per_Month) - 1 ):
    net_change = int(Profit_Loss_Per_Month[x + 1]) - int(Profit_Loss_Per_Month[x])
    net_change_month_to_month.append(net_change)

# Total sum of month-to-month net change
total_net_change = 0.0

# Iteration to calculate the Average Change
for amount in net_change_month_to_month:
    total_net_change = total_net_change + amount
# Avarage Change Variable
average_change = round((total_net_change/len(net_change_month_to_month)), 2)

# To remove the first month in the list of net change months
net_change_months.pop(0)

# Zipped list of net_change_months list and net_change_month_to_month list
month_increase_or_decrease = list(zip(net_change_months, net_change_month_to_month))


# To find Greatest Increase and Greatest Decrease in Profits
for x in month_increase_or_decrease:
    if x[1] == max(net_change_month_to_month):
        Greatest_increase = max(net_change_month_to_month)
        Greatest_increase_month = x[0]
    if x[1] == min(net_change_month_to_month):
        Greatest_decrease = min(net_change_month_to_month)
        Greatest_decrease_month = x[0]




print(f"\nFinancial Analysis")
print(f"\n-------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Greatest Increase in Profits: {Greatest_increase_month} $({Greatest_increase})\n")
print(f"Greatest Decrease in Profits: {Greatest_decrease_month} $({Greatest_decrease})\n")

# save the output file path
output_file = os.path.join("..", "analysis", "output.txt")

# open the output file and write
with open(output_file, "w") as datafile:
    datafile.write ("Financial Analysis")
    datafile.write ("\n-------------------------\n")
    datafile.write (f"Total Months: {total_months}\n")
    datafile.write (f"Total: ${net_total}\n")
    datafile.write (f"Greatest Increase in Profits: {Greatest_increase_month} $({Greatest_increase})\n")
    datafile.write (f"Greatest Decrease in Profits: {Greatest_decrease_month} $({Greatest_decrease})\n")