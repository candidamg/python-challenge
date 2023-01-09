#importing modules to be used
import os #module to create file path across operating systems
import csv #module for reading and writing files

#path to the csv file
csvpath = os.path.join('PyBank/Resources/budget_data.csv')

#creating the variables
months_count = 0
allMonths = []
profit = []
mprofit = []
ave_ch = 0
difference = []
profit_lenght = 0

#opening the budget_data file in reader mode
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    #reading the header located in the first row
    csv_header = next(csvreader)

    #this would print the header
    #print(f"{csv_header}")
    
    #reading the data 
    for row in csvreader: 
        
        #counter for the total number of months included in the dataset
        months_count = months_count + 1

        #appending the months in a list
        allMonths.append(row[0])
        #appending the profits in a list
        profit.append(int(row[1]))
        
        #net total amount of profit/losses over the entire period
        nettotal = sum(profit)
    
    #profit lenght - not counting the first one
    profit_lenght = len(profit) -1

    #for-loop to go through the list for the monthly change in profits
    for i in range(profit_lenght):
        
        #calculating the difference between the next and current
        difference = profit[i+1]-profit[i]
        #append = for the monthly profit change
        mprofit.append(difference)

        #calculating the average change
        ave_ch = sum(mprofit) / len(mprofit)
        #rounding the average change by 2 decimals
        ave_ch = round(ave_ch,2)
            
        #Obtain the max and min of the the montly profit change list
        increase_profit = max(mprofit)
        decrease_profit = min(mprofit)

        #getting the index for the increase and decrease from the profit/losses 
        increase_profit_date = mprofit.index(increase_profit) 
        decrease_profit_date = mprofit.index(decrease_profit)  

        #getting the greatest increase and decrease months
        increase_date = allMonths[increase_profit_date+1]
        decrease_date = allMonths[decrease_profit_date+1]

#---------------------------------------------------
#PRINTING THE RESULTS
#--------------------------------------------------- 

print("\nFinancial Analysis")
print("\n----------------------------")
#printing the total number of months included in the dataset
print(f"\nTotal Months: {months_count}")
#printing the net total amount of "Profit/Losses" over the entire period
print(f"\nTotal: ${nettotal}")
#printing the average 
print(f"\nAverage Change: ${ave_ch}")
#printing the greatest increase in profits (date and amount) over the entire period
print(f"\nGreatest Increase in Profits: {increase_date} (${(increase_profit)})")
#printing the greatest decrease in profits (date and amount) over the entire period
print(f"\nGreatest Decrease in Profits: {decrease_date} (${(decrease_profit)})\n")

#assigning the path to a variable
new_file = os.path.join('PyBank/analysis/new.txt')

#creating a text file in write mode
with open(new_file, 'w') as f:
        
    #---------------------------------------------------
    #EXPORTING THE RESULTS IN A NEW TEXT FILE 
    #--------------------------------------------------- 
    
    f.write("\nFinancial Analysis")
    f.write("\n----------------------------")
    #writing the total number of months included in the dataset
    f.write(f"\nTotal Months: {months_count}")
    #writing the net total amount of "Profit/Losses" over the entire period
    f.write(f"\nTotal: ${nettotal}")
    #writing the average 
    f.write(f"\nAverage Change: ${ave_ch}")
    #writing the greatest increase in profits (date and amount) over the entire period
    f.write(f"\nGreatest Increase in Profits: {increase_date} (${(increase_profit)})")
    #writing the greatest decrease in profits (date and amount) over the entire period
    f.write(f"\nGreatest Decrease in Profits: {decrease_date} (${(decrease_profit)})\n")