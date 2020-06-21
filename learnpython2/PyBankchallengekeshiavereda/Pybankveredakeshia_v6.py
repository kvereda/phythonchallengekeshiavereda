import os
import csv

# path to collect data from and to folder
file_to_load=os.path.join("..","pybankchallengeveredakeshia", "budget_data.csv")

#variables
date = []
total_months = 0
current_net_total = 0
last_months_loss= 0
net_total_loss = 0
avg_change_net_total = []
greatest_increase_month = []
greatest_increase_net_total = 0
greatest_decrease_net_total = 0
greatest_decrease_month = []

#read csv 
with open(file_to_load) as bud_data:
    budget_reader = csv.reader(bud_data, delimiter=',')
    header = next(budget_reader)
   
    for row in budget_reader:
        
        #Total_months
        total_months = total_months + 1

        #Net_Total
        current_net_total += int(row[1])
        
        #Difference between months
        if  (total_months == 1):
            last_months_loss = current_net_total
        else:
            avg_change_net_total = current_net_total - last_months_loss
            date.append(row[0])
        #Average Change
            avg_change_net_total.append(avg_change_net_total)
            last_months_loss =current_net_total

        avg_change_net_total = round(current_net_total / ((len(total_months)-1),2)
        
        #greatest_increase_in_profits
        greatest_increase_net_total = max(avg_change_net_total)
        #greatest_decrease_in_profits
        greatest_decrease_net_total = min(avg_change_net_total)

        #date for greatest_increase month
        greatest_increase_month_index = avg_change_net_total.index(greatest_increase_net_total)
        greatest_increase_month = date[greatest_increase_month_index]
        #date for greatest_decrease month
        greatest_decrease_month_index = avg_change_net_total.index(greatest_decrease_net_total)
        greatest_decrease_month = date[greatest_decrease_month_index]
#print
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${current_net_total}")
print(f"Average Change: ${avg_change_net_total}")
print(f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase_net_total}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease_net_total}")
#rewrite
file_to_output=os.path.join("pybankchallengeveredakeshia","budget_data_analysis.txt")
with open(file_to_output, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${current_net_total}\n")
    outfile.write(f"Average Change: ${avg_change_net_total}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase_net_total}\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease_net_total}\n")