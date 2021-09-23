# Duplicate code example
print("Good morning!")
print("How are you feeling?")
feeling = input()
print("I am happy to hear that you are feeling " + feeling + ".")
print("Good afternoon!")
print("How are you feeling?")
feeling = input()
print("I am happy to hear that you are feeling " + feeling + ".")
print("Good evening!")
print("How are you feeling?")
feeling = input()
print("I am happy to hear that you are feeling " + feeling + ".")

# How to fix code above by using a function
def askFeeling():
    print("How are you feeling?")
    feeling = input()
    print("I am happy to hear that you are feeling " + feeling + ".")


print("Good morning!")
askFeeling()
print("Good afternoon!")
askFeeling()
print("Good evening!")
askFeeling()

# How to fix using a loop
for timeOfDay in ["morning", "afternoon", "evening"]:
    print("Good " + timeOfDay + "!")
    print("How are you feeling?")
    feeling = input()
    print("I am happy to hear that you are feeling " + feeling + ".")

# Using a function and a loop
def askFeeling(timeOfDay):
    print("Good " + timeOfDay + "!")
    print("How are you feeling?")
    feeling = input()
    print("I am happy to hear that you are feeling " + feeling + ".")


for timeOfDay in ["morning", "afternoon", "evening"]:
    askFeeling(timeOfDay)

# Magic Numbers
# Consider how this could confuse a programmer
import time

expiration = time.time() + 604800

# Set up constants for different time amounts
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
SECONDS_PER_WEEK = 7 * SECONDS_PER_DAY

expiration = time.time() + SECONDS_PER_WEEK

# Deck of cards vs Years
NUM_CARDS_IN_DECK = 52
NUM_WEEKS_IN_YEAR = 52

print("This deck contains", NUM_CARDS_IN_DECK, "cards.")
print("This 2 year contract lasts for", 2 * NUM_WEEKS_IN_YEAR, "weeks.")

# Find the bug
while True:
    print('Set solar panel direction:')
    direction = input().lower()
    if direction in ('north', 'south', 'east', 'west'):
        break

print('Solar panel heading set to:', direction)
1 if direction == 'nrth':
    print('Warning: Facing north is inefficient for this panel.')


# Set up constants for each cardinal direction:
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

while True:
    print('Set solar panel direction:')
    direction = input().lower()
    if direction in (NORTH, SOUTH, EAST, WEST):
        break

print('Solar panel heading set to:', direction)
1 if direction == NRTH:
    print('Warning: Facing north is inefficient for this panel.')

# Example of dead code, code inside a fucntion but after a return
import random
def coinFlip():
    if random.randint(0, 1):
        return 'Heads!'
    else:
        return 'Tails!'
    return 'The coin landed on its edge!'

    print(coinFlip())
Tails!

# Example of unimplemented
def exampleFunction():
    pass

# Logging example
import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

# Java users are used to creating classes to organise their program’s code
import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

d = Dice()
print('You rolled a', d.roll())
You rolled a 1

# Above can be replaced with a simple function call
print('You roleed a', random.randint(1, 6))

# List Comprehensions Within List Comprehensions
spam = []
for number in range(100):
    if number % 5 != 0:
        spam.append(str(number))
print(spam)

spam = {str(number) for number in range(100) if number % 5!= 0}
print(spam)

spam = {str(number): number for number in range(100) if number % 5 !=0}
print(spam)

# Nested list comprehensions
nestedIntList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
nestedStrList = []
for sublist in nestedIntList:
    nestedStrList.append{(str(i) for i in sublist)}
print(nestedIntList)

# Two loops same flattened list
nestedList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
flatList = []
for sublist in nestedList:
    for num in sublist:
        flatList.append(num)
print(flatList)

# Using except blocks to catch exceptions, using a pass with except block can do nothing
try:
    num = input('Enter as number: ')
    num = int(num)
except ValueError:
    pass
# Enter a number: 42
print(num)
'forty two'

# Handling exceptions with poor error messages is another code smell. Look at this example:
try:
    num = input('Enter a number: ')
    num = int(num)
except ValueError:
    print('An incorrect value was passed to int()')
# Enter a number: 42
# An incorrect number was passed to int()

# Function that indicates whether a file we want to delete is already nonexistent:
import os
def deleteWithConfirmation(filename):
    try:
        if (input('Delete ' + filename + ', are you sure? Y/N') == 'Y'):
            os.unlink(filename)
    except FileNotFoundError:
        print('That file already did not exist.')

# Proponents of this code smell myth argue that because functions should always do just one thing, and error handling is one thing, we should split this function into two functions. They argue that if you use a try-except statement, it should be the first statement in a function and envelop all of the function’s code to look like this:
import os
def handleErrorForDeleteWithConfirmation(filename):
    try:        
        _deleteWithConfirmation(filename)
    except FileNotFoundError:
        print('That file already did not exist.')

def _deleteWithConfirmation(filename):
    if (input('Delete ' + filename + ', are you sure? Y/N') == 'Y'):
        os.unlink(filename)

# Example of Flag Arguements
def someFunction(flagArgument):
    if flagArgument:
        # Run some code...
    else:
        # Run some completely different code...
