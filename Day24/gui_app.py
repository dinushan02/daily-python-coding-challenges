import tkinter as tk
from tkinter import messagebox


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


def calculate():
    user_input = entry.get()

    try:
        number = int(user_input)
        result = sum_of_digits(number)
        result_label.config(text=f"Sum of digits: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid whole number!")


root = tk.Tk()
root.title("Sum of Digits Calculator")
root.geometry("350x200")
root.resizable(False, False)

title_label = tk.Label(root, text="Sum of Digits", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()