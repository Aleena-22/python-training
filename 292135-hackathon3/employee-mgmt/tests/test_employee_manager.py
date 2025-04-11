import unittest
from employee_manager import EmployeeManager
from employee import Employee

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_and_get_employees(self):
        self.manager.add_employee("Amal", "Software", "Developer", 50000, 5000, 2000)
        self.manager.add_employee("Aleena", "HR", "Manager", 60000, 6000, 3000)
        employees = self.manager.get_all_employees()
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].name, "Amal")
        self.assertEqual(employees[1].name, "Aleena")

    def test_find_employee_by_id(self):
        employee = self.manager.add_employee("Amal", "Software", "Developer", 50000, 5000, 2000)
        found_employee = self.manager.search_by_employee_id(employee.id)
        self.assertIsNotNone(found_employee)
        self.assertEqual(found_employee.name, "Amal")
        self.assertEqual(found_employee.department, "Software")

    def test_delete_employee(self):
        employee = self.manager.add_employee("Amal", "Software", "Developer", 50000, 5000, 2000)
        result = self.manager.delete_employee(employee.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_employees()), 0)

    def test_delete_nonexistent_employee(self):
        result = self.manager.delete_employee("non-existent-id")
        self.assertFalse(result)

    def tearDown(self):
        self.manager = None

if __name__ == "__main__":
    unittest.main()
