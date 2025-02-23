class Account:
    def __init__(self, account_id: str, customer_id: str, account_number: str, balance: float = 0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance
    def __str__(self):
        return (f"Account("
                f"account_id={self.account_id}, "
                f"customer_id={self.customer_id}, "
                f"account_number={self.account_number}, "
                f"balance={self.balance})")