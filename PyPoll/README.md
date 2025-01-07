# Election Results Script

Description
This Python script reads an election data CSV file, performs an analysis of the election results, and outputs the following:
    * Total number of votes
    * List of candidates who recieved votes
    * Percentage of total votes recieved by each candidate
    * Total number of votes recieved by each candidates
    * The winner of the election (the candidate with the most votes)

The script assumes that the CSV file three columns: an ballot id, county and candidate

Requirements
Python 3.x
csv module (this is part of the Python standard library, no additional installation required)
os module (this is part of the Python standard library, no additional installation required)

Getting Started
1. Clone or download the repository
You can either clone this repository (if hosted on a platform like GitHub) or download the script file directly.

2. Set up your data file
Prepare your CSV file and ensure it has the following format:
    Ballot ID, County, Candidate
    1,Jefferson,John Doe
    2,King,Jane Smith

3. Modify the CSV file path
In the script, replace the placeholder for the CSV file path with the actual path to your CSV file:
    csv_file = 'path_to_your_file.csv'

4. Run the script
Execute the script by running the following command in your terminal or command prompt:
    python main.py

5. Results
The script will:
    * Print the analysis results in the console.
    * Create an output CSV file, election_results.csv, containing the following results:
        * Total number of votes
        * List of candidates who recieved votes
        * Percentage of total votes recieved by each candidate
        * Total number of votes recieved by each candidates
        * The winner of the election (the candidate with the most votes)

Customization
    Output file pat: You can change the output file name or path by modifying the output_csv variable in the script
