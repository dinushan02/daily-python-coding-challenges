history_file = "history.txt"


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2


def menu():
    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")


def save_history(expression):
    with open(history_file, "a") as file:
        file.write(expression + "\n")


def view_history():
    print("\n===== Calculator History =====")

    try:
        with open(history_file, "r") as file:
            history = file.readlines()

            if len(history) == 0:
                print("No history available.")

            else:
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item.strip()}")

    except FileNotFoundError:
        print("No history file found.")


def clear_history():
    with open(history_file, "w") as file:
        file.write("")

    print("History cleared successfully.")


def main():
    while True:
        try:
            menu()
            choice = int(input("Choose (1-7): "))

            if choice == 7:
                print("Bye 👍")
                break

            elif choice in [1, 2, 3, 4]:

                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))

                try:
                    if choice == 1:
                        result = add(num1, num2)
                        expression = f"{num1} + {num2} = {result}"

                    elif choice == 2:
                        result = sub(num1, num2)
                        expression = f"{num1} - {num2} = {result}"

                    elif choice == 3:
                        result = mul(num1, num2)
                        expression = f"{num1} * {num2} = {result}"

                    elif choice == 4:
                        result = div(num1, num2)
                        expression = f"{num1} / {num2} = {result}"

                    print(f"Result: {result:.2f}")

                    save_history(expression)

                except ZeroDivisionError as e:
                    print(e)

            elif choice == 5:
                view_history()

            elif choice == 6:
                clear_history()

            else:
                print("Please choose between 1 and 7")

        except ValueError:
            print("Please only enter a number!")


if __name__ == "__main__":
    main()