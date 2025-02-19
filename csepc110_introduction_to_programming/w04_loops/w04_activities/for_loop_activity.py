cities = ["Brazzaville", "Libreville", "Bamako", "Kinshasa", "Bangui", "Cape Town", "Kigali", "Nairobi", "Accra", "Lagos", ""]

for city in cities:
	print(city)
	
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

# range(start, stop, step)

for number in range(1, 11, 1):
    print(number)

for number in range(0,11,1):
    print(number)
# This is the same as the previous example, but the step is 1 by default
for number in range(11):
    print(number)

#list of some colors
colors = ["red", "blue", "green", "yellow"]

#Loop to display each color one by one
for color in colors:
	print(color)

#Loop to display the numbers 1–8, one number on each line
for i in range(1,9):
    print(i)

#Loop to display the even numbers (hint: count by two) 2–20, one number on each line
for i in range(2,22,2):
    print(i)

"""
Author: Brother Burton

Purpose: Practice using for loops.
"""

# 1. Iterate through a list of items
colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

print() # A blank line to make the output look nicer

# 2. Iterate through a list of numbers
for i in range(1, 9):
    print(i)

print() # A blank line to make the output look nicer

# 3. Iterate through even numbers

# Notice that we start at 2, go up through, but not including 21, and count by 2
for i in range(2, 21, 2):
    print(i)