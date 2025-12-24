class BankAcc:
    def _init_ (self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit (self, amount):
        if amount < 0:
            return "Invalid Entry"
        else:
            self.balance += amount
            return self.balance
    def withdraw (self,amount):
        if amount > self.balance:
            return "Insufficient Funds!"
        else:
            self.balance  -= amount
            return  self.balance
    def get_balance (self):
        return "Account Balance:",self.balance
a1 = BankAcc("Sevita",24000)
print(a1.deposit(2065))
print(a1.withdraw(29000))
print(a1.withdraw(2000))
print("Current Balance:",a1.get_balance())
