from src.domains.account import Account
from src.domains.customer import Customer
import random
from src.repositories.account_repository import AccountRepository

class CreateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def generate_account_number(self, account_id: str):
        return f"{account_id}-{random.randint(1000, 9999)}"
    
    def create_account(self, customer_id: str, name: str, email: str, phone_number: str) -> Account:
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        account_id = self.account_repository.get_next_account_id()
        random_account_number = self.generate_account_number(account_id)
        account = Account(account_id=account_id, customer_id=customer.customer_id, account_number=random_account_number)
        self.account_repository.save_account(account)
        return account