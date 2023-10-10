class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("123456789", "Sujithra", 1000.0)

    # Display initial balance
    account.display_balance()

    # Deposit some money
    account.deposit(500)

    # Withdraw some money
    account.withdraw(200)

    # Attempt to withdraw an invalid amount
    account.withdraw(1500)

    # Display the final balance
    account.display_balance()

