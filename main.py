import sqlite3
import re
from bank_account import BankAccount

conn = sqlite3.connect('vinay.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS BankAccount (
                    holder_name TEXT,
                    phone_number TEXT,
                    account_number TEXT PRIMARY KEY,
                    balance REAL
                )''')

def insert_account(account):
    cursor.execute('''INSERT INTO BankAccount (holder_name, phone_number, account_number, balance)
                    VALUES (?, ?, ?, ?)''', (account.holder_name, account.phone_number, account.account_number, account.balance))
    conn.commit()

def get_account(account_number):
    cursor.execute('''SELECT * FROM BankAccount WHERE account_number=?''', (account_number,))
    return cursor.fetchone()

def generate_account_number(phone_number):
    last_four_digits = phone_number[-4:]
    return f"VBAC{last_four_digits}"

def create_account():
    holder_name = input("Enter your name: ")
    while True:
        phone_number = input("Enter your 10-digit phone number: ")
        if re.match(r'^\d{10}$', phone_number):  # Use the re module for pattern matching
            break
        else:
            print("Invalid phone number format. Please enter 10 digits.")
    account_number = generate_account_number(phone_number)
    balance = 500
    account = BankAccount(holder_name, phone_number, account_number, balance)
    insert_account(account)
    print(f"Account created successfully! Your account number is: {account_number}")

def deposit():
    account_number = input("Enter your account number: ")
    account = get_account(account_number)
    if account:
        amount = float(input("Enter the amount to deposit: "))
        account = BankAccount(*account)
        account.deposit(amount)
        cursor.execute('''UPDATE BankAccount SET balance=? WHERE account_number=?''',
                        (account.balance, account.account_number))
        conn.commit()
    else:
        print("Account not found.")

def withdraw():
    account_number = input("Enter your account number: ")
    account = get_account(account_number)
    if account:
        amount = float(input("Enter the amount to withdraw: "))
        account = BankAccount(*account)
        account.withdraw(amount)
        cursor.execute('''UPDATE BankAccount SET balance=? WHERE account_number=?''',
                        (account.balance, account.account_number))
        conn.commit()
    else:
        print("Account not found.")

def check_balance():
    account_number = input("Enter your account number: ")
    account = get_account(account_number)
    if account:
        print(f"Current balance for account {account[2]}: {account[3]}")
    else:
        print("Account not found.")

while True:
    print("\n1) Create Account")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Check Balance")
    print("5) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

conn.close()
