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
    print("\nWelcome to Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


def main():
    while True:
        try:
            menu()
            choice = int(input("Choose (1/2/3/4/5): "))

            if choice == 5:
                print("Bye 👍")
                break

            elif choice in [1, 2, 3, 4]:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))

                try:
                    if choice == 1:
                        result = add(num1, num2)
                    elif choice == 2:
                        result = sub(num1, num2)
                    elif choice == 3:
                        result = mul(num1, num2)
                    elif choice == 4:
                        result = div(num1, num2)

                    print(f"Result: {result:.2f}")

                except ZeroDivisionError as e:
                    print(e)

            else:
                print("Please choose (1/2/3/4/5)")

        except ValueError:
            print("Please only enter a number!")


if __name__ == "__main__":
    main()



