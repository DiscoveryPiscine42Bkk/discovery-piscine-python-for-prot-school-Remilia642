def add_one(num):

    num += 1
    return num


my_number = 10

print("Before calling add_one:", my_number)

add_one(my_number)

print("After calling add_one:", my_number)

print("Observation: The value of my_number did not change because the change inside the function add_one is limited to the local scope of the function.")