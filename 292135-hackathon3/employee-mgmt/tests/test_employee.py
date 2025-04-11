import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Amal", "Software", "Developer", 50000, 5000, 2000)

    def test_net_salary_calculation(self):
        self.assertEqual(self.employee.net_salary, 47000)

    def test_to_dict(self):
        employee_dict = self.employee.to_dict()
        self.assertEqual(employee_dict["name"], "Amal")
        self.assertEqual(employee_dict["department"], "Software")
        self.assertEqual(employee_dict["net_salary"], 47000)

    def test_from_dict(self):
        employee_data = {
            "id": "12345",
            "name": "Aleena",
            "department": "HR",
            "designation": "Manager",
            "gross_salary": 60000,
            "tax": 6000,
            "bonus": 3000,
            "net_salary": 57000
        }
        new_employee = Employee.from_dict(employee_data)
        self.assertEqual(new_employee.name, "Aleena")
        self.assertEqual(new_employee.net_salary, 57000)

if __name__ == "__main__":
    unittest.main()
