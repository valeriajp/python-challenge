# -*- coding: UTF-8 -*-
#"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
actual_month = 0
previous_month = 0

#The Changes in "Profit/Losses" over the entire period (actual_month - previous_month)
monthly_change = 0

# empty list for months and hold monthly_change
month = []
monthly_profit_change = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # Track the total and net change

    # Process each row of data
    for row in reader:
        total_months +=1

        # Track the total
        actual_month = (int(row[1]))

        # Track the net change
        total_net += actual_month
        
        # Regression for previous month value to first month
        if total_months == 1:
            previous_month = actual_month 
    
        # Calculation for summing up change in months
        else:
            monthly_change = actual_month - previous_month
        # Addition of month to column   
            month.append(row[0])
        # Addition of monthly change to column
            monthly_profit_change.append(monthly_change)
        # Restart the cycle
            previous_month = actual_month

        # Calculate the greatest increase in profits (month and amount), Function Max value
        # Calculate the greatest decrease in losses (month and amount), Function min value

# Calculate the average net change across the months
mean_change = (sum(monthly_profit_change)) / (total_months - 1) 

# Generate the output summary
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Average Change: {(round(mean_change,2))}")
print(f"Greatest Increase in Profits: ${(max(monthly_profit_change))}")
print(f"Greatest Decrease in Profits: ${(min(monthly_profit_change))}")

# Print the output
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    writer = csv.writer(txt_file)
 
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total Months: {total_months}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {(round(mean_change,2))}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: ${(max(monthly_profit_change))}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: ${(min(monthly_profit_change))}")