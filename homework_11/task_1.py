import uuid
from decimal import Decimal
from datetime import datetime


class Transaction:

    def __init__(self, amount: str, transact_type: str):
        self.amount = Decimal(amount)
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transact_type = transact_type

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Transaction amount: {self.amount} | Type: {self.transact_type} | Date: {self.date}"


class BankAccount:

    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = Decimal('0')
        self.transactions = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"ID: {self.id} | Name: {self.name} | Account balance, USD: {self.balance}"

    def deposits(self, amount):
        transact = Transaction(amount, 'Deposit')
        self.transactions.append(transact)
        self.balance += transact.amount

    def withdrawals(self, amount):
        if Decimal(amount) <= Decimal('0'):
            raise ValueError("The sum can't be lesser than 0")
        if Decimal(amount) > self.balance:
            raise ValueError("Insufficient balance")
        transact = Transaction(amount, 'Withdrawals')
        self.transactions.append(transact)
        self.balance -= transact.amount

    def transactions_history(self):
        return '\n'.join([str(t) for t in self.transactions])


# Client code:
user_misha = BankAccount("Misha's bank account")

try:
    user_misha.deposits('850.78')
    user_misha.deposits('150.60')
    user_misha.deposits('67.40')
    user_misha.deposits('133.45')
    user_misha.withdrawals('122.43')
    user_misha.withdrawals('1222.43')
except ValueError as e:
    print(e)

print(user_misha)
print(user_misha.balance)
print(user_misha.transactions_history())

