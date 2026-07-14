# some exercis erelated today topics
# 1. class is the blue print of objects

class Human :
    def __init__(self,info, id, gpa):
        self.info=info
        self.id = id
        self.gpa = gpa
    
    def move(self):
        print(f"{self.info} {self.id}:{self.gpa}")
b=Human("welcome to my bootcamp",1,3.19)


# 
# excute the  class
print(b.move())

# class Account:
#     def __init__(self, owner, bal):
#         self.owner = owner
#         self.balance = bal
#     def deposit(self, amount):
#         self.balance += amount
# a = Account("Almaz", 1500)
# a.deposit(500)
# print(a.balance)



# the second class claass




class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
a=Animal.name="Tiger"
b=Animal.age=23

print(a,b)



# class 
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def statement(self):
        print(f"{self.owner}: {self.balance}")


almaz = Account("Almaz", 1500)
almaz.deposit(500)
almaz.withdraw(200)
almaz.statement()




# Encapsulation practce
print("============Encapsulation practice======")
class Account:
    def _init_(self,owner,balance=0):
        self.owner=owner
        self._balance=balance
    @property
    def balance(self):
        return self._balance
    def deposite(self,amount):
        if amount <=0 :
            raise ValueError("Must be positive")
        self. _balance +=amount
    a=Account("alamaz",1500)
    a.deposit(1500)
    print(a.balance)