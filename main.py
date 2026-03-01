from bank import BankAccount
def main():
    account = BankAccount("Khalid", 0)
    print(account)
    #print("Try to withdraw $1500 from the account:")
    #print(account.withdraw(1500))
    print("Try to deposit $500 into the account:")
    print(account.deposit(500))
    print("Try to withdraw $200 from the account:")
    print(account.withdraw(200))

    print("Trying getters:")
    print(f"Account Holder from getter method: {account.get_account_holder()}")
    print(f"Balance from getter method: ${account.get_balance():.2f}")
    
    account.__balance = 1000000
    print(account)
if __name__ == "__main__":
    main()