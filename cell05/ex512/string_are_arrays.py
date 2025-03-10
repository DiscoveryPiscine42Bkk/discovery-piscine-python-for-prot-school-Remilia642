#!/usr/bin/env python3

import sys

def string_are_arrays():
    """Displays 'z' for each 'z' in the string or 'none'."""
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        z_count = input_string.count('z')
        if z_count > 0:
            print("z" * z_count)
        else:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    string_are_arrays()