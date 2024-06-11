import os
import csv

print("Election Results")
print("_____________________")

# load the CSV file
election_data = os.path.join("..", "Resources","election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    data = list(csv_reader)

# The total number of votes cast
total_votes = len(data)
print(f'Total number of votes cast: {total_votes}')
print("_____________________")

# A complete list of candidates who received votes
candidates = {}
for row in data:
    candidate = row[2]
    if candidate not in candidates:
        candidates[candidate] = 0
    candidates[candidate] += 1


print("Candidates who received votes:")
for candidate in candidates:
    print(candidate)

# The percentage of votes each candidate won
# The total number of votes each candidate won

for candidate, count in candidates.items():
    candidate_rate = count / total_votes * 100
    print(f'{candidate}: {candidate_rate:.2f}% ({count} votes)')

# The winner of the election based on popular vote

def find_winner(candidates):
    winner = max(candidates, key=candidates.get)
    return winner

winner = find_winner(candidates)
print(f'Winner: {winner}')
