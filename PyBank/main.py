

#Import/Path:
import os
import csv
PyBankcsv=os.path.join("Resources", "budget_data.csv")

#Lists
profit = []
monthly_changes = []
date = []

#Variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
# profit_loss_average = 0
# increase_date = 0
# decrease_date = 0
# greatest_increase_profits = 0
# greatest_decrease_profits = 0

# Open the CSV using the set path PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    revenue = []

    # Loop
    for row in csvreader:    
        # Use count to count the number months in this dataset
        count = count + 1
        # Use for the greatest increase and decrease in profits
        date.append(row[0])

        # Append the profit information & calculate the total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #Calculate the average change in profits
        average_change_profits = (total_change_profits/count)

        #Find the max and min change in profits and the corresponding dates these changes were obeserved
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

        revenue.append(row[1])

    revenue_change = []
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i + 1]) - int(revenue[i])
        revenue_change.append(profit_loss)

    total = sum(revenue_change)
    profit_loss_average = total / len(revenue_change)

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(float(profit_loss_average), 2)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")
    

    with open('analysis', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(profit_loss_average)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")
