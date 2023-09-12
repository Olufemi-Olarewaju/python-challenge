import os
import csv

# To establish filepath
election_csv = os.path.join("..", "Resources", "election_data.csv")

# Variable for list of Voter ID
VoterID_list = []

# Variable for Unique list of Candidates
Candidate_list = []

# Variable for Total list of Candidates (not Unique)
Total_Candidate_list = []

# Read csv file
with open(election_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    header = next(csvreader)

    # To iterate through csv    
    for row in csvreader:
        VoterID_list.append(row[0])
        Total_Candidate_list.append(row[2])

        # To create unique Candidate List
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])

# To calculate Total Votes
Total_votes = len(VoterID_list)

#The list for the percentage of votes each candidate won 
Candidate_Vote_Percent = []

#The list for the total of votes each candidate won 
Candidate_Vote_Total = []

# Iteration to calculate total and percentage of votes each candidate won 
for x in range(len(Candidate_list)):       
    Total_Candidate_Vote = Total_Candidate_list.count(Candidate_list[x])
    Candidate_Vote_Total.append(Total_Candidate_Vote)

    percent_vote = round(((Total_Candidate_Vote/Total_votes) * 100), 3)
    Candidate_Vote_Percent.append(percent_vote)

# Variable to store each candidate's name, percentage of votes won, count of votes won
Candidate_1 = Candidate_list[0]
Candidate_1_percent = Candidate_Vote_Percent[0]
Candidate_1_votecount = Candidate_Vote_Total[0]

Candidate_2 = Candidate_list[1]
Candidate_2_percent = Candidate_Vote_Percent[1]
Candidate_2_votecount = Candidate_Vote_Total[1]

Candidate_3 = Candidate_list[2]
Candidate_3_percent = Candidate_Vote_Percent[2]
Candidate_3_votecount = Candidate_Vote_Total[2]

# Zipped list of Candidate_list and Candidate_Vote_Percent
percent_vote_per_candidate = list(zip(Candidate_list, Candidate_Vote_Percent))

# Iteration to find the winner
for x in percent_vote_per_candidate:
    
    if x[1] == max(Candidate_Vote_Percent):
        winner = x[0]


print(f"\nElection Results")
print(f"\n-------------------------\n")
print(f"Total Votes: {Total_votes}\n")
print(f"\n-------------------------\n")
print(f"{Candidate_1}: {Candidate_1_percent}% ({Candidate_1_votecount})")
print(f"{Candidate_2}: {Candidate_2_percent}% ({Candidate_2_votecount})")
print(f"{Candidate_3}: {Candidate_3_percent}% ({Candidate_3_votecount})")
print(f"\n-------------------------\n")
print(f"Winner: {winner}")
print(f"\n-------------------------\n")


# save the output file path
output_file = os.path.join("..", "analysis", "output.txt")

# open the output file and write
with open(output_file, "w") as datafile:
    datafile.write (f"\nElection Results\n")
    datafile.write (f"\n-------------------------\n")
    datafile.write (f"\nTotal Votes: {Total_votes}\n")
    datafile.write (f"\n-------------------------\n")
    datafile.write (f"\n{Candidate_1}: {Candidate_1_percent}% ({Candidate_1_votecount})\n")
    datafile.write (f"\n{Candidate_2}: {Candidate_2_percent}% ({Candidate_2_votecount})\n")
    datafile.write (f"\n{Candidate_3}: {Candidate_3_percent}% ({Candidate_3_votecount})\n")
    datafile.write (f"\n-------------------------\n")
    datafile.write (f"\nWinner: {winner}\n")
    datafile.write (f"\n-------------------------\n")