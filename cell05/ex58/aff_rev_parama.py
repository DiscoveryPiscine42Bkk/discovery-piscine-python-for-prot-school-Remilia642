#!/usr/bin/env python3

import sys

def aff_rev_params():
    """Displays parameters in reverse order or 'none' if fewer than two."""
    if len(sys.argv) < 2:
        print("none")
    else:
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])

if __name__ == "__main__":
    aff_rev_params()