import math

def round_up():
    try:
        num_str = input("Give me a number: ")
        num = float(num_str)

        rounded_up = math.ceil(num)
        print(rounded_up)

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    round_up()