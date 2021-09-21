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
