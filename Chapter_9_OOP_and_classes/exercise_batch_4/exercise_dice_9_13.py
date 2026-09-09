# Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called 
# roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and 
# roll it 10 times.

from random import randint

class Dice:
    """A class representing a standard six-sided die."""
    
    def __init__(self):
        """Initialize the die with 6 sides."""
        self.sides = 6
        
    def roll_die(self):
        """Roll the die and return a random number between 1 and the number of sides."""
        print("\nRolling the dice")
        dice_value = randint(1, self.sides)
        print(f"\t{dice_value}")
        
        
        
dice = Dice()

dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
