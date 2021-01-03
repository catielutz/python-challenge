# import modules
import os
import csv

# set path for file
pybankcsv = os.path.join("Resources", "budget_data.csv")

# define variables and lists
months = []
PnL_changes = []
count_months = 0
net_PnL = 0
prev_mo_PnL = 0
curr_mo_PnL = 0
total_PnL_change = 0

# open and read file
with open(pybankcsv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    csv_header = next(csvreader)
   # read through each row after the header
    for row in csvreader:
        # count months
        count_months += 1

        # find net total PNL
        curr_mo_PnL = int(row[1])
        net_PnL += curr_mo_PnL

        if(count_months == 1):
            # set the value of the previous month to be equal to current month
            prev_mo_PnL = curr_mo_PnL
            continue
        else:
            # calculate PnL changes
            total_PnL_change = curr_mo_PnL - prev_mo_PnL
            
            # append each month to the months list
            months.append(row[0])

            # append PnL change to the PnL change list
            PnL_changes.append(total_PnL_change)

            # move the loop along
            prev_mo_PnL = curr_mo_PnL

# find sum and avg of total changes for the entire period
sum_PnL = sum(PnL_changes)
average_PnL = round(sum_PnL/(count_months - 1), 2)

# find max profit and loss
profit_max = max(PnL_changes)
loss_max = min(PnL_changes)

# find index for max profit and loss
profitmax_index = PnL_changes.index(profit_max)
lossmax_index = PnL_changes.index(loss_max)

# assign best and worst month
best_month = months[profitmax_index]
worst_month = months[lossmax_index]

# print results in terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_PnL}")
print(f"Average Change: ${average_PnL}")
print(f"Greatest Increase in Profits: {best_month} (${profit_max})")
print(f"Greatest Decrease in Profits: {worst_month} (${loss_max})")

# print results to text file
My_Analysis = os.path.join("analysis", "My_Analysis.txt")
with open(My_Analysis, "w") as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {count_months}\n")
    output.write(f"Total: ${net_PnL}\n")
    output.write(f"Average Change: ${average_PnL}\n")
    output.write(f"Greatest Increase in Profits: {best_month} (${profit_max})\n")
    output.write(f"Greatest Decrease in Profits: {worst_month} (${loss_max})\n")