# import the necessary library for working with CSV files
import os
import csv

# set the path to the election_data.csv file
csv_path = os.path.join("Resources", "election_data.csv")

# initialize variables to store election analysis results
total_votes = 0
candidates = {}
winner = ""
max_votes = 0
candidate_info = []

# read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # skip the header row
    next(csvreader)

    # loop through each row in the CSV file
    for row in csvreader:
        
        # extract the ballot id and candidiate name from the current row
        voter_id = row[0]
        candidate = row[2]

        # count the total number of votes cast
        total_votes += 1

        # update the candidate's vote count
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# find the winner based on popular vote
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# calculate and print the election results to the terminal
print("Election Results")
print("----------")
# calculate the percentage of votes each candidate received
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")    
print("----------")
print(f"Winner: {winner}")
print("----------")

# write the election results to a text file
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, "w") as result:
    result.write("Election Results\n")
    result.write("----------\n")
    result.write(f"Total Votes: {total_votes}\n")
    result.write("----------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        result.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    result.write("----------\n")
    result.write(f"Winner: {winner}\n")
    result.write("----------\n")

print("End of Election Results")
