# Arithmetic magic methods __add__, __sub__, __mul__, __truediv__.

class BankAccount:
    def __init__(self, name, balance):
        print('Create a new object via method __init__')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ method call')
        if isinstance(other, BankAccount):
            self.balance += other.balance
            return self.balance
        if isinstance(other, (int, float)):
            self.balance += other
            return BankAccount(self.name, self.balance)
    
    def __repr__(self):
        return f"A new client {self.name} has balance {self.balance}"
    

old_client = BankAccount('John', 1200)
print(f'A balance of old client is {old_client.balance}')
print(f'A memory address of old client is {id(old_client)}')
new_client = old_client + 100
print(f'A balance of new client is {new_client.balance}')
print(f'A memory address of new client is {id(new_client)}')
print(new_client)


