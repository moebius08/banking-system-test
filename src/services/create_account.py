from domains.account import Account
from domains.customer import Customer

class CreateAccountUseCase:
    def create_account(self, customer_id: str, name: str, email: str, phone_number: str) -> Account:
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        account = Account(account_id=1, customer_id=customer.customer_id, account_number='123456')
        return account
