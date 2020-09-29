import csv

def candidates(csvfile):
    candidate = str(csvfile[2])
    county = str(csvfile[1])
    voterID = int(csvfile[0])
    

votesCast = 0
voterCount = 0

with open ('/Users/jordanheise/Desktop/nu-chi-data-pt-09-2020-u-c/03-Python/HW/Instructions/PyPoll/Resources/election_data.csv') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     header_row = next(csvfile)
     print(f"Header: {header_row}")
     
     


    
     # need to sum total # of voters
     
     voters = [0]
     
     for row in csvreader:
         voterCount = voterCount + 1
         
     
     print("Election Results")
     print("------------------------")
     print(f"Total Votes: {voterCount}")
     print("------------------------")