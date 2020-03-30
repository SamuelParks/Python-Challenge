# Modules for reading CSV files regardless of operating system being used
import os
import csv

#Setting up some of the variables outside of for loop
change_per_month_tot=0
greatest_increase = 0
greatest_decrease = 0

# Lists to store data
date = []
profit = []

#Pulls budget data CSV file from same folder and reads it
csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r', encoding='utf-8') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # This reads the header row first and allows it to be skipped
    csv_header = next(csvreader)

    #Reads the first row of data separately to avoid messing up the measure of change that is kept track of in the for loop
    ##Removing the first month because the first month does not have a change - we can't assume that the previous month was zero, so we have to remove it. We change only start tracking changes with the first to second month and so on
    first_data_row = next(csvreader)
    date.append(first_data_row[0])
    profit.append(first_data_row[1])
    past_month=int(profit[0])
    net_Profit_Loss=int(profit[0])
    greatest_increase_month =0
    greatest_decrease_month =0

    #Creates row counter outside of for loop so that it can be used outside of for loop; 
    ## This skips the header in the for loop, but starts as one because we did the first line of data separately
    month_counter=1

    # This reads each row of data after the header AND the first line of data - because we are measuring change
    for row in csvreader:
                       
         #This saves all the dates and profit/loss in lists
        date.append(row[0])
        profit.append(row[1])
        month_counter += 1

        change_this_month=int(row[1])-past_month
        change_per_month_tot+=change_this_month
        net_Profit_Loss+= int(row[1])

        if (change_this_month>greatest_increase):
            greatest_increase = change_this_month
            greatest_increase_month = month_counter

        if (change_this_month<greatest_decrease):
            greatest_decrease = change_this_month
            greatest_decrease_month = month_counter

        # This overwrites the past_month with the current month, which will be the past month when the for loop starts again
        past_month = int(row[1])

#Removing the first month because the first month does not have a change - we can't assume that the previous month was zero, so we have to remove it. We change only start tracking changes with the first to second month and so on
average_change_tot = (change_per_month_tot)/(month_counter-1)


print(f"Total Months: {month_counter}")
print(f"Total:  ${net_Profit_Loss}")
print(f"Average Change: $ {round(average_change_tot,2)}")

#greatest_decrease_month and greatest_increase_month are subtracted by one because the index starts at zero
print(f"Greatest Increase in Profits: {date[greatest_increase_month-1]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date[greatest_decrease_month-1]} (${greatest_decrease})")

# Set variable for output file
output_file = os.path.join("PyBankOutput.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # This writes the same information into the output file as was printed into the terminal above
    writer.writerow(["Total Months: ", month_counter])
    writer.writerow(["Total: ",  "$", net_Profit_Loss])
    writer.writerow(["Average Change: ", "$", round(average_change_tot,2)])

    #greatest_decrease_month and greatest_increase_month are subtracted by one because the index starts at zero
    writer.writerow(["Greatest Increase in Profits: ", date[greatest_increase_month-1], "$", greatest_increase])
    writer.writerow(["Greatest Decrease in Profits: ", date[greatest_decrease_month-1], "$", greatest_decrease])