from src.services.create_account import CreateAccountUseCase
from src.services.account_statement import AccountStatementUseCase
from src.services.transaction import TransactionUseCase
from src.domains.transaction import Transaction
from src.repositories.account_repository import AccountRepository
from src.repositories.transaction_repository import TransactionRepository

def main():
    #Initialize repositories
    account_repository = AccountRepository()
    transaction_repository = TransactionRepository()
    #Initialize Use Case with repositories
    transaction_use_case = TransactionUseCase(account_repository, transaction_repository)
    create_account_use_case = CreateAccountUseCase(account_repository)
    #Create three Accounts
    account1 = create_account_use_case.create_account("123456", "Kim", "adrian@gmail.com", "091234567832")
    account1_id = account1.account_id
    account2 = create_account_use_case.create_account("654321", "Adrian", "kim@gmail.com", "0912345678342")
    account2_id = account2.account_id
    account3 = create_account_use_case.create_account("789456", "Kimmy", "adrian@gmail.com", "0912321457832")
    account3_id = account3.account_id
    #Create Account with same Customer ID
    account4 = create_account_use_case.create_account("789456", "Kimmy", "adrian@gmail.com", "0912321457832")
    #Save the Account to the repository
    account_repository.save_account(account1)
    account_repository.save_account(account2)
    account_repository.save_account(account3)
    #Create Transaction Model for Deposit
    transaction1 = Transaction(account_id=account1_id, amount=178.2, transaction_type="deposit")
    transaction2 = Transaction(account_id=account2_id, amount=42.42, transaction_type="deposit")
    transaction3 = Transaction(account_id=account3_id, amount=312, transaction_type="deposit")
    transaction4 = Transaction(account_id=account2_id, amount=250, transaction_type="deposit")
    #Make a Transaction to ther account(Deposit)
    transaction_use_case.make_transaction(transaction1)
    transaction_use_case.make_transaction(transaction2)
    transaction_use_case.make_transaction(transaction3)
    transaction_use_case.make_transaction(transaction4)
    #Create Transaction Model for Deposit
    transaction5 = Transaction(account_id=account1_id, amount=100, transaction_type="withdraw")
    transaction6 = Transaction(account_id=account2_id, amount=100, transaction_type="withdraw")
    transaction7 = Transaction(account_id=account3_id, amount=100, transaction_type="withdraw")
    transaction8 = Transaction(account_id=account2_id, amount=100, transaction_type="withdraw")
    #Make a Transaction to ther account(Withdraw)
    transaction_use_case.make_transaction(transaction5)
    transaction_use_case.make_transaction(transaction6)
    transaction_use_case.make_transaction(transaction7)
    transaction_use_case.make_transaction(transaction8)

    #Generate an Account Statement
    statement_use_case = AccountStatementUseCase(transaction_repository)
    statement = statement_use_case.generate_account_statement(account3_id)
    print(statement)
    #Find account by customer_id
    accounts = account_repository.find_accounts_by_customer_id("654321")
    for account in accounts:
        print(str(account))

if __name__ == "__main__":
    main() 