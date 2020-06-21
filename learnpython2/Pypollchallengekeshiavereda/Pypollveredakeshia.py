import os
import csv

# path to collect data from and to folder
file_to_load=os.path.join("..","pypollchallengeveredakeshia", "election_data.csv")

#variables
votes = 0
total_number_votes = []
candidate = 0
candidate_list = []
percentage = []
percent_per_candidate = []
total_per_canditate = []
winner = []
with open(file_to_load) as elec_data:
    elect_reader = csv.reader(elec_data, delimiter=',')
    header = next (elect_reader)

    for row in elect_reader:    
    
        #Total_votes
        votes = votes + 1
        #candidate list
        candidate = row[2]
        #number per candidate
        if candidate in candidate_list:
           candidate_index = candidate_list.index(candidate)
           total_number_votes[candidate_index] = total_number_votes[candidate_index] + 1
        else:
            candidate_list.append(candidate)
            total_number_votes.append(1)
        #max total votes
        max_total_votes = total_number_votes[0]
        max_index = 0
        #percent per candidate
        for number in range(len(candidate_list)):
            percent_per_candidate = total_number_votes[number] / votes*100
            percentage.append(percent_per_candidate)
        #winner
            if total_number_votes[number] > max_total_votes:
               max_total_votes = total_number_votes[number]
               print(max_total_votes)
               max_index = number
        winner = candidate_list[max_index]
#print
print("Election Results")
print("------------------")
print(f"Total Votes: {total_number_votes}"
print("------------------")
print(f"Candidate List: {candidate_list}"   
print"-------------------")
print(f"Winner:{winner}")
print("-------------------")
#rewrite
file_to_output=os.path.join("pypollchallengeveredakeshia","election_data_analysis.txt")
with open(file_to_output, "w") as outfile:
    outfile.write(output)
