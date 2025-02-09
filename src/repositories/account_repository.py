from domains.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts: Account = {}

    def save_account(self, account: Account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id) -> Account:
        return self.accounts.get(account_id)