import csv

with open('/Users/jordanheise/Desktop/python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        
import datetime

end_date = datetime.datetime(2017,2,1)
start_date = datetime.datetime(2010, 1, 1)

num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


print("Financial Analysis")
print("--------------------------")
print("Total Months:", num_months)
