# Example

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print("")

# Conditional Tests

car = "bmw"
print(car == "bmw")  # True
car = "audi"
print(car == "bmw")  # False
car = "Audi"
print(car == "audi")  # False (Python is case sensitive)
print(car.lower() == "audi")  # True

print("")

# Checking for Inequality

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

print("")

# Numerical Comparisons

age = 18
print(age == 18)  # True

answer = 17
if answer != 42:
    print("Wrong. Try again!")

age = 19
print(age < 21)  # True
print(age <= 21)  # True
print(age > 21)  # False
print(age >= 21)  # False

print("")

# Checking Multiple Conditions

"""
reference the document ./truth-table.md
"""

## AND

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # True

## OR

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)  # True
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)  # False

print("")

# Checking Whether a Value Is in a List

# Using the keyword 'in' to check if a value is in a list
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)  # True

# Using the keyword 'not in' to check if a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

print("")

# Boolean Expressions

game_active = True
can_edit = False

print("")

# if Statements

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("")

# if-else Statements

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("")

# The if-elif-else Chain

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

print("")

"""
The code below is the same as the previous one, 
but it uses a variable to store the price
"""

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
