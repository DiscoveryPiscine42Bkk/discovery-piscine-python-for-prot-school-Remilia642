#!/usr/bin/env python3

def play_with_filtered_unique_arrays():
    """
    Defines an array, creates a new array by adding 2 to elements greater than 5,
    removes duplicates from the new array, and displays both arrays.
    """

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [5]
    unique_new_array = [3]

    for number in original_array:
        if number > 5:
            new_array.append(number + 2)

    # Remove duplicates from new_array
    for number in new_array:
        if number not in unique_new_array:
            unique_new_array.append(number)

    print("Original Array:", original_array)
    print("New Array (values > 5, +2, unique):", unique_new_array)

if __name__ == "__main__":
    play_with_filtered_unique_arrays()