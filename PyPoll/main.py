# Modules for reading CSV files regardless of operating system being used
import os
import csv

# Lists to store data
candidate_dictionary = {}

#Pulls budget data CSV file from same folder and reads it
csvpath = os.path.join('election_data.csv')

with open(csvpath, 'r', encoding='utf-8') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # This reads the header row first and allows it to be skipped
    csv_header = next(csvreader)
  
    # Read each row of data after the header
    for row in csvreader:
                       
        if row[2] not in candidate_dictionary:
            candidate_dictionary.update( {row[2] : 1} )

        else:
            old_vote_count = candidate_dictionary[row[2]]
            candidate_dictionary[row[2]] = old_vote_count +1

vote_total = sum(candidate_dictionary.values())
greatest_vote_value = max(candidate_dictionary.values())
winning_candidate = []

# This checks to see if there is a tie as well as who the winner is
for key, value in candidate_dictionary.items():
    print(key)
    print(value)
    if value == greatest_vote_value:
        print(key)
        print(value)
        winning_candidate.append(key)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_total}")
print("-------------------------")
for i in candidate_dictionary: 
    print(f"{i}: {(int(candidate_dictionary[i])/vote_total*100):.3f}% ({candidate_dictionary[i]})") 
print("-------------------------")

#In case there is a tie, there are two different print outs:
if len(winning_candidate)==1:
    print(f"Winner: {winning_candidate[0]}")
else:
    print(f"We have a tie. Here are the winners: {winning_candidate}")
print("-------------------------")

# Set variable for output file
output_file = os.path.join("PyPollOutput.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # This writes the same information into the output file as was printed into the terminal above
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow(["Total Votes:", vote_total])
    writer.writerow(["-------------------------"])
    for i in candidate_dictionary: 
        writer.writerow([i,int(candidate_dictionary[i])/vote_total*100,candidate_dictionary[i]]) 
    writer.writerow(["-------------------------"])

    #In case there is a tie, there are two different print outs:
    if len(winning_candidate)==1:
        writer.writerow(["Winner:", winning_candidate[0]])
    else:
        writer.writerow(["We have a tie. Here are the winners:", winning_candidate])
    writer.writerow(["-------------------------"])
