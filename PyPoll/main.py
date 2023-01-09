#PyPoll
#importing modules to be used
import os #module to create file path across operating systems
import csv #module for reading and writing files

#creating path to the csv file
csvpath = os.path.join('PyPoll\Resources\election_data.csv')

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
        


# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote