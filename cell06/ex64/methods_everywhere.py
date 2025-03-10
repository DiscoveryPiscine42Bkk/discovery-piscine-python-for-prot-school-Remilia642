#!/usr/bin/env python3

import sys

def shrink(text):
    """Displays the first eight characters of a string."""
    print(text[:8])

def enlarge(text):
    """Appends 'Z' characters to a string to make it eight characters long."""
    while len(text) < 8:
        text += 'Z'
    print(text)

def process_arguments():
    """Processes command-line arguments and calls shrink/enlarge accordingly."""
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) < 8:
                enlarge(arg)
            else:
                print(arg)

if __name__ == "__main__":
    process_arguments()