#!/usr/bin/env python3

def play_with_arrays():
    """
    Defines an array, creates a new array by adding 2 to each element,
    and displays both arrays.
    """

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []

    for number in original_array:
        new_array.append(number + 2)

    print("Original Array:", original_array)
    print("New Array:", new_array)

if __name__ == "__main__":
    play_with_arrays()