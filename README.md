# PDAX Test

## Architecture

The application follows simple clean architecture and is divided into three layers:

1. **Domain Layer**: Contains entities representing domain concepts such as `Account`, `Transaction`, and `Customer`. These entities have methods for operations related to their domains.

2. **Use Case Layer**: Contains business logic for the application. It includes use cases such as creating accounts (`CreateAccountUseCase`), making transactions (`TransactionUseCase`), and generating account statements (`AccountStatementUseCase`).

3. **Infrastructure Layer**: Responsible for interacting with external systems and services. includes repositories for persisting and retrieving data, such as `AccountRepository` and `TransactionRepository`.

## Setup

1. **Requirements**:
   - Python 3.x
   - `pytest` for testing

2. **Installation**:
   - Clone the repository.
   - Navigate to the project directory.
   - Set up a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies if applicable.

3. **Running the Application**:
   - Execute `main.py` to run a sample scenario:
     ```bash
     python main.py
     ```

4. **Running Tests**:
   - Use `pytest` to run the unit tests:
     ```bash
     pytest tests/transaction_test_case.py
     ```

## Project Structure

- `src/domains`: Contains domain entities (`Account`, `Transaction`, `Customer`).
- `src/services`: Contains use case implementations (`CreateAccountUseCase`, `TransactionUseCase`, `AccountStatementUseCase`).
- `src/repositories`: Contains repository implementations for accounts and transactions.
- `tests`: Contains unit tests for application functionalities.