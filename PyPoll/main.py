# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0 # Track the total number of votes cast
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0


# Open the CSV file and process it
with open(file_to_load,newline="", encoding="UTF-8") as election_data:

# with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes +=1
        # Print a loading indicator (for large datasets)
        #print(". ", end="")
        # Increment the total vote count for each row
        # Get the candidate's name from the row
        # If the candidate is not already in the candidate list, add them
        # Add a vote to the candidate's count
        if row[2] == "Charles Casper Stockham": 
            Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Doane_votes +=1

# Winning Candidate and Winning Count Tracker
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Stockham_votes, DeGette_votes, Doane_votes]

# Define lists and dictionaries to track candidate names and vote counts
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

        # Print the total vote count (to terminal)
        # Write the total vote count to the text file
        # Loop through the candidates to determine vote percentages and identify the winner
        # Get the vote count and calculate the percentage
Stockham_percent = (Stockham_votes/total_votes) *100
DeGette_percent = (DeGette_votes/total_votes) * 100
Doane_percent = (Doane_votes/total_votes)* 100

        # Update the winning candidate if this one has more votes
        # Print and save each candidate's vote count and percentage
        # Generate and print the winning candidate summary
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
print(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

    # Save the winning candidate summary to the text file
    # Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    writer = csv.writer(txt_file)

    txt_file.write(f"Election Results")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {total_votes}")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
    txt_file.write("\n")
    txt_file.write(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
    txt_file.write("\n")
    txt_file.write(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Winner: {key}")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")

    