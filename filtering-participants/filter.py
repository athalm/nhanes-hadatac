import csv
import sys
import re
import os

def sanitize_filename(filename):
    return re.sub(r'<', 'l', re.sub(r'<=', 'le', re.sub(r'>=', 'ge', re.sub(r'>', 'g', filename))))

if len(sys.argv) != 4:
    print("Usage: python filter_by_variable.py <value_criteria> <variable_name> <filename>")
    sys.exit(1)

value_criteria = sys.argv[1]
variable_name = sys.argv[2]
filename = sys.argv[3]
pattern = re.compile(r'([<>]=?)(\d+)')
match = pattern.match(value_criteria)

if match:
    operator = match.group(1)
    value = int(match.group(2))
else:
    operator = ''
    value = int(value_criteria)

file_path = os.path.join("../Data/", filename)
if not os.path.exists(file_path):
    print(f"File '{filename}' not found in the 'Data' directory.")
    sys.exit(1)

output_filename = sanitize_filename(f"filtered_{variable_name}_{value_criteria}_{filename}")
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    if operator == '>':
        filtered_data = [row for row in reader if row[variable_name] and int(row[variable_name]) > value]
    elif operator == '>=':
        filtered_data = [row for row in reader if row[variable_name] and int(row[variable_name]) >= value]
    elif operator == '<':
        filtered_data = [row for row in reader if row[variable_name] and int(row[variable_name]) < value]
    elif operator == '<=':
        filtered_data = [row for row in reader if row[variable_name] and int(row[variable_name]) <= value]
    else:
        filtered_data = [row for row in reader if row[variable_name] and int(row[variable_name]) == value]

if filtered_data:
    fieldnames = filtered_data[0].keys()
    with open(output_filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)
    print(f"Filtered data with value {value_criteria} for variable {variable_name} written to {output_filename}.")
else:
    print(f"No data found with value {value_criteria} for variable {variable_name}.")
