import json

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name is -> {self.name}, Age -> {self.age}, Gender -> {self.gender}"

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        return f"{super().get_details()}, ID -> {self.emp_id}, Department -> {self.department}, Salary -> Rs:{self.salary}"

    def is_eligible_for_bonus(self):
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, int(salary))

    @staticmethod
    def bonus_policy():
        return "Employees who is getting less than Rs:50000 salary is eligible a bonus."

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
                  
    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]
    
# save the data to json

def save_to_json(employees, json_path):
    employees_data = [] 
    
    for emp in employees:
        emp_dict = {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        }
        employees_data.append(emp_dict) 

    with open(json_path, 'w') as file:
        json.dump(employees_data, file, indent=4)

# load the data from json
def load_from_json(json_path):
    with open(json_path, 'r') as file:
        data_of_employees = json.load(file) 
        employees = []
        
        for emp in data_of_employees:
            employees.append(Employee(
                emp["name"], 
                emp["age"], 
                emp["gender"], 
                emp["emp_id"], 
                emp["department"], 
                emp["salary"]
            ))
            
        return employees
