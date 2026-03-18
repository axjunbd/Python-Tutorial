import tkinter as tk
from tkinter import messagebox


def get_numbers():
    try:
        num1 = int(first_number_entry.get())
        num2 = int(second_number_entry.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")
        return None


def calculate(operation):
    numbers = get_numbers()
    if numbers is None:
        return

    num1, num2 = numbers

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        else:
            result = ""

        result_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")
        result_var.set("")


root = tk.Tk()
root.title("Arithmetic Operations")
root.geometry("420x260")


tk.Label(root, text="First Integer:").pack(pady=(12, 4))
first_number_entry = tk.Entry(root, width=24)
first_number_entry.pack()

tk.Label(root, text="Second Integer:").pack(pady=(10, 4))
second_number_entry = tk.Entry(root, width=24)
second_number_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=14)

tk.Button(button_frame, text="Add", width=8, command=lambda: calculate("add")).grid(
    row=0, column=0, padx=4
)
tk.Button(
    button_frame,
    text="Subtract",
    width=8,
    command=lambda: calculate("subtract"),
).grid(row=0, column=1, padx=4)
tk.Button(
    button_frame,
    text="Multiply",
    width=8,
    command=lambda: calculate("multiply"),
).grid(row=0, column=2, padx=4)
tk.Button(button_frame, text="Divide", width=8, command=lambda: calculate("divide")).grid(
    row=0, column=3, padx=4
)

tk.Label(root, text="Result:").pack()
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, width=28, state="readonly")
result_entry.pack(pady=5)

root.mainloop()
