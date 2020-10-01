import csv

with open ('/Users/jordanheise/Desktop/python-challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
    