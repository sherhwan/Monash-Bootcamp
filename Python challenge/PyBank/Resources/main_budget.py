import os
import csv

# load the CSV file
budget_data = os.path.join("..", "Resources","budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    data = list(csv_reader)


# The total number of months included in the dataset
dates = [row[0] for row in data]
total_months = len(set(dates))
print(f'Total months: {total_months}')

# The net total amount of "Profit/Losses" over the entire period
total_amount = 0

for row in data:
    total_amount += int(row[1])
print(f'Total profit/losses: {total_amount}')

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))]
average_change = sum(changes) / len(changes)
print(f'Average change: {average_change:.2f}')

# The greatest increase in profits (date and amount) over the entire period
max_increase = -float('inf')
max_increase_date = ""
previous_profit = 0.0

# Iterate through the data to find the greatest increase
for row in data:
    date = row[0]
    profit = int(row[1])

    if previous_profit is not None:
        increase = profit - previous_profit
        if increase > max_increase:
            max_increase = increase
            max_increase_date = date

    previous_profit = profit

print(f'The greatest increase in profits: {max_increase_date} (${max_increase})')

# The greatest decrease in profits (date and amount) over the entire period
max_decrease = float('inf')
max_decrease_date = ""
previous_loss = 0.0

# Iterate through the data to find the greatest increase
for row in data:
    date = row[0]
    loss = int(row[1])

    if previous_loss is not 0.0:
        decrease = loss - previous_loss
        if decrease < max_decrease:
            max_decrease = decrease
            max_decrease_date = date

    previous_loss = loss

print(f'The greatest decrease in profits: {max_decrease_date} (${max_decrease})')

