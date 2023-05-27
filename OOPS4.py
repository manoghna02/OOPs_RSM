#4. Bank Class
class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
 
class Bank:
    def __init__(self):
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
        print("Account "+account.account_number+" is added")
    def remove_account(self,account_number):
        for account in self.accounts:
            if account.account_number==account_number:
                self.accounts.remove(account)
                print("Account "+account_number+" is removed")
    def total_balance(self):
        total_bal=sum(account.balance for account in self.accounts)
        print("Total balance is:",total_bal)

myBank=Bank()

account1 = Account("A1", 500)
myBank.add_account(account1)
account2 = Account("A2", 1000)
myBank.add_account(account2)
account3 = Account("A3", 1500)
myBank.add_account(account3)
myBank.total_balance()
myBank.remove_account("A1")
myBank.total_balance()


