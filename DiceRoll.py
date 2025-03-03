#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
    # Create an empty list with possible roll values (2-12)
    rolls = [0] * 11  # Only 11 

  
    for r in range(100):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        rolls[total - 2] += 1 

    # Print the results
    dice = 2
    for count in rolls:
        print(dice, ":", count)
        dice += 1  

if __name__ == '__main__':
    main()