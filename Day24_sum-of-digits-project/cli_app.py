def sum_of_digits(number):
    num = abs(number)

    if num == 0:
        return 0

    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


try:
    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"Sum of all digits: {result}")
except ValueError:
    print("Please enter only a whole number!")



