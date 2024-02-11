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

# reference ./truth-table.md
