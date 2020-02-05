#!/usr/bin/env python3
import random, argparse

def promptForInt(s):
    while True:
        try:
            guess = int(input(s))
            return guess
        except ValueError:
            print("You must enter an integer!")

parser = argparse.ArgumentParser(description="Imitates the experience of rolling dice.")
parser.add_argument("-n", "--num", type=int, default=2, help="How many dice are being rolled")
parser.add_argument("-r", "--rolls", type=int, default=-1, help="How many times the dice are rolled")
parser.add_argument("-s", "--sides", type=int, default=6, help="How many sides each die will have")
parser.add_argument("-v", "--verbose", action="count", default=0, help="Produce more verbose output")
args = parser.parse_args()

if args.sides <= 0:
    print("The dice must have at least 1 side!")
else:
    rollsSoFar = 0
    choice = "y"
    displayEnd = " " if args.rolls == -1 else "\n"
    while(choice == "y" and (rollsSoFar < args.rolls or args.rolls == -1 )):
        for i in range(args.num):
            thisDie = random.randint(1, args.sides)
            if args.verbose == 0:
                if i == 0:
                    print(f"{thisDie}", end="")
                else:
                    print(f" {thisDie}", end="")
            elif args.verbose == 1:
                if i == 0:
                    print(f"{thisDie}", end="")
                else:
                    print(f", {thisDie}", end="")
            else:
                if i == 0:
                    print(f"[{thisDie}]", end="")
                else:
                    print(f" [{thisDie}]", end="")
        print(f"{displayEnd}", end="")
        rollsSoFar += 1
        choice = "y" if args.rolls != -1 else input(" ..Roll again? (y/n) ").strip().lower()
