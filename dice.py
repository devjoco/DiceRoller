#!/usr/bin/env python3
import random
import argparse

def promptForInt(s):
    while True:
        try:
            guess = int(input(s))
            return guess
        except ValueError:
            print("You must enter an integer!")

parser = argparse.ArgumentParser(description="Imitates the experience of rolling dice.")
parser.add_argument("dice", nargs="?", help="how many dice are being rolled")
parser.add_argument("-r", "--rolls", help="how many times the dice are rolled")
parser.add_argument("-s", "--sides", help="how many sides each die will have",
                    type=int, default=6)
args = parser.parse_args()


if args.sides == 0:
    print("The dice must have at least 1 side!")
else:
    # Ask how many dice are being rolled
    num = promptForInt("How many dice are you rolling? (0 to stop) ")

    while(num != 0):
        # Randomly calculate dice
        for i in range(num):
            thisDie = random.randint(1,args.sides)
            # Display dice
            print(f"[{thisDie}] ",end='')
        print()

        num = promptForInt("How many dice are you rolling? (0 to stop) ")
