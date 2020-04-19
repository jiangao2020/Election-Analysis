# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote. 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County options and county votes
county_options = []
county_votes = {}

# Candidate options and candidate votes
candidate_options =[]
candidate_votes ={}

# Largest County Turnout
largest_county=""
largest_turnout=0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
         total_votes += 1

         county_name=row[1]

         candidate_name=row[2]

         if county_name not in county_options:

            county_options.append(county_name)

            county_votes[county_name] = 0

         county_votes[county_name] += 1
 
         if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

         candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
   election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")

   print(election_results, end="")
   txt_file.write(election_results)

   for county in county_votes:
      voters = county_votes[county]
      cvote_percentage = float(voters)/float(total_votes)*100

      county_results = (f"{county}: {cvote_percentage:.1f}% ({voters:,})\n")

      print(county_results)
      txt_file.write(county_results)

      if voters > largest_turnout:
                  largest_turnout = voters
                  largest_county = county
   
   largest_turnout_summary = (
      f"-------------------------\n"
      f"Largest County Turnout: {largest_county}\n"
      f"-------------------------\n")
   
   print(largest_turnout_summary)
   txt_file.write(largest_turnout_summary)

   for candidate in candidate_votes:
      votes = candidate_votes[candidate]
      vote_percentage = float(votes)/float(total_votes)*100

      candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

      print(candidate_results)
      txt_file.write(candidate_results)

      if (votes > winning_count) and (vote_percentage > winning_percentage):
                  winning_count = votes
                  winning_percentage = vote_percentage
                  winning_candidate = candidate

   winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")

   print(winning_candidate_summary)
   txt_file.write(winning_candidate_summary)
   