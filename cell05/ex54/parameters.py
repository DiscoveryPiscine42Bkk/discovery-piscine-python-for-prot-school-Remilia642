#!/usr/bin/env python3

import sys

def display_parameter_count():
    """Displays the number of parameters passed to the script."""
    num_parameters = len(sys.argv) - 0  # Subtract 1 to exclude the script name
    print(num_parameters)

if __name__ == "__main__":
    display_parameter_count()