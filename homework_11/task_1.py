import uuid
from decimal import Decimal
from datetime import datetime
from tabulate import tabulate


class Transaction:
    """
    Represents a financial transaction.

    Args:
        amount (str): The amount of money involved in the transaction.
        transact_type (str): The type of the transaction (e.g., 'Deposits' or 'Withdrawals').

    Attributes:
        amount (Decimal): The amount of money involved in the transaction.
        date (str): The date and time of the transaction in the format '%Y-%m-%d %H:%M:%S'.
        transact_type (str): The type of the transaction.
        fee (Decimal): The transaction fee, calculated as 1% of the transaction amount.

    Methods:
        __str__(): Returns a string representation of the transaction.
        __repr__(): Returns a string representation of the transaction.
    """
    def __init__(self, amount: str, transact_type: str):
        if type(transact_type) != str or type(amount) != str:
            raise TypeError("Amount/transact_type must be a string")
        self.amount = Decimal(amount)
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transact_type = transact_type
        self.fee = round(self.amount * Decimal('0.01'), 2)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.amount}|{self.fee}|{self.transact_type}|{self.date}"


class BankAccount:

    """
        Represents a bank account.

        Args:
            name (str): The name associated with the bank account.

        Attributes:
            id_acc (uuid.UUID): The unique identifier for the bank account.
            transactions (list): List of Transaction objects representing the account's transactions.
            name (str): The name associated with the bank account.
            balance (Decimal): The current balance of the bank account.

        Properties:
            transactions_history: Returns a formatted history of transactions using tabulate.

        Methods:
            deposits(amount): Deposits the specified amount into the account.
            withdrawals(amount): Withdraws the specified amount from the account.
        """

    def __init__(self, name: str):
        """
        Initialize a BankAccount instance.

        Args:
            name (str): The name associated with the bank account.
        """
        self.__id = uuid.uuid4()
        self.__name = name
        self.__balance = Decimal('0')
        self.__transactions = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Name: {self.name} | Account balance, USD: {self.balance}"

    @property
    def id_acc(self):
        """
        uuid.UUID4(): The unique identifier for the bank account.
        """
        return self.__id

    @property
    def transactions(self):
        """
        list: List of Transaction objects representing the account's transactions.
        """
        return self.__transactions

    @property
    def name(self):
        """
        str: The name associated with the bank account.
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Set a new name for the bank account.

        Args:
            new_name (str): The new name to set for the bank account.
        """
        self.__name = new_name

    @property
    def balance(self):
        """
        Decimal: The current balance of the bank account.
        """
        return self.__balance

    @property
    def transactions_history(self):
        """
        str: Returns a formatted history of transactions using tabulate.
        """
        header = ["Amount", "Comission", "Type of transaction", "Date and time"]
        data = [str(t).split('|') for t in self.__transactions]
        return tabulate(data, headers=header)

    def deposits(self, amount: str):
        """
        Deposit the specified amount of money into the account.

        Args:
            amount (str): The amount of money to deposit.
        """
        if Decimal(amount) <= Decimal('0'):
            raise ValueError("The sum can't be lesser than 0")
        transact = Transaction(amount, 'Deposits')
        self.__transactions.append(transact)
        transact.amount -= transact.fee
        self.__balance += transact.amount

    def withdrawals(self, amount: str):
        """
        Withdraw the specified amount of money from the account.

        Args:
            amount (str): The amount of money to withdraw.
        """
        if Decimal(amount) <= Decimal('0'):
            raise ValueError("The sum can't be lesser than 0")
        transact = Transaction(amount, 'Withdrawals')
        if Decimal(amount) + transact.fee > self.balance:
            raise ValueError("Insufficient balance")
        transact.amount += transact.fee
        self.__balance -= transact.amount
        self.__transactions.append(transact)


# Client code:
if __name__ == '__main__':
    user_misha = BankAccount("Misha Dev")
    try:
        user_misha.deposits('1000')
        user_misha.deposits('5')
        user_misha.withdrawals('100')
        user_misha.withdrawals('6')
        user_misha.deposits('300')
        user_misha.withdrawals('400')
    except ValueError as e:
        print(e)

    print(user_misha)
    print(user_misha.name)
    print(user_misha.id_acc)
    print(user_misha.balance)
    print(user_misha.transactions)
    print(user_misha.transactions_history)
