# double underscore is used to make a variable private
# single underscore is used to indicate that a variable is protected
# Encapsulation is the concept of wrapping data and methods into a single unit
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self._balance = balance  # protected variable

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited: {amount}. New Balance: {self._balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew: {amount}. New Balance: {self._balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def getAccountNumber(self): # Getter method to access private variable
        return self.__account_number  

    def setAccountNumber(self, new_account_number): # Setter method to modify private variable
        self.__account_number = new_account_number  

    def getBalance(self):  # Getter method to access protected variable
        return self._balance
    def get_account_info(self):
        return f"Account Number: {self.__account_number}, Balance: {self._balance}"
    
    def get_account_info2(self):
        return f"Account Number: {self.getAccountNumber()}, Balance: {self.getBalance()}"   

# create an instance of BankAccount
account = BankAccount("123456789", 1000)    
# access account information using public method
print(account.get_account_info())
# deposit money     
print(account.deposit(500))
# withdraw money
print(account.withdraw(200))
# access private variable using getter
print("Account Number (using getter):", account.getAccountNumber()) 
# modify private variable using setter
account.setAccountNumber("987654321")   
print("Updated Account Number (using getter):", account.getAccountNumber())
# access protected variable using getter
print("Balance (using getter):", account.getBalance())  
# access account information using public method
print(account.get_account_info2())  
# trying to access private variable directly (will raise an error)
# print(account.__account_number)  # Uncommenting this line will raise an AttributeError    
# but we can access it using name mangling (not recommended)
print("Accessing private account number using name mangling:", account._BankAccount__account_number)

# trying to access protected variable directly (not recommended but possible)
print("Directly accessing protected balance:", account._balance)  # Possible but not recommended        
