#PyPoll
#importing modules to be used
import os #module to create file path across operating systems
import csv #module for reading and writing files

#creating path to the csv file
csvpath = os.path.join('PyPoll\Resources\election_data.csv')

#variables
num_votes = 0

#assigning the path as a file
with open(csvpath) as csvfile:
    
    #assigning the reader 
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    #reading the header located in the first row
    csv_header = next(csvreader)

    #this would print the header
    #print(f"{csv_header}")
    
    #reading through the data
    for row in csvreader:
        
        #this would print the data
        #print(row)
        
        num_votes = num_votes + 1
        
        

print(f'\nElection Results')
print(f'\n----------------------------\n')
# The total number of votes cast
print(f'Total Votes: \n')
print(f'------------------------------\n')
# All candidates who received votes with the % and the total number of votes
print(f' test  \n')
print(f'------------------------------\n')
# The winner of the election based on popular vote
print(f'test \n')
print(f'------------------------------\n')
