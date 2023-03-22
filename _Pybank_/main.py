import os
import csv
#   path to collect data from the resources
budget_csv = os.path.join('Resources','budget_data.csv')

#   Set the path to save the analysis results to the Analysis directory
Analysis_text = os.path.join('Analysis', 'text.txt')


C = 0
date = []
profit = []
monthly_change = []
Total_profit = 0 
previous_profit= 0
i = 0

#   Read the CSV file
with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
#   store the header row
    header = next(csvreader)

#    Loop through each row of data and perform calculations
    for row in csvreader:
        C = C +1
        date.append(row[0])
        profit.append(row[1])
        Current_profit= int(row[1])
        Total_profit = Total_profit + Current_profit 
        change =  Current_profit - previous_profit
        monthly_change.append(change)  
        previous_profit = Current_profit


#   Find Greatest increase and decrease changes.  

Greatest_increase= max(monthly_change)
GI_date = date[monthly_change.index(Greatest_increase)]

Greatest_decrease= min(monthly_change)
GD_date = date[monthly_change.index(Greatest_decrease)]
#   calculate Avarage change
total= previous_profit - int(profit[0])
avg = total/(C-1)

print("```text")
print("Financial Analysis")
print("------------------------------")
print("")
print("Total Months:" + str(C))
print("Total: $" + str(Total_profit))
print("avarage change: $" + str(avg) )
print("Great Increase in profits: " + str(GI_date) + " ($" + str(Greatest_increase) + ")")
print("Great Decrease in profits: " + str(GD_date) + " ($" + str(Greatest_decrease) + ")")
print("")
print("```")
#   save the results to the output text file
with open(Analysis_text, 'w') as text:
    text.write("----------------------------------------------------------------------------------\n")
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------------------------------\n")
    text.write("\n")
    text.write("    Total Months:" + str(C) +"\n")
    text.write("    Total: $" + str(Total_profit) + "\n")
    text.write("    avarage change: $" + str(avg) + "\n")
    text.write("    Great Increase in profits: " + str(GI_date) + " ($" + str(Greatest_increase) + ")" + "\n")
    text.write("    Great Decrease in profits: " + str(GD_date) + " ($" + str(Greatest_decrease) + ")" + "\n\n")
    text.write("----------------------------------------------------------------------------------\n")