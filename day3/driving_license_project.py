# input to keyboard 

name=input("Enter your name: ")
age=int(input("Enter your age: "))
education=int(input("Enter your education: "))
# hints
# age must be  at least 18 years and over
# education must be at leat bachlor of degree and above
# name must be a string  and not empty



def driving_eligibility(age, education):
    try:
        age = int(age)
    except ValueError:
        print("Invalid age input. Please enter a valid number.")
        return False

    if age >= 18 and education >= 8:
        print(f"{name} is eligible to drive.")
        return True
    else:
        print(f"{name} is not eligible to drive.")
        return False

driving_eligibility(age, education)
  
