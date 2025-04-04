class BankAccount(object):

    interest_rate = 3

    def __init__(self, acc_holder, balance = 0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount} \nCurrent balance INR {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Debited INR {amount} \n Current balance INR {self.balance}")

    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Updated interest rate to {cls.interest_rate} pct")

    set_interest_rate = classmethod(set_interest_rate)

    def validate_account_number(account_number):
        return len(str(account_number)) == 12 and str(account_number).isdigit()
    
    validate_account_number = staticmethod(validate_account_number)

if __name__ == "__main__":

    acc1 = BankAccount("Anil", 5000)

    if (BankAccount.validate_account_number('234359501312')):
        acc1.deposit(500)
        acc1.withdraw(200)

        BankAccount.set_interest_rate(6)