#PyPoll
#importing modules to be used
import os #module to create file path across operating systems
import csv #module for reading and writing files


#creating path to the csv file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#variables
num_votes = 0
votes = {}
candidates = {}
percentage = 0
perc_votes = {}
counter =0
final_votes = 0

#assigning the path as a file
with open(csvpath) as csvfile:
    
    #assigning the reader 
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    #reading the header located in the first row
    csv_header = next(csvreader)

    # this would print the header
    # print(f"{csv_header}")
    
    #reading through the data
    for row in csvreader:
        
        #this would print the data
        #print(row)
        
        #counting the number of votes
        num_votes = num_votes + 1
        
        #Candidates row in csv
        candidate = row[2]
                
        #counting the votes and the unique candidates
        if candidate in votes: #if candidate has votes
            votes[candidate] += 1 #then counting the votes per each unique candidate
        else:
            votes[candidate] =1 #if not, assigning to 1 since null
        
        #Now, we have the candidates and their respective votes
        
        #calculating the percentage of votes for each candidate
        for i, voting in votes.items():
            perc_votes[i] = round((voting/num_votes)* 100 , 3)
            
            #retrieving the name of the winner of the eletion
            if voting > final_votes:
                final_votes = voting
                winner_of_election = i

print("\n\nElection Results")
print("-------------------------")
print(f"Total Votes: {num_votes}") # The total number of votes cast
print("-------------------------")
    # All candidates who received votes with the % and the total number of votes
for each_candidate_data, i in votes.items():
    print(f'{each_candidate_data}: {perc_votes[each_candidate_data]}% ({votes[each_candidate_data]})')
print("-------------------------") 
#winner of the election based on popular vote
print(f"Winner: {winner_of_election}")
print("-------------------------\n") 
