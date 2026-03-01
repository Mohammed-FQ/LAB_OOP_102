class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        if not account_holder:
            raise ValueError("Account holder name cannot be empty")
        self.__account_holder = account_holder
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return f"After deposit: ${self.__balance:.2f}"
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return f"After withdrawal: ${self.__balance:.2f}"
        
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder

    def __str__(self):
        return f"Bank Account Info:-\n\nAccount Holder: {self.__account_holder}\nBalance: ${self.__balance:.2f}\n"