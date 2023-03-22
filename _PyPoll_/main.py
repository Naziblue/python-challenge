import os
import csv

#   set the paths for the input and output files

election_csv= os.path.join('Resources', 'election_data.csv')
Analysis_text = os.path.join('Analysis', 'text.txt')

candidate_votes = {}
total_votes=0 
Winner= ""
W_T= 0
# Read the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
#   store the header row
    header = next(csvreader)
#   loop over each row to count the votes for each candidate
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
print("``` text")
print("Election Results")
print("-----------------------------------------------------------------")
print("")
print("Total Votes: " + str(total_votes))
print("-----------------------------------------------------------------")

#    print each candidate's vote count and percentage
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes/total_votes:.3%} ({votes})")
#   Find the Winner
for candidate, votes in candidate_votes.items():
    if votes > W_T :
        W_T = votes
        Winner = candidate

#Another way to find the winner:    winner = max(candidate_votes, key=candidate_votes.get)

print("-----------------------------------------------------------------")

print("Winner: " + Winner)
print("-----------------------------------------------------------------")
print("```")
#   save the election results to the output text file
with open (Analysis_text, 'w') as text:
    text.write("Election Results\n")
    text.write("-----------------------------------------------------------------\n\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("-----------------------------------------------------------------\n\n")
    for candidate, votes in candidate_votes.items():
        text.write(f"{candidate}: {votes/total_votes:.3%} ({votes})" + "\n")
    text.write("-----------------------------------------------------------------\n\n")
    text.write("Winner: " + Winner + "\n")
    text.write("-----------------------------------------------------------------\n\n")


