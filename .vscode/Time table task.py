def get_input_number():
    user_input = input("Enter a number to generate its multiplication table: ").strip()
    if not user_input:
        print("Invalid input: please enter a number.")
        return None

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input: please enter a valid numeric value.")
        return None

    return number


def print_multiplication_table(value):
    for i in range(1, 11):
        product = i * value
        print(f"{i} X {value:g} = {product:g}")


if __name__ == "__main__":
    number = get_input_number()
    if number is None:
        exit(1)

    print_multiplication_table(number)