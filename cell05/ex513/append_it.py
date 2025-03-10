#!/usr/bin/env python3

import sys

def append_it():
    """Appends 'ism' to parameters or displays 'none'."""
    if len(sys.argv) == 1:
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            param = sys.argv[i]
            if not param.endswith("ism"):
                print(param + "ism")

if __name__ == "__main__":
    append_it()