import csv

months = [0]
profit_loss_changes = [1]
count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
profit_loss_change = 0

with open ('/Users/jordanheise/Desktop/nu-chi-data-pt-09-2020-u-c/03-Python/HW/Instructions/PyBank/Resources/budget_data.csv') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     header_row = next(csvfile)
     print(f"Header: {header_row}")