magicians = ["alice", "david", "carolina"]
for magician in magicians:  # for each magician in the list of magicians
    print(magician)  # print the name of the magician

i = 0

for magician in magicians:
    current_magician = magicians[i]
    if (
        # if the index equals the length of the list of magicians minus 1
        i == len(magicians) - 1
    ):
        next_magician = magicians[0]  # the next magician is the first one
    else:
        next_magician = magicians[i + 1]  # otherwise, the next magician is the next one
    print(f"{current_magician} is next to {next_magician}")
    i += 1

# ----------------------------------------------

## Range function

for value in range(1, 5):  # for each value in the range of 1 to 5 (not including 5)
    print(value)

numbers = list(range(1, 6))  # create a list of numbers from 1 to 5
print(numbers)

even_numbers = list(range(2, 11, 2))  #  third argument is the step value
mult_of_five = list(range(0, 11, 5))
print(even_numbers)
print(mult_of_five)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

## Statistics

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

## List Comprehensions

squares = [value**2 for value in range(1, 11)]  # expression then for loop, no colons
print(squares)

mults_of_three = [value * 3 for value in range(1, 11)]  # multiples of 3
print(mults_of_three)
mults_of_three = [value for value in range(3, 31, 3)]  # another variet of above
print(mults_of_three)
# mults_of_three = [value for value in range(6, 31, 1.5)] cant use floats as steps

odd_num_20 = [value for value in range(1, 20, 2)]
print(odd_num_20)

""" num_one_million = [value for value in range(1, 100_000_001)] # This will take a sec
print(min(num_one_million))
print(max(num_one_million))
print(sum(num_one_million)) """

# ----------------------------------------------

## Working with parts of a list

### Slicing a list [start:end], not including the end index

players = ["charles", "martina", "michael", "florence", "eli"]
print(f"All: {players}")  # print all players
print(f"First three: {players[0:3]}")  # print the first three players
print(f"2nd to 4th: {players[1:4]}")  # print the second through fourth players
print(f"First three: {players[:3]}")  # omitting start index, start = 0
print(f"Last three: {players[2:]}")  # omitting the end index, end = end of list
(f"Last three: {players[-3:]}")  # print the last three players
print(f"First three: {players[:-3]}")  # print all but the last three players

### Looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

### Copying a list

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]  # copy the list
my_foods.append("cannoli")  # add an item to my list
friends_foods.append("ice cream")  # add an item to friends list
print(f"My favs: {my_foods}")
print(f"Friends favs: {friends_foods}")

""" 
The following will not work as intended.
It will create a reference to the original list.
So the two lists will be the same.
If you want to create a copy of a list, 
you can use the slice notation, as above.
"""

my_fav_games = ["mario", "zelda", "pokemon"]
friends_fav_games = my_fav_games
my_fav_games.append("smash")
friends_fav_games.append("mario kart")
print(f"My fav games: {my_fav_games}")
print(f"Friends fav games: {friends_fav_games}")  # same list

# ----------------------------------------------

## Tuples
