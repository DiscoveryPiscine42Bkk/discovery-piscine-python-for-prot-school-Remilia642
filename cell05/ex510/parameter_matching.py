#!/usr/bin/env python3

import sys

def parameter_matching():
    """
    Prompts the user for a word and checks if it matches the parameter.
    Displays "Good job!" or "Nope, sorry..." or "none".
    """
    if len(sys.argv) == 2:
        parameter = sys.argv[1]
        user_input = input("Enter a word: ")
        if user_input == parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")

if __name__ == "__main__":
    parameter_matching()