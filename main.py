# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
import os
import csv

csvpath = os.path.join('.', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')



    # read header to pass row
    csv_header = next(budgetdata)
    print(f"CSV Header: {csv_header}")

    def Analysis():
        Rows = 0
        Total = 0
        Increase = 0
        DateInc = 0
        Decrease = 0            
        DateDec = 0

        for row in csvreader:
            print(f"CSV Header: {csv_header}")

            Rows += 1

            incr = float(row[1])
            Total += incr
            Average = Total/Rows
        
            if incr < Decrease:
                Decrease = incr
                DateDec = str(row[0])

            if incr > Increase:
                Increase = incr
                DateInc = str(row[0])

        print("Financial Analysis")
        print('-------------------')
        print(f"Total Months: {str(Rows)}")
        print(f"Total: ${str(Total)}")
        print(f"Average Change: ${str(Average)}")
        print(f"Greatest Increase in Profits: {str(DateInc)} (${str(Increase)})")
        print(f"Greatest Decrease in Profits: {str(DateDec)} (${str(Decrease)})")

        with open("PyBankAnalysis.text", "w") as f:
            f.write("Financial Analysis \n")
            f.write('-------------------\n')
            f.write(f"Total Months: {str(Rows)}\n")
            f.write(f"Total: ${str(Total)}\n")
            f.write(f"Average Change: ${str(Average)}\n")
            f.write(f"Greatest Increase in Profits: {str(DateInc)} (${str(Increase)})\n")
            f.write(f"Greatest Decrease in Profits: {str(DateDec)} (${str(Decrease)})\n")

    Analysis()
