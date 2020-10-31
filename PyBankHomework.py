import os
import csv

bank_csv = os.path.join("PyBank","Resources", "budget_data.csv")

totalMonths = 0
netProfit = 0
avgChange = 0.0
currentMonth = 0.0
previousMonth = 0.0



with open(bank_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)


    csv_header = next(csvreader)
    
    
    currentMonth = 0
    previousMonth = 0
    monthChange = [] 
        

    for row in csvreader:
       
      totalMonths += 1 
      netProfit += int(row[1])
      
      currentMonth = row[1] 
      monthChange.append(int(currentMonth)-int(previousMonth))   

      
      previousMonth= row[1]


monthChange.remove(867884)
avgChange = round(sum(monthChange)/len(monthChange),2)
grt_profit = max(monthChange)
min_profit = min(monthChange)



output_file = os.path.join("NewBank.txt")

with open(output_file, "w") as outfile:
  outfile.write(f"FINANCIAL ANALYSIS \n")
  outfile.write(f"-----------------------------\n")
  outfile.write(f"Total months: {totalMonths}\n")
  outfile.write(f"Total Profit: ${netProfit}\n")
  outfile.write(f"Avg Change: ${avgChange}\n")
  outfile.write(f"Greatest Increase in Profit: ${grt_profit} \n")
  outfile.write(f"Greatest Decrease in Profit: ${min_profit} ")

  
  print(f"FINANCIAL ANALYSIS")
  print("-----------------------------")
  print(f"Total months: {totalMonths}")
  print(f"Total Profit: ${netProfit}")
  
  print(f"Avg Change: ${avgChange}")
  print(f"Greatest Increase in Profit: ${grt_profit}")
  print(f"Greatest Decrease in Profit: ${min_profit}")


