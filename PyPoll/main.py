#create simple function to check if a candidate is in a list 
def checkCandExist(candlist, cand):
    if cand in candlist: 
        return True


#import 
import csv
import os 

file_path = os.path.join("Resources","election_data.csv")
with open(file_path) as csvfile: 
    candidates = []
    candVotes = []
    csvreader = csv.reader(csvfile, delimiter =',')
    #skip header row 
    next(csvreader)
    first_row = next(csvreader)
    #first candidate registered 
    candidates.append(first_row[2])
    candVotes.append(1)
    totalVotes = 1 
    
    for row in csvreader: 
        totalVotes = totalVotes + 1 #add the vote to total count 
        #for new candidates appearing in file, initialize 
        if not checkCandExist(candidates, row[2]): 
            candidates.append(row[2])
            candVotes.append(1)
        else: #otherwise add the votes to respective candidate 
            location = candidates.index(row[2])
            candVotes[location] = candVotes[location] + 1
    
    percentage = [number/totalVotes for number in candVotes] #calculate the percentage for each voter 
    percentage = [number*100 for number in percentage] #multiplying to get percent form 
    
    #find the max voting count and locate the winner from list of candidates
    winner = candidates[candVotes.index(max(candVotes))] 

    
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {totalVotes}")
    print("------------------------------")
    for i in candidates: 
        x = candidates.index(i)
        print(f"{i}: {round(percentage[x],3)}% ({candVotes[x]})")
    print("------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------")

#write the analysis file 
output_path = os.path.join("analysis","analysis.txt")
with open(output_path, 'w') as file: 
    file.write("Election Results\n")
    file.write("------------------------------\n")
    file.write(f"Total Votes: {totalVotes}\n")
    file.write("------------------------------\n")
    for i in candidates: 
        x = candidates.index(i)
        file.write(f"{i}: {round(percentage[x],3)}% ({candVotes[x]})\n")
    file.write("------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------------")