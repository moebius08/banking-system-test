class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def save_transaction(self, transaction):
        self.transactions.append(transaction)

    def find_transactions_by_account_id(self, account_id):
        return [transaction for transaction in self.transactions if transaction['account_id'] == account_id]
    