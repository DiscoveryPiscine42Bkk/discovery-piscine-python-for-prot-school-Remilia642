#!/usr/bin/env python3

import sys

def free_range():
    """Creates and displays a range array or 'none'."""
    if len(sys.argv) == 3:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            if start < end:
                result_array = list(range(start, end))
            else:
                result_array = list(range(end, start))

            print(result_array)
        except ValueError:
            print("none") # if the arguments are not integers.
    else:
        print("none")

if __name__ == "__main__":
    free_range()