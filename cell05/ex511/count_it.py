#!/usr/bin/env python3

import sys

def count_it():
    """Displays parameter count and each parameter with its length."""
    if len(sys.argv) == 1:
        print("Hi")
    else:
        print(f"parameters: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"{sys.argv[i]} {len(sys.argv[i])}")

if __name__ == "__main__":
    count_it()