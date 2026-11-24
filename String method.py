a = "Sojib"
b = a.casefold()
pass

def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def calculate(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: Cannot divide by zero"
            return a / b
        case "%":
            if b == 0:
                return "Error: Cannot divide by zero"
            return a % b
        case "**":
            return a ** b
        case _:
            return "Error: Invalid operator"


def main():
    print("=== Simple Calculator ===")
    print("Operators: +  -  *  /  %  **")

    while True:
        num1 = get_number("\nEnter first number: ")
        op = input("Enter operator (+, -, *, /, %, **): ").strip()
        num2 = get_number("Enter second number: ")

        result = calculate(num1, num2, op)
        print(f"Result: {result}")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()