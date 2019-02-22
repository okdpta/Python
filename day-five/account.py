def raise_error(message):
  raise ValueError(message)

class BankAccount :
    def _init_(self):
        self.balance = 0
        self.is_open = False 

    def get_balance(self):
        if self.is_open:
            return self.balance
        raise_error('Account Closed')

    def open(self):
        self.is_open = True

    def deposit(self, amount):
        if self.is_open:
            if amount > 0:
                self.balance += amount
                return self.balance
            raise_error('Can not deposit negative amount')
        raise_error('Can not deposit negative amount')

    def withdraw(self, amount):
        if self.is_open:
            # using >= instead of <= was breaking our code
            if amount <= self.balance:
                if amount > 0:
                    self.balance -= amount
                return self.balance
            raise_error('Can not withdraw negative amount')
            raise_error('Insufficient balance')
        raise_error('Account is closed')

    def close(self):
        self.is_open = False

