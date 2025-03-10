def check_decimal():
    try:
        num_str = input("Give me a number: ")
        num = float(num_str)

        if num == int(num):
            print("This number is an integer.")
        else:
            print("This number is a decimal.")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    check_decimal()