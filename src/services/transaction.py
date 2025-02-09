from src.repositories.account_repository import AccountRepository
from src.repositories.transaction_repository import TransactionRepository
from src.domains.transaction import Transaction

class TransactionUseCase:

    def __init__(self, account_repository: AccountRepository, transaction_repository: TransactionRepository):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def make_transaction(self, transaction: Transaction):
        account = self.account_repository.find_account_by_id(account_id=transaction.account_id)
        
        if transaction.transaction_type == 'deposit':
            account.deposit(transaction.amount)
        elif transaction.transaction_type == 'withdraw':
            account.withdraw(transaction.amount)
        else:
            raise ValueError("Invalid transaction type")
        self.account_repository.save_account(account)
        self.transaction_repository.save_transaction({
            'account_id': transaction.account_id,
            'transaction_type': transaction.transaction_type,
            'amount': transaction.amount,
        })