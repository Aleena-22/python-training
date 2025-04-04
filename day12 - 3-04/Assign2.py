# Task 1: Some ranks are missing, fix the problem
# Task 2: Print the formatted report into a file - studentreport.txt
# Task 3: Write the content of the class dictionary to a file in a CSV format - studentreport.csv 
#             name,age,regid,phy,chem,math,bio,avg,rank
#             Vijay,14,HPE001,99,98,97,96,97.5,3
#             Aryan,14,HPE002,98,91,93,96,94.5,9

path = r"D:\py_training\python-training\day12 - 3-04\students.csv"
f = open(path)
content = f.readlines()
f.close()

print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict

class_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average

for regid in class_dict.keys():
    sum_of_subjects = float(class_dict[regid]['phy']) + float(class_dict[regid]['chem']) + \
                      float(class_dict[regid]['math']) + float(class_dict[regid]['bio'])
    class_dict[regid]['avg'] = sum_of_subjects / 4


print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank

sorted_avgs = sorted(set([class_dict[regid]['avg'] for regid in class_dict.keys()]), reverse=True)  # Unique sorted averages

rank_mapping = {avg: rank+1 for rank, avg in enumerate(sorted_avgs)}  # Mapping average to rank

for regid in class_dict.keys():
    class_dict[regid]['rank'] = rank_mapping[class_dict[regid]['avg']]  # Assign rank based on mapping


print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report

report_path = "studentreport.txt"
with open(report_path, 'w') as report_file:
    template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}\n"
    line = '-'*90 + '\n'

    report_file.write("CLASS REPORT\n")
    report_file.write(line)
    report_file.write(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK'))  # No separator line after header

    for regid in class_dict.keys():
        student = class_dict[regid]
        report_file.write(template.format(student['regid'], student['name'], student['age'], student['phy'],
                                          student['chem'], student['math'], student['bio'], student['avg'], student['rank']))

print("report txt saved")

csv_path = "studentreport.csv"
columns = ['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank']

# Write the class dictionary to a CSV file manually
with open(csv_path, 'w') as csv_file:
    # header row
    csv_file.write(",".join(columns) + "\n")
    # student data rows
    for regid in class_dict.keys():
        student = class_dict[regid]
        row = [student['name'], student['age'], student['regid'], student['phy'],
               student['chem'], student['math'], student['bio'], str(student['avg']), str(student['rank'])]
        csv_file.write(",".join(row) + "\n")

