from src.domains.account import Account
from src.repositories.transaction_repository import TransactionRepository

class AccountStatementUseCase:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def generate_account_statement(self, account_id: str) -> str:
        transactions = self.transaction_repository.find_transactions_by_account_id(account_id)
        
        # Format the transactions into a statement string
        statement_lines = ["Account Statement:"]
        for transaction in transactions:
            line = f"Account ID {transaction['account_id']}: {transaction['transaction_type']} of {transaction['amount']}"
            statement_lines.append(line)
        
        return "\n".join(statement_lines)