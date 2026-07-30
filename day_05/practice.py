





# # class Account:
# #     def __init__(self, owner, balance=0):
# #       self.owner = owner
# #       self.balance = balance
# #     def deposit(self, amount):
# #      self.balance += amount
# # class SavingsAccount(Account): # inherits
# #  pass



# # s = SavingsAccount("Almaz", 1500)
# # s.deposit(500)
# # print(f"The total Balance will be: {s.balance}") # 2000






# # # exercise 2 
# # class SavingsAccount(Account):
# #     def __init__(self, owner, number,
# #     balance=0, rate=0.05):
# #      super().__init__(owner, number, balance)
# #      self.rate = rate
# # def add_interest(self):
# #  interest = self.balance * self.rate
# #  self.deposit(interest) # reuse parent method


# # # run practice 2
# # s = SavingsAccount("Almaz", "CBE-1", 1500)
# # s.deposit(500) # inherited
# # s.add_interest() # new
# # print(s.ance)

    




# # class Animal:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def Move(self):
# #         print(self.name, self.age)
      


# # person1 = Animal("Surafel", 12)
# # person1.Move()





# # # 2 polymorphism
# # accounts = [
# #   Account("Hanna", "CBE-1", 1500),
# #   SavingsAccount("Almaz", "CBE-2", 1500),
# #  CurrentAccount("Dawit", "CBE-3", 800), # type: ignore
# # ]
# # for acc in accounts:
# #  acc.statement() # the right version 






# # the third example 
# def show_balance(item):
#   print(item.balance)
# show_balance(savings)
# show_balance(current)
# show_balance(wallet)



# abstruction in python 
# Abstraction means exposing what an object does, while hiding 
# how it does it.


# compostion and abstruction
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
class Cat(Animal):
   def move(self):
     print("Cat is moving")
class Horse(Animal):
  def run(self):
    print("horse is running ")


dog = Dog()
cat=Cat()
horse=Horse()
dog.eat()
dog.sleep()
dog.bark()
cat.move()
horse.run()