# Dice Roller
The dice rolling simulator will imitate the experience of rolling dice. It will generate a random number and the user can play again and again to get a number from the dice until the user decides to quit the program.

## SYNOPSIS
    dice.py [-h] [-n NUM] [-r ROLLS] [-s SIDES]

## DESCRIPTION
    Simulates a dice roll.

    -h, --help
        Display help and exit

    -n, --num
        Specify how many dice to roll
        If not specified, defaults to two dice

    -r, --rolls
        Specify how many rolls, and perform them all immediately
        If not specified, waits for user to continue rolling

    -s, --sides
        Specify how many sides each die has
        If not specified, defaults to 6-sided dice

    -v, --verbose
        Separate each die outcome with a comma 
        If given twice, surround each with brackets for a slightly more graphical depiction
        If not specified, separate each die outcome with a space

