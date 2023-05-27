#2. Banking System Class Hierarchy
class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit amount:',amount)
        print('Total balance:',self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print('Withdraw amount:',amount)
            print('Total balance:',self.balance)
        else:
            print("insufficient funds")
class SavingsAccount(Account):
    def __init__(self,account_number,balance,interest_rate):
        self.account_number=account_number
        self.balance=balance
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=(self.balance*self.interest_rate)/100
        print("Interest:", interest)
class CheckingAccount(Account):
    def __init__(self,account_number,balance,overdraft_limit):
        self.account_number=account_number
        self.balance=balance
        self.overdraft_limit=overdraft_limit
    def apply_overdraft(self,amount):
        if amount<=self.balance+self.overdraft_limit:
            self.balance=self.balance-amount
            print("Balance:",self.balance)
        else:
            print("overdraft limit exceeded")
    
print("John's account details")            
johnSavings=SavingsAccount(15431,1000,5)
johnSavings.deposit(100)
johnSavings.withdraw(200)
johnSavings.calculate_interest()

print("Jane's account details") 
janeChecking=CheckingAccount(18909,2000,500)
janeChecking.deposit(100)
janeChecking.withdraw(200)
janeChecking.apply_overdraft(100)