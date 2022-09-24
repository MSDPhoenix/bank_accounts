class BankAccounts:
    all_accounts = []
    def __init__(self,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccounts.all_accounts.append(self)

    def deposit(self,amount):
        print(f"Depositing ${amount}")
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance > 0:
            self.balance -= amount
            print(f"Withdrawing ${amount}")
            if self.balance < amount:
                print("Insufficient funds.  Charging $5 fee.")
                self.balance -= 5
        else:
            print("Insufficient funds. Transaction cancelled")
        return self

    def display_account_info(self):
        print(f"Interest rate: {self.int_rate}")
        print(f"Balance: {self.balance}\n")
        return self

    def yield_interest(self):
        x = self.balance * self.int_rate
        self.balance += x
        print(f"Interest: {x}, new balance: {self.balance}")
        return self

    @classmethod
    def print_all(cls):
        for account in BankAccounts.all_accounts:
            account.display_account_info()

account1 = BankAccounts(.02)
account1.deposit(100).deposit(200).deposit(50).withdraw(9).yield_interest().display_account_info()

account2 = BankAccounts(.03,300)
account2.deposit(500).deposit(750).withdraw(30).withdraw(25).withdraw(90).withdraw(1).yield_interest().display_account_info()

BankAccounts.print_all()