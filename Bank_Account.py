class BankAccount:
    def __init__(self, account_id, balance, owner):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance
    @property
    def owner(self):
        return self._owner

    @balance.setter
    def balance(self,value):
        if value < 0 or value > 1000000:
            raise ValueError("Invalid Balance")
        self._balance = value
    
    @owner.setter
    def owner(self,value):
        if value == "":
            raise ValueError
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Invalid Owner")
        self._owner = value
        return self._owner

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Invalid Amount")
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("Invalid Withdraw")
        self.balance = self.balance - amount
        return self.balance

    def __repr__(self):
        return f"BankAccount ({self.account_id}, {self.balance}, {self.owner})"
    def __str__(self):
        return f"Account {self.account_id} owned by {self.owner}: {self.balance}"
    def __eq__(self, other):
        if not isinstance(other,BankAccount):
            return NotImplemented
        return self.account_id == other.account_id

a = BankAccount(101, 5000, "John")
print((a))
a.withdraw(100)
print(a)