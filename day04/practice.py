
# # List revision
fruits=["apple","Banana","Orange","Ananas"]
# print(fruits)
# # list is orderd ,chnagable and duplicte 

# 2 list methods   append methods
print(fruits.append("surafel"))
print(fruits)

# 3 remove methods in python
fruits.remove("Banana")
print(fruits)

# sort method in  python 

numbers=[10,2,34,3,45,4]
numbers.sort()
print(numbers)


# the second data structure is tupple 
# tuplle can not chnage the items of the data
colors=("red","blue","green")
# colors[1]="yellow"

# colors.sort()
print(colors)


# Use tuples for

# Coordinates
# Months
# Fixed value




# sets
# set removes duplicate 
nums={1,3,5,3,2,34,45}
nums.add(0)
print(nums)


# dictionries
# is key + values
students={
    "name":"surafel",
     "age": 23,
     "email":"surafelmengist"
}
print(students)




# revision
students = {}

while True:
    print("\nStudent Manager")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        students[name] = age

    elif choice == "2":
        if students:
            for name, age in students.items():
                print(f"{name} - {age}")
        else:
            print("No students found.")

    elif choice == "3":
        try:
            with open("students.txt", "w") as file:
                for name, age in students.items():
                    file.write(f"{name},{age}\n")
            print("Students saved successfully.")
        except Exception as e:
            print("Error:", e)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")







# # some exercis erelated today topics
# # 1. class is the blue print of objects

# class Human :
#     def __init__(self,info, id, gpa):
#         self.info=info
#         self.id = id
#         self.gpa = gpa
    
#     def move(self):
#         print(f"{self.info} {self.id}:{self.gpa}")
# b=Human("welcome to my bootcamp",1,3.19)


# # without oop concepts
# # Accounts={
# #     "balanc":300,
# #     "owner":"aster"
# # }
# # def deposite(Acc,amount):
# #     Acc["balanc"]+=amount
# # result=deposite(Accounts,3000)
# # print(result)
    
    
    
# accounts = {
#     "balanc": 300,
#     "owner": "aster"
# }

# def deposit(acc, amount):
#     acc["balanc"] += amount

# deposit(accounts, 3000)

# print(accounts)



# # 
# # excute the  class
# print(b.move())

# # class Account:
# #     def __init__(self, owner, bal):
# #         self.owner = owner
# #         self.balance = bal
# #     def deposit(self, amount):
# #         self.balance += amount
# # a = Account("Almaz", 1500)
# # a.deposit(500)
# # print(a.balance)



# # the second class claass




# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# a=Animal.name="Tiger"
# b=Animal.age=23

# print(a,b)



# # class 
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount

#     def statement(self):
#         print(f"{self.owner}: {self.balance}")


# almaz = Account("Almaz", 1500)
# almaz.deposit(500)
# almaz.withdraw(200)
# almaz.statement()




# # Encapsulation practce
# print("============Encapsulation practice======")
# class Account:
#     def _init_(self,owner,balance=0):
#         self.owner=owner
#         self._balance=balance
#     @property
#     def balance(self):
#         return self._balance
#     def deposite(self,amount):
#         if amount <=0 :
#             raise ValueError("Must be positive")
#         self. _balance +=amount
#     a=Account("alamaz",1500)
#     a.deposit(1500)
#     print(a.balance)
    
    
    
    
    
    
    
    
    # mini lab projects
    
print("==========mini projects==========")
class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        self.balance -= amount

    def statement(self):

        print(f"""
Owner   : {self.owner}
Balance : {self.balance} ETB
""")
        
        # run the program
account = Account("Surafel",5000)

account.deposit(1000)

account.withdraw(700)

account.statement()