FIle name: filter.py

Description:
This script filters data from a CSV file based on a specified value criteria for a given variable.
It supports filtering based on comparison operators (<, <=, >, >=) as well as exact matches.
Empty string entries for the specified variable are skipped.

Usage:
python filter.py <value_criteria> <variable_name> <filename>

Arguments:
- value_criteria: The criteria for filtering the data. It can be a number or a comparison operator followed by a number.
  Supported comparison operators are: <, <=, >, >=.
  If no comparison operator is provided, then it is assumed that an exact match is required.
- variable_name: The name of the variable to filter the data by.
- filename: The name of the CSV file containing the data. The file should be located in the 'Data' directory.

Example Usage:
python filter.py "40" RIDAGEYR DA-NHANES-2009-2010-DEMO_F.csv
python filter.py "<40" RIDAGEYR DA-NHANES-2009-2010-DEMO_F.csv
python filter.py ">40" RIDAGEYR DA-NHANES-2009-2010-DEMO_F.csv
python filter.py "1" DMQMILIT DA-NHANES-2009-2010-DEMO_F.csv

Output:
The filtered data is saved to a new CSV file in the same directory with a filename in the format:
filtered_<variable_name>_<value_criteria>_<filename>