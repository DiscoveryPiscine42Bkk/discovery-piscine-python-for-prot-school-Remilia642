def multiplication_table():
    try:
        num = int(input("Enter a number\n"))

        for i in range(10):
            print(f"{i} x {num} = {i * num}")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    multiplication_table()