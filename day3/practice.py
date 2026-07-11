# cities =["Addis Ababa", "Adama","Hawassa","Bahir Dar","Gondar","Mekele","Dire Dawa","Jijiga","Jimma","Dessie"]
# print(cities[0])
# print(cities[1])
# print(cities[2])
# print(cities[3])
# print(cities[4])
# print(cities[5])
# print(cities[6])
# print(cities[7])
# print(cities[8])
# print(cities[9])

# # Loop through all cities
# for city in cities:
#     print(city)
    
    
# # common list methods
# print(len(cities))  # Get the number of cities
# print(cities[0:5])  # Get the first five cities
# print(cities[-1])   # Get the last city
# print(cities.index("Gondar"))  # Get the index of a specific city
# print("Gondar" in cities)  # Check if a city is in the list
# print(cities.count("Addis Ababa"))  # Count occurrences of a city
# print(cities.sort())  # Sort the cities alphabetically
# print(cities.pop())  # Print and remove the last city from the list
# print(cities.remove("Adama"))  # Remove a specific city from the list
# print(cities.insert(1, "Bishoftu")) 
# print(cities.append("Shashemene"))


# # list methods
# numbers = [1, 2, 3, 4, 5]
# # insert a number at a specific index
# numbers.insert(2, 10)  # Insert 10 at index 2
# print(numbers)  # Output: [1, 2, 10, 3, 4, 5]


# # for loop in python
# for i in range(1, 10):
#     print(i)
    
    
#     # the second for loop
#     totals =[]
#     for price in (100, 250, 400):
#         totals.append(price * 15)
#         print(totals)
        
        
#         # tuple vs list
#         # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#         # A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
#         # 
#     frainds = ("John", "Jane", "Doe")  # This is a tuple
#     print(frainds[0])  # Accessing elements in a tuple
#     frainds[0] = "Mike"  # This will raise an error because tuples are immutable
    
#     location =(9.03, 38.74)
#     lat, lon = location  # Unpacking the tuple into two variables
#     location[0] = 10.00  # This will raise an error because tuples are immutable
    
    
    
#     # 4 
    
    
#     # lists are mutable, meaning you can change their content
#     my_list = [1, 2, 3, 4, 5]
#     print(my_list)  # Output: [1, 2, 3, 4, 5]
#     my_list[0] = 10  # Changing the first element
#     print(my_list)  # Output: [10, 2, 3, 4, 5]
    
    
    
# dictionaries are mutable, meaning you can change their content
# customer = {
#     "name": "Biruk lakew",
#     "age": 30,
#     "city": "Addis Ababa"
# }
# print(customer)  # Output: {'name': 'Biruk lakew', 'age': 30, 'city': 'Addis Ababa'}
# customer["age"] = 31  # Changing the age
# print(customer)  # Output: {'name': 'Biruk lakew', 'age': 31, 'city': 'Addis Ababa'}




# Iterating a dictionary
from dataclasses import field


price = {"Bread": 2.5, "apple": 1.2, "banana": 0.8, "orange": 1.5}
for fruit, p in price.items():
    print(f"The price of {fruit} is ${p}")
    
    
# countrie and city dictionary
countries = {
    "Ethiopia": ["Addis Ababa", "Gondar", "Jimma"],
    "Kenya": ["Nairobi", "Mombasa", "Kisumu"],
    "Tanzania": ["Dodoma", "Mwanza", "Arusha"]
}
for country, cities in countries.items():
    print(f"The cities in {country} are: {', '.join(cities)}")
    
    # country.keys()  # Get all the country names
    # countries.values()  # Get all the cities in the countries
    # "Kenya" in countries  # Check if a country is in the dictionary
    
    
    # Sets — unique collections
    nums=[1, 2, 3, 4, 5, 1, 2, 3]
    unique_nums=set(nums)
    print(unique_nums)  # Output: {1, 2, 3, 4, 5}
    
    
    # Set operations
    a={1, 2, 3, 4}
    b={3, 4, 5, 6}
    print(a & b)  # Intersection: {3, 4}
    print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
    print(a - b)  # Difference: {1, 2}
    
    
    
#     list [ ] Ordered, changeable, duplicates allowed. A queue of customers.
# tuple ( ) Ordered, fixed. A coordinate or a fixed record.
# dict {k: v} Key-value lookup, keys unique. A profile by field name.


# exception handling
try:
    x = 10 / 0

    print(x)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
# the second example of exception handling
try:
    y = int("not a number")
    print(y)
except ValueError:
    print("Invalid input. Please enter a valid number.")