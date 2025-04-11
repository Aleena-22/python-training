import unittest
import os
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filepath = 'test_employees.pkl'
        self.storage = Storage()

        self.employee_data = [
            Employee("Amal", "Software", "Developer", 50000, 5000, 2000).to_dict(),
            Employee("Aleena", "HR", "Manager", 60000, 6000, 3000).to_dict()
        ]

    def test_save_and_load(self):
        self.storage.save_to_file(self.employee_data, self.filepath)

        loaded_data = self.storage.load_from_file(self.filepath)

        self.assertEqual(len(loaded_data), len(self.employee_data))
        for i in range(len(self.employee_data)):
            self.assertEqual(loaded_data[i]['id'], self.employee_data[i]['id'])
            self.assertEqual(loaded_data[i]['name'], self.employee_data[i]['name'])
            self.assertEqual(loaded_data[i]['department'], self.employee_data[i]['department'])
            self.assertEqual(loaded_data[i]['designation'], self.employee_data[i]['designation'])
            self.assertEqual(loaded_data[i]['gross_salary'], self.employee_data[i]['gross_salary'])
            self.assertEqual(loaded_data[i]['tax'], self.employee_data[i]['tax'])
            self.assertEqual(loaded_data[i]['bonus'], self.employee_data[i]['bonus'])
            self.assertEqual(loaded_data[i]['net_salary'], self.employee_data[i]['net_salary'])

    def test_load_non_existent_file(self):
        non_existent_file = "non_existent.pkl"
        loaded_data = self.storage.load_from_file(non_existent_file)
        self.assertEqual(loaded_data, [])

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

if __name__ == "__main__":
    unittest.main()
