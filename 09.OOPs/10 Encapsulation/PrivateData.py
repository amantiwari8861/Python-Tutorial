class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✅ Allowed
# print(account.__balance)    # ❌ AttributeError (private)
print(account._BankAccount__balance)   

# in python there is no truly concept of Private