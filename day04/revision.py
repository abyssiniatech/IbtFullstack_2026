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