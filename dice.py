"""
python dice.py -> roll one 6-sided die
python dice.py 2d6 -> roll two 6-sided die
python dice.py 10 -> 1 to 10, inclusive
python dice.py 5 10 -> 5 to 10, inclusive
python dice.py alice bob carol -> randomly select one of alice bob carol
"""

import random, sys

def rollDice(numberOfDice, numberOfSides):
    total = 0
    for i in range(numberOfDice):
        total += random.randint(1, numberOfSides)
    return total

# Figure out what the command line arguments are asking for:
if len(sys.argv) == 1:
    # No command line arguments were given, so roll 1d6:
    print(rollDice(1, 6))
elif len(sys.argv) == 2:
    # One command line argument was given.
    theArg = sys.argv[1].lower()  # Use this name to make our code more readable.
    if theArg.isdecimal():
        # theArg is a number, so return a number from 1 to theArg:
        print(random.randint(1, int(theArg)))
    else:
        if 'd' in theArg:
            firstPart = theArg.split('d')[0]
            secondPart = theArg.split('d')[1]
            if firstPart.isdecimal() and secondPart.isdecimal():
                # theArg is 1d6-style dice notation, so roll the dice:
                print(rollDice(int(firstPart), int(secondPart)))
elif len(sys.argv) == 3:
    # Two command line arguments were given.
    if sys.argv[1].isdecimal() and sys.argv[2].isdecimal():
        # Two integers were given as the bounds for a random number number:
        print(random.randint(int(sys.argv[1]), int(sys.argv[2])))
    else:
        # Two items were given to randomly select from:
        print(random.choice([sys.argv[1], sys.argv[2]]))
elif len(sys.argv) > 3:
    # Multiple items were given to randomly select from:
    print(random.choice(sys.argv[1:]))



