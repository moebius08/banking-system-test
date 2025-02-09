from src.domains.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts: Account = {}

    def save_account(self, account: Account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id) -> Account:
        return self.accounts.get(account_id)
    def find_accounts_by_customer_id(self, customer_id):
        customer_accounts = []
        for account in self.accounts.values():
            if account.customer_id == customer_id:
                customer_accounts.append(account)
        return customer_accounts
    
    def get_next_account_id(self):
        if not self.accounts:
            return 1
        return max(int(account_id) for account_id in self.accounts.keys()) + 1