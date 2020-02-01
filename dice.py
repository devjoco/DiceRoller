#!/usr/bin/env python3
import random

def promptForInt(s):
    while True:
        try:
            guess = int(input(s))
            return guess
        except ValueError:
            print("You must enter an integer!")

# Ask how many dice are being rolled
num = promptForInt("How many dice are you rolling? (0 to stop) ")

while(num != 0):
    # Randomly calculate dice
    for i in range(num):
        thisDie = random.randint(1,6)
        # Display dice
        print(f"[{thisDie}] ",end='')
    print()

    num = promptForInt("How many dice are you rolling? (0 to stop) ")
