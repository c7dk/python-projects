# 1. simplest class

class MyClass:
    def show(self):
        self.name = 'foo'
        print('this is my class')

mc = MyClass()
print(type(mc))
mc.show()
print(mc.name)


# 2. bank customer

class BankCustomer(object):
    def __init__(self, name='No body', balance=0.0):
        self.name = name
        self.balance = balance

    def put_money_in(self, amount):
        self.balance = self.balance + amount

    def take_money_out(self, amount):
        if(self.balance - amount < 0):
            print('Cannot take money out more than your balance')
            print('Request to take money out is rejected')
        else:
            self.balance = self.balance - amount


will = BankCustomer()
print(type(will))
print(will.name)
will.name = 'Will Smith'
print(will.name)
print(will.balance)

will.put_money_in(50)
print(will.balance)

will.take_money_out(1000)
print(will.balance)

grace = BankCustomer('Grace Park', 4000)
print(grace.name)
print(grace.balance)

grace.take_money_out(6000)
print(grace.balance)
