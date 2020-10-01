import csv

candidates = []
votesCast = 0
voterCount = 0
pollerData = ['1', '2']
    

with open ('/Users/jordanheise/Desktop/nu-chi-data-pt-09-2020-u-c/03-Python/HW/Instructions/PyPoll/Resources/election_data.csv') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     header_row = next(csvfile)
     
     
     # need to total up # of votes per candidate and divide by Total Votes
     # to determine percentage
     
     voters = [0]
     
     for row in csvreader:
         voterCount = voterCount + 1
         candidate = [2]
         
     # comb through data set to count instances of candidate votes earned
         
         if candidate in candidates:
             candidate_index = candidates.index(candidate)
             voterCount[candidate_index] = voterCount[candidate_index] + 1
             
         else:
             candidates.append(candidate)
             voterCount.append(1)
             
         
     
     print("Election Results")
     print("------------------------")
     print(f"Total Votes: {voterCount}")
     print("------------------------")