import csv

votes = []
candidates = []

with open ('/Users/jordanheise/Desktop/python-challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
   
    
    for column in csvreader:
        votes.append(column[0])
        candidates.append(column[2])

        totalVotes = (len(votes))    
        
    totalvotes = (len(votes))
    
    
    print("Election Results: ")
    print("----------------------")
    print("Total Votes ", totalvotes)
    print("----------------------")
    
    khan = int(candidates.count("Khan"))
    khanPerc = round((khan/totalvotes)*100,3)
    oTooley = int(candidates.count("O'Tooley"))
    oTooleyPerc = round((oTooley/totalvotes)*100,3)
    li = int(candidates.count("Li"))
    liPerc = round((li/totalvotes)*100,3)
    correy = int(candidates.count("Correy"))
    correyPerc = round((correy/totalvotes)*100,3)
    
    voteDict = {"Khan": khan, "Correy": correy, "Li": li, "O'Tooley": oTooley}
    winner = max(voteDict, key = voteDict.get)
    
    
    print(f"Khan: {khanPerc}% ({khan})")
    print(f"Correy: {correyPerc}% ({correy})")
    print(f"Li: {liPerc}% ({li})")
    print(f"oTooley: {oTooleyPerc}% ({oTooley})")
    print("-----------------------")
    print("Winner: ",winner)