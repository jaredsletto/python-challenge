"""Module 3 Challenge"""
# pylint: disable=C0103
# Import data
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Assign directories
voter_id = []
county = []
candidate = []
rows = 0

# Open csv file
with open(election_csv, encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        rows += 1

## Calculate the total number of votes cast
votes = rows

## Calculate a complete list of candidates who received votes
unican_list = []
unican_dic = {}
percent_list = []
percent_dic = {}
with open(election_csv, encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
## Calculate the total number of votes each candidate won
        if row[2] not in unican_list:
            unican_list.append(row[2])
            unican_dic[row[2]] = 0
        unican_dic[row[2]] += 1
## Calculate the percentage of votes each candidate won

## Calculate the winner of the election based on popular vote
winner_percent = max(unican_dic.values())
winner = (list(unican_dic.keys())[list(unican_dic.values()).index(winner_percent)])

## Print the results
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(votes))
print("---------------------------")
## Calculate the percentage of votes each candidate won
for key, value in unican_dic.items():
    print(key + ": " + str(round((value/votes)*100,2)) + "% (" + str(value) + ")")
print("---------------------------")
print("Winner: " + winner)
print("---------------------------")

# Print to txt file
pybank_txt = os.path.join("analysis", "PyPollAnalysis.txt")
with open(pybank_txt, "a") as f:
    print("Election Results", file=f)
    print("---------------------------", file=f)
    print("Total Votes: " + str(votes), file=f)
    print("---------------------------", file=f)
    ## Calculate the percentage of votes each candidate won
    for key, value in unican_dic.items():
        print(key + ": " + str(round((value/votes)*100,2)) + "% (" + str(value) +\
               ")", file=f)
    print("---------------------------", file=f)
    print("Winner: " + winner, file=f)
    print("---------------------------", file=f)
