import random

for i in range(3): # creating a range object three times.
    print(random.randint(10, 22)) # random module, then random method.

letters = ['A', 'B', 'C', 'D', 'E']
picked = random.choice(letters) # picking a letter from the letters list.
print(picked)
# blank
# blank
class Dice: # always blank two lines above and below the class loop.
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second) # ending the class loop with tuple using ().
# blank
# blank
dice = Dice()
print(dice.roll())
