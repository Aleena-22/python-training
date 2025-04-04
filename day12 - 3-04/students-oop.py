from students import Student
import csv
from operator import methodcaller, attrgetter


# Read the contents 


student_data = []

with open("D:\py_training\python-training\day12 - 3-04\students.csv", "r") as csvdata:  # context manager
    content = csv.DictReader(csvdata)
    for row in content:
        student_data.append(row)
    

# Create a list of student objects
students = []
for data in student_data:
    temp = Student(data['name'], data['regid'], data['age'])
    temp.set_marks(phy=data['phy'], chem=data['chem'], bio=data['bio'], math=data['math'])
    students.append(temp)

print(type(students[0])) # output if __repr__ not defined-> <class 'students.Student'>
print(students[0]) # output if __str__ not defined -> <students.Student object at 0x000002076AE82F30>

# Calculate average and rank

avgs = list(map(methodcaller('calculate_average'), students))
avgs = sorted(list(set(avgs)), reverse=True)
ranks = [student.set_rank(avgs.index(getattr(student, 'average')) + 1) for student in students]

print(avgs, ranks)

'''
# alternative to getattr()
a = attrgetter('average')(students[0])
print("INFO ", a)
'''


# Write data to the report

with open('studentreport-oop.csv', 'w', newline='') as csvfile:
    reportwriter = csv.writer(csvfile, delimiter=',')
    for student in students:                       
        reportwriter.writerow(student.__str__().split(','))
