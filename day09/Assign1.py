# Create a employee class with the following features: name,
# age, company, gross_salary, tax_rate, net_salary Implement
# methods to: print information, calculate net_salary based on
# tax rate, set the gross salary, set the tax rate
 
class employee:
 
    #constructor and instance variable initialization
    def __init__(self, name, age, company, gross_salary,tax_rate):
        self.name = name
        self.age = age
        self.company = company
        self.gross_salary = gross_salary
        self.tax_rate = tax_rate
        self.net_salary = 0
 
    # class methods
    def calculate_net_salary(self):
        self.net_salary = self.gross_salary * (1 - self.tax_rate / 100)
        return self.net_salary
 
    def set_gross_salary(self, gross_salary):
        self.gross_salary = gross_salary
 
    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate
   
    def print_information(self):
        print("\nEmployee Information")
        print("------------------------------------")
        print(f"Name        -> {self.name}")
        print(f"Age         -> {self.age}")
        print(f"Company     -> {self.company}")
        print(f"Gross Salary ->  {self.gross_salary}")
        print(f"Tax Rate (%) -> {self.tax_rate}")
        print(f"Net Salary   -> {self.calculate_net_salary()}")
        print("------------------------------------")
 
emp1 = employee("Alice", 30, "UST", 150000, 25)
emp2 = employee("Bob", 45, "TCS", 120000, 20)
 
emp1.print_information()
emp2.print_information()