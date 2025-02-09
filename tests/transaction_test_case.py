import pytest
from src.domains.account import Account
from src.domains.transaction import Transaction, TransactionType
from src.repositories.account_repository import AccountRepository
from src.repositories.transaction_repository import TransactionRepository
from src.services.transaction import TransactionUseCase
from src.services.create_account import CreateAccountUseCase
from src.services.account_statement import AccountStatementUseCase

@pytest.fixture
def setup_repositories():
    account_repository = AccountRepository()
    transaction_repository = TransactionRepository()
    create_account_use_case = CreateAccountUseCase(account_repository)
    transaction_use_case = TransactionUseCase(account_repository, transaction_repository)
    account_statement_use_case = AccountStatementUseCase(transaction_repository)
    return account_repository, transaction_repository, create_account_use_case, transaction_use_case,account_statement_use_case

def test_deposit_transaction(setup_repositories):
    account_repository, _, create_account, transaction_use_case, _ = setup_repositories
    
    account = create_account.create_account("123", "John Doe", "john@example.com", "555-1234")
    
    transaction = Transaction(account_id=account.account_id, amount=100.0, transaction_type='deposit')
    transaction_use_case.make_transaction(transaction)
    
    updated_account = account_repository.find_account_by_id(account.account_id)
    assert updated_account.balance == 100.0

def test_withdraw_transaction(setup_repositories):
    account_repository, _, create_account, transaction_use_case,_ = setup_repositories
    
    account = create_account.create_account("456", "Jane Doe", "jane@example.com", "555-5678")
    deposit_transaction = Transaction(account_id=account.account_id, amount=200.0, transaction_type='deposit')
    transaction_use_case.make_transaction(deposit_transaction)
    
    withdraw_transaction = Transaction(account_id=account.account_id, amount=50.0, transaction_type='withdraw')
    transaction_use_case.make_transaction(withdraw_transaction)
    
    updated_account = account_repository.find_account_by_id(account.account_id)
    assert updated_account.balance == 150.0

def test_withdraw_insufficient_funds(setup_repositories):
    account_repository, _, create_account, transaction_use_case,_ = setup_repositories
    
    account = create_account.create_account("789", "John Smith", "smith@example.com", "555-9876")
    deposit_transaction = Transaction(account_id=account.account_id, amount=50.0, transaction_type='deposit')
    transaction_use_case.make_transaction(deposit_transaction)
    
    withdraw_transaction = Transaction(account_id=account.account_id, amount=100.0, transaction_type='withdraw')
    with pytest.raises(ValueError, match="Insufficient funds"):
        transaction_use_case.make_transaction(withdraw_transaction)
    
    updated_account = account_repository.find_account_by_id(account.account_id)
    assert updated_account.balance == 50.0

def test_create_account(setup_repositories):
    account_repository, _, create_account, _, _ = setup_repositories
    
    account = create_account.create_account("123", "John Doe", "john@example.com", "555-1234")
    
    assert account.account_id == 1
    assert account.customer_id == "123"
    assert account.balance == 0.0
    
    updated_account = account_repository.find_account_by_id(account.account_id)
    assert updated_account.account_id == 1
    assert updated_account.customer_id == "123"
    assert updated_account.balance == 0.0

    get_accounts_by_customer_id = account_repository.find_accounts_by_customer_id("123")
    
    assert get_accounts_by_customer_id[0].account_id == 1
    assert get_accounts_by_customer_id[0].customer_id == "123"
    assert get_accounts_by_customer_id[0].balance == 0.0

def make_a_deposit_by_customer_id(setup_repositories):
    account_repository, transaction_repository, create_account, transaction_use_case, _ = setup_repositories
    account = create_account.create_account("123", "John Doe", "john@example.com", "555-1234")
    #find by customer id
    get_accounts_by_customer_id = account_repository.find_accounts_by_customer_id("123")
    #get the first account and the accound id
    account = get_accounts_by_customer_id[0]['account_id']
    customer_transaction = Transaction(account_id=account, amount=100.0, transaction_type='deposit')
    transaction_use_case.make_transaction(customer_transaction)
    #Check if the transaction is saved in the account
    updated_account = account_repository.find_account_by_id(account)
    assert updated_account['balance'] == 100.0

def test_next_account_id(setup_repositories):
    account_repository, _, create_account, _,_ = setup_repositories
    next_id = account_repository.get_next_account_id()
    assert next_id == 1
    #Create an account
    account = create_account.create_account("789", "John Smith", "smith@example.com", "555-9876")
    next_next_id = account_repository.get_next_account_id()
    assert next_next_id == 2

def test_generate_account_statement(setup_repositories):
    account_repository, transaction_repository, create_account, transaction_use_case,account_statement_use_case = setup_repositories
    #Create an account
    account = create_account.create_account("789", "John Smith", "smith@example.com", "555-9876")
    #Make a transaction (Deposit)
    deposit_transaction = Transaction(account_id=account.account_id, amount=100.0, transaction_type='deposit')
    transaction_use_case.make_transaction(deposit_transaction)
    #Make another transaction (Withdraw)
    withdraw_transaction = Transaction(account_id=account.account_id, amount=50.0, transaction_type='withdraw')
    transaction_use_case.make_transaction(withdraw_transaction)
    statement = account_statement_use_case.generate_account_statement(account.account_id)
    #Initialize the expected statement
    expected_statement = (
        "Account Statement:\n"
        f"Account ID {account.account_id}: deposit of 100.0\n"
        f"Account ID {account.account_id}: withdraw of 50.0"
    )

    assert statement == expected_statement
