class Account():
    """
    Bank account class
    """
    def __init__(self, accNumber, name, balance, accType):
        self.accNumber = accNumber
        self.name = name
        self.balance = balance
        self.accType = accType

    def __str__(self):
        return "Account type: " + str(self.accType) + "\nAccount number: " + str(self.accNumber) + "\nCustomer name: " + str(self.name) + "\nBalance: " + str(self.balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit cannot be negative.")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal cannot be negative.")
        if self.balance - amount < 0:
            raise ValueError("You simply cannot have what isn't there...")
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance


class SavingsAccount():
    """
    Savings account class
    """

    def __init__(self, accNumber, name, savings_balance, accType, annualInterestRate):
        self.accNumber = accNumber
        self.name = name
        self.savings_balance = savings_balance
        self.accType = accType
        self.annualInterestRate = annualInterestRate

    def __str__(self):
        return "Account type: " + str(self.accType) + "\nAccount number: " + str(
            self.accNumber) + "\nCustomer name: " + str(self.name) + "\nBalance: " + str(self.savings_balance) + "\nAnnual interest rate: " + str(self.annualInterestRate)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit cannot be negative.")
        self.savings_balance = round(self.savings_balance + amount, 2)
        print("New balance: ", self.savings_balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal cannot be negative.")
        if self.savings_balance - amount < 0:
            raise ValueError("You simply cannot have what isn't there...")
        self.savings_balance = round(self.savings_balance - amount, 2)
        print("New balance: ", self.savings_balance)

    def update_interest(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.annualInterestRate = rate

    def calculate_monthly_interest(self):
        monthlyRate = ((self.annualInterestRate / 12) / 100)
        interest = round(self.savings_balance * monthlyRate, 2)
        print("Monthly interest of £", interest, " has been added.")
        self.deposit(interest)

    def get_balance(self):
        return self.balance