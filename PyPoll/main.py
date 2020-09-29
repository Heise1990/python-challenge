import pandas        
import datetime

end_date = datetime.datetime(2017,2,1)
start_date = datetime.datetime(2010, 1, 1)

num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Financial Analysis")
print("--------------------------")
print("Total Months:", num_months)


budgetData = pandas.read_csv('/Users/jordanheise/Desktop/python-challenge/PyBank/Resources/budget_data.csv', delimiter=',')

sum_PL = budgetData['Profit/Losses'].sum()