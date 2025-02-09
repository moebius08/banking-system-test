from domains.account import Account
from repositories.account_repository import AccountRepository
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'

class TransactionUseCase:

    def __init__(self):
        self.account_repository = AccountRepository()

    def make_transaction(self, account_id: str, amount: float, transaction_type: TransactionType):
        account = self.account_repository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")