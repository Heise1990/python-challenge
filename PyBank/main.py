import csv

PL = []
numberMonths = 0
PLchanges = [1]
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
        
        currentPL = int(row[1])
        netPL += currentPL
        
        if (numberMonths == 1):
            previousPL = currentPL
            continue
        else:
            PLchange = currentPL - previousPL
            months.append(row[0])
            PLchanges.append(PLchange)
            previousPL = currentPL
            
    sumPL = sum(PLchanges)
    avgPL = round(sumPL/(numberMonths - 1),2)
    
    grtstChange = max(PLchanges)
    smlstChange = min(PLchanges)
    
    grtstIncrs = PLchanges.index(grtstChange)
    grtstDcrs = PLchanges.index(smlstChange)
    
    bestMonthPL = PLchanges.index(grtstChange)
    worstMonthPL = PLchanges.index(smlstChange)
    
    bestMonth = months[bestMonthPL]
    worstMonth = months[worstMonthPL]
    
    output = (
	f"Financial Analysis\n"
	f"-------------------------\n"
	f"Total Months: {numberMonths}\n"
	f"Total: ${netPL}\n"
	f"Average Change: ${avgPL}\n"
	f"Greatest Increase in Profits: {bestMonth} (${grtstChange})\n"
	f"Greatest Decrease in Profits: {worstMonth} (${smlstChange})\n")

print(output)

with open("PYBankFinancials.txt", "w") as txt_file:
	txt_file.write(output)