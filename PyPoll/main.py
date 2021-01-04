import os
import csv

# set path for file
polldata = os.path.join("Resources", "election_data.csv")

# define initial values to hold data
total_votes = 0
candidates = []
count_vote = []
winning_count = 0

# open and read  file
with open(polldata, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the header
    csv_header = next(csvreader)
    # loop through
    for row in csvreader:
        # increase counter
        total_votes += 1
        # create distinct list of candidates
        if(row[2] not in candidates):
            candidates.append(row[2])
            count_vote.append(0)
        # indext candidate list
        candidate_index = candidates.index(row[2])
        # use the index to count votes per candidate
        count_vote[candidate_index] +=1

# print total votes in terminal
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total votes: {total_votes}")
print("-------------------------")

# calculate percentages, determine winner, print results to terminal
for name in range(len(candidates)):
    percentOFvote = round((count_vote[name]/total_votes)*100)
    print(f"{candidates[name]}: {percentOFvote}% ({count_vote[name]})")
    if (winning_count < count_vote[name]):
        winning_count = count_vote[name]
        winner = candidates[name] 
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# print to text file
