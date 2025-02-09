from enum import Enum

class TransactionType(Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'

class Transaction:
    def __init__(self, account_id: str, amount: float, transaction_type: TransactionType):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type