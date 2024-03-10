import sqlite3
import re

class BankAccount:
    def __init__(self, holder_name, phone_number, account_number, balance=0):
        self.holder_name = holder_name
        self.phone_number = phone_number
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            elif amount > 20000:
                raise ValueError("Deposit amount cannot exceed 20000.")
            else:
                self.balance += amount
                print(f"Deposited {amount} into account {self.account_number}.")
        except ValueError as e:
            print(str(e))

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            elif amount > 10000:
                raise ValueError("Withdrawal amount cannot exceed 10000.")
            elif self.balance < amount:
                raise ValueError("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}.")
        except ValueError as e:
            print(str(e))

    def display_balance(self):
        print(f"Current balance for account {self.account_number}: {self.balance}")
