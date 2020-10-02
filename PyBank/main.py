import csv

PL = []
numberMonths = 0
netPL = 0
previousPL = 0
PLchange = 0

with open ('/Users/jordanheise/Desktop/python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header_row = next(csvfile)
        
 # need to total up # of months in data series
 
    months = [0]
        
    for row in csvreader:
        numberMonths = numberMonths + 1
        
        currentPL = int