# import required modules
import csv
import os

# path to csv
csv_file = os.path.join("/Users/rmwc_/Data_Bootcamp/python-challenge/PyPoll/Resources/election_data.csv")

# create variables to hold the data
total_votes = 0
candidates = []
candidate_votes = {}

# read the csv and skip header
with open(csv_file) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # calculate the total votes cast
    for row in csvreader:
        total_votes +=1
        candidate = row[2]

        # create list of cndidates who recieved votes
        if candidate not in candidates:
            candidates.append(candidate)
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# calculate the percentage of votes recieved by each candidate
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes)*100
    candidate_percentages[candidate] = percentage

# calculate the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)

# print results
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")

# define output csv path
output_path = os.path.join("/Users/rmwc_/Data_Bootcamp/python-challenge/PyPoll/analysis/election_results.csv")

# write results to csv
with open(output_path, mode='w') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["---------------------"])
    for candidate in candidates:
        writer.writerow([f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})"])
    writer.writerow(["---------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["---------------------"])