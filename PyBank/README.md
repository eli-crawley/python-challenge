# Financial Analysis Script

Description
This Python script reads a CSV file containing financial data, performs analysis, and outputs the results to both the console and a new CSV file. The analysis includes:
    * Total number of months in the dataset
    * Total profit/loss over the period
    * Average change in profit/loss between months
    * Greatest increase in profits and the corresponding month
    * Greatest decrease in profits and the corresponding month

The script assumes that the CSV file two columns: date (month-year) and profits/losses

Requirements
Python 3.x
csv module (this is part of the Python standard library, no additional installation required)
os module (this is part of the Python standard library, no additional installation required)

Getting Started
1. Clone or download the repository
You can either clone this repository (if hosted on a platform like GitHub) or download the script file directly.

2. Set up your data file
Prepare your CSV file with the financial data. Ensure it is structured in the following format:
    Date, Profit/Losses
    Jan-2010, 1000
    Feb-2010, 1500

3. Modify the CSV file path
In the script, replace the placeholder for the CSV file path with the actual path to your CSV file:
    csv_file = 'path_to_your_file.csv'

4. Run the script
Execute the script by running the following command in your terminal or command prompt:
    python main.py

5. Results
The script will:
    * Print the analysis results in the console.
    * Create an output CSV file, output_financial_analysis.csv, containing the following results:
        * Total months
        * Total profit/loss
        * Average change in profit/loss
        * Greatest increase in profits and the corresponding month
        * Greatest decrease in profits and the corresponding month

Customization
    Output file pat: You can change the output file name or path by modifying the output_csv variable in the script
