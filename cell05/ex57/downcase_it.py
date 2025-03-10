#!/usr/bin/env python3

import sys

def downcase_it():
    """Displays the lowercase version of the given string or 'none'."""
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        print(input_string.lower())
    else:
        print("none")

if __name__ == "__main__":
    downcase_it()