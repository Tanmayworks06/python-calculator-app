class bankaccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance += amt 
        print(f"deposited: ${amt} , new balance: ${self.balance}")

    def withdraw(self,amt):
        if amt > self.balance:
            print("insufficient funds !")
        else:
            self.balance -= amt
            print(f"withdrew: ${amt} , new balance: {self.balance}")

    def __str__(self):
        return f"account holder ({self.name} , ${self.balance})"

account = bankaccount("Tanmay",10000)
print(account)
account.deposit(5000)
account.withdraw(5000)