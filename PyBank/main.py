#output needs to be budget_data.csv
#import 
import os
import csv 

# Set path for file  
csvpath = os.path.join("Resources", "budget_data.csv")

# open CSV file 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row & first row 
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    #counter for total number of months 
    months = 1 
    #total profit/loss 
    totalPL = float(firstrow[1])
    #initializer for average change 
    avgChange = 0
    # to compare for changes 
    prevValue = float(firstrow[1])
    #initializer for greatest increase 
    greatestInc = 0 
    greatestIncM = ""
    # initializer for greatest decrease 
    greatestDec= 0 
    greatestDecM=""

    for row in csvreader: 
        months = months + 1 #continue adding months such that you get total number of months at the end 
        totalPL = float(row[1]) + totalPL # continue adding the profit/loss to obtain total profit/loss at the end 
        change = float(row[1])-prevValue #compared to previous value, what was the change 
        avgChange = avgChange + change # add up the changes to calculate average change later 
        prevValue = float(row[1]) #current row is now previous row for next iteration 
        #compare changes to see if it's greater than greatest increase
        if change >=0 and change > greatestInc : 
            greatestInc = change 
            greatestIncM = row[0]
        #compare changes to see if it's less than greatest decrease 
        if change<0 and change<greatestDec: 
            greatestDec = change 
            greatestDecM = row[0]
    #calculate the average change by dividng the sum of all changes by month - 1 
    avgChange = avgChange/(months-1)

    toPrint = [
        "Financial Analysis", 
        "--------------------------------",
        f"Total Months: {months}",
        f"Total: ${round(totalPL)}",
        f"Average Change: ${round(avgChange,2)}",
        f"Greatest Increase in Profits: {greatestIncM} (${round(greatestInc)})",
        f"Greatest Decrease in Profits: {greatestDecM} (${round(greatestDec)})"
        ]

    for i in toPrint: 
        print(i)
        
    

 #specifying file to write to 
output_path = os.path.join("analysis","analysis.txt")

# write to text file 
with open(output_path, 'w') as txtfile: 
    
    for i in toPrint:
        txtfile.writelines(i+'\n')
    