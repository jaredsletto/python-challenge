"""Module 3 Challenge"""
# pylint: disable=C0103
# Import data
import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Create lists
date_list = []
profit_list = []
abs_profit_list = []
month_list = []
day_list = []

# Open csv file
with open(budget_csv, encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        date_list.append(row[0])
        profit_list.append(int(row[1]))
        abs_profit_list.append(int(row[1]))
    # Split date
        split_date = row[0].split("-")
        month_list.append(split_date[0])
        day_list.append(int(split_date[1]))

## Calculate the total number of months included in the dataset
# Count each month
jan_count = month_list.count("Jan")
feb_count = month_list.count("Feb")
mar_count = month_list.count("Mar")
apr_count = month_list.count("Apr")
may_count = month_list.count("May")
jun_count = month_list.count("Jun")
jul_count = month_list.count("Jul")
aug_count = month_list.count("Aug")
sep_count = month_list.count("Sep")
oct_count = month_list.count("Oct")
nov_count = month_list.count("Nov")
dec_count = month_list.count("Dec")

# Add all month counts
month_count = jan_count + feb_count + mar_count + apr_count + may_count + \
    jun_count + jul_count + aug_count + sep_count + oct_count + nov_count + \
        dec_count

## Calculate the net total amount of "Profit/Losses" over the entire period
net_profit = sum(profit_list)

## Calculate the changes in "Profit/Losses" over the entire period, and then
## the average of those changes
profit_change = 0
previous_profit = 0
greatest_inc =  0
greatest_inc_date = 0
greatest_dec = 0
greatest_dec_date = 0
with open(budget_csv, encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        if previous_profit == 0:
            row_change = 0
            previous_profit = row[1]
        else:
            row_change = int(row[1]) - previous_profit
            profit_change += row_change
## Calculate the greatest increase in profits (date and amount) over the entire
## period
        if row_change > greatest_inc:
            greatest_inc = row_change
            greatest_inc_date = row[0]
## Calculate the greatest decrease in profits (date and amount) over the entire
## period
        elif row_change < greatest_dec:
            greatest_dec = row_change
            greatest_dec_date = row[0]
        previous_profit = int(row[1])

## Calculate average profit change
avg_profit_change = (profit_change / (month_count - 1))
rounded_avg = round(avg_profit_change,2)

# Print the results
print("Financial Analysis")
print("--------------------------------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(net_profit))
print("Average Change: $" + str(rounded_avg))
print("Greatest Increase in Profits: " + str(greatest_inc_date) + " ($"\
       + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + str(greatest_dec_date) + " ($"\
       + str(greatest_dec) + ")")
