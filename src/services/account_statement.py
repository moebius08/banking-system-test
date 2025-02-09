from domains.account import Account

class AccountStatementUseCase:
    def generate_account_statement(self, account: Account):
        statement = f"Account ID: {account.account_id}\nBalance: {account.get_balance()}"
        return statement