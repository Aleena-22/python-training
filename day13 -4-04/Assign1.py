# 1. Refactor the 24-sc-student-report-generator.py to work with student.json
#     Read student.json
#     Calculate averages and ranks
#     Write student-report.json

# Step 1
# Read the content
import json

json_path = r"D:\py_training\python-training\day13 -4-04\students.json"

with open(json_path, 'r') as f:
    data = json.load(f) 

print("\nINFO -> Step 1: Read JSON data\n", data)

# Convert list to dictionary using 'regid' as the key
class_dict = {student['regid']: student for student in data}

# Step 2
# Calculate the average

for regid in class_dict.keys():
    sum_of_subjects = float(class_dict[regid]['phy']) + float(class_dict[regid]['chem']) + \
                      float(class_dict[regid]['math']) + float(class_dict[regid]['bio'])
    class_dict[regid]['avg'] = sum_of_subjects / 4

print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank

avgs = set([class_dict[regid]['avg'] for regid in class_dict.keys()])
avgs = list(avgs)
avgs.sort(reverse=True)

for regid in class_dict.keys():
    class_dict[regid]['rank'] = avgs.index(class_dict[regid]['avg']) + 1

print("\n" + "-"*100)
print("INFO -> Step 3: Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report in json

report_json_path = "D:\py_training\python-training\day13 -4-04\student-report.json"

# Write the updated data back to a new JSON file
with open(report_json_path, 'w') as json_file:
    json.dump(class_dict, json_file, indent=4)

