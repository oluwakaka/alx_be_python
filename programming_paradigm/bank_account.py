class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.account_balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
