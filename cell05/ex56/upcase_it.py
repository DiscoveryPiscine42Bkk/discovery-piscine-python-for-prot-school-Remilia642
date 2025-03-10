#!/usr/bin/env python3

import sys

def upcase_it():
    """Displays the uppercase version of the given string or 'none'."""
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        print(input_string.upper())
    else:
        print("none")

if __name__ == "__main__":
    upcase_it()