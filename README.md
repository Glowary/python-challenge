# Module 3 Challenge - Python  
​
## PyBank Budget Analysis

For this assignment, we are trying to find:  
​
 - The total number of months included in the dataset  
 - The net total of "Profit/Losses" over the entire period  
 - The changes in "Profit/Losses" over the entire period  
 - The average of the changes from month to month over the entire period  
 - The greatest increase in profits (date and amount) over the entire period  
 - The greatest decrease in profits (date and amount) over the entire period  

### The script will follow the below process for data analysis:  
> 1. Import the necessary library for CSV files and file handling using the `import` function.  
> 2. Define the file path for the raw data file using `os.path.join()`.  
> 3. Initialize the variables that will be used to analyze and store the data. Make sure to set variables as the proper data type.  
> 4. Open and read the CSV file using `with open()` and skip the header using the `next()` function. Then, begin looping through the data for the below calculations.  
> 5. Calculate the total number of months included in the dataset by counting the number of rows one by one, adding one as each row is counted.  
> 6. Calculate the net total of "Profit/Losses" over the entire period by converting each value in the row into integers and adding the row-to-row total.  
> 7. Calculate the month-to-month changes in "Profit/Losses" over the entire period using `if` statements to ensure there are two months of data to find the difference. Use `append()` to store the list of the differences along with the corresponding month.  
> 8. Calculate the average of the month-to-month change using the list stored from the previous step. The average will be the total of all the values from the stored list divided by the number of items in the list.  
> 9. Calculate the greatest increase and decrease in profit with the date and amount over the entire period by using the `max()` and `min()` functions to analyze the list.  
> 10. Print the analyzed results using the `print()` function.  
> 11. Write the result in the text file "financial_analysis.txt" in the "Analysis" folder.
> 12. Add a message at the end showing the analysis is complete and the results have been written to file.  
​  

To read this loop, we’ll loop through each file in the file except for the header. We need to extract the Date and Profit/Loss from the current row we’re analyzing and 
count the total number of months and net total profits. Then, we will calculate the difference in profit from month to month.  
``` py
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        
        total_profit += profit_loss
        if total_months > 1:
            change = profit_loss - previous_profit
            profit_changes.append(change)
            months.append(date)
        previous_profit = profit_loss
```
Using the values we found from the previous section, we are going to calculate the average change in profit/loss, the greatest increase and decrease in profits, and the 
corresponding dates for the greatest increase and decrease.
``` py
average_change = round(sum(profit_changes) / len(profit_changes), 2)
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)
increase_date = months[profit_changes.index(greatest_increase)]
decrease_date = months[profit_changes.index(greatest_decrease)]
```
## PyPoll Election Analysis
For this assignment, we are trying to find:  
​
 - The total number of votes cast  
 - A complete list of candidates who received votes  
 - The total number of votes each candidate won  
 - The percentage of votes each candidate won  
 - The winner of the election based on popular vote  
​
### The script will follow the below process for data analysis:  
> 1. Import the necessary library for CSV files and file handling using the `import` function.  
> 2. Define the file path for the raw data file using `os.path.join()`.  
> 3. Initialize the variables that will be used to analyze and store the data. Make sure to set variables as the proper data type.  
> 4. Open and read the CSV file using `with open()` and skip the header using the `next()` function, then begin looping through the data for the below calculations.  
> 5. Calculate the total number of votes cast by counting the number of rows individually, adding one as each row is counted.  
> 6. Get a complete list of candidates who received votes and calculate the total number of votes for each candidate by using the `if` function. The candidate's name will be extracted from the current row, then check if the name is already in the dictionary. If it is not, then the new unique name will be stored in the dictionary. If the name is already in the dictionary, the vote count will begin for the candidate by increments of 1.  
> 7. Find the percentage of votes for each candidate by looping through the candidate dictionary and using the numbers from the previous steps.  
> 7a. Divide the number of votes the candidate got by the total number of votes overall. Converts into a three-decimal percentage by multiplying it by 100 and using `:.3f` for three decimal points.  
> 8. Find the winner using `if` by going through the candidate dictionary and comparing the vote count.  
> 9. Print the analyzed results using the `print()` function.  
> 10. Write the result in the text file "election_results.txt" in the "Analysis" folder.  
> 11. Add a message at the end showing the analysis is complete and the results have been written to file.  
​  

To read this loop, we’ll loop through each file in the file except for the header. We need to extract the Ballot ID and Candidate from the current row we’re analyzing and
then count the total votes cast. Finalize the candidate's vote count and find the winner based on the most votes received.
```py
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        voter_id = row[0]
        candidate = row[2]
        total_votes += 1
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate
<...>
# calculate the percentage of votes each candidate received
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")    
```  
## Note/Reminders:
- Make sure the location of the data and Python script are saved in the same directory.  
- The first column's index is zero.  
- `[]` is for a list of ordered collections of items.  
- `{}` is for a dictionary of unordered collection items.  
- `""` is for a string of sequence of characters.  
- `f`"TEXT {variable/expression} TEXT"  
- [:.3f` is for format-width of string-decimal](https://thepythonguru.com/python-string-formatting/)
