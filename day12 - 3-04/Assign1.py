# Task 1: Update the class dictionary with averages for every student (Step 3)
# Task 2: Come up with a logic to assign ranks for every student and implement it (Step 4)

path = r"D:\py_training\python-training\day12 - 3-04\students.csv"
f = open(path)
content = f.readlines()
f.close()

print("INFO -> step 1", content)

class_dict = {}
columns = [item.strip() for item in content[0].split(',')]  
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')]  
    student_dict = dict(zip(columns, values))  
    class_dict[student_dict['regid']] = student_dict  

# Step 3: Calculate the average
grade_columns = ['phy', 'chem', 'math', 'bio']

for student_id, student_data in class_dict.items():
    grades = []
    
    for col in grade_columns:
        if col in student_data:
            try:
                grades.append(int(student_data[col]))  
            except ValueError:
                print(f"Warning: Non-numeric value found for {student_id} in {col}. Skipping.")
    
    # Calculate the average only if there are valid grades
    if grades:
        student_data['average'] = sum(grades) / len(grades)  
    else:
        student_data['average'] = None  

# Step 4: Calculate ranks ensuring sequential numbering
sorted_students = sorted(class_dict.values(), key=lambda x: x.get('average', 0), reverse=True)

rank = 0
previous_average = None

for student in sorted_students:
    if student['average'] == previous_average:
        student['rank'] = rank  # Same rank for same average
    else:
        rank += 1  # Ensure next rank is sequential
        student['rank'] = rank
    
    previous_average = student['average']

# Update class_dict with sorted students
class_dict = {student['regid']: student for student in sorted_students}


# Step 5: Display the report
print("\n" + "="*100)
print("INFO -> step 5 -> Final Report")
print(f"{'RegID':<10} {'Name':<20} {'Average':<10} {'Rank':<5}")
print("-" * 50)
for student_id, student_data in class_dict.items():
    print(f"{student_id:<10} {student_data.get('name', 'N/A'):<20} {student_data.get('average', 'N/A'):<10} {student_data.get('rank', 'N/A'):<5}")

