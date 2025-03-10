def advanced_mult():
    outer_counter = 0

    while outer_counter <= 10:
        inner_counter = 0
        result_string = f"Table de {outer_counter}:"

        while inner_counter <= 10:
            result_string += f" {outer_counter * inner_counter}"
            inner_counter += 1

        print(result_string)
        outer_counter += 1

if __name__ == "__main__":
    advanced_mult()