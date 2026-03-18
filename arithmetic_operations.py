import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Arithmetic Operations")
    root.geometry("300x250")
    
    ttk.Label(root, text="Number 1:").pack(pady=5)
    num1_entry = ttk.Entry(root)
    num1_entry.pack(pady=5)
    
    ttk.Label(root, text="Number 2:").pack(pady=5)
    num2_entry = ttk.Entry(root)
    num2_entry.pack(pady=5)
    
    result_label = ttk.Label(root, text="Result: ")
    result_label.pack(pady=10)
    
    def calculate(op):
        try:
            n1 = float(num1_entry.get())
            n2 = float(num2_entry.get())
            if op == '+': res = n1 + n2
            elif op == '-': res = n1 - n2
            elif op == '*': res = n1 * n2
            elif op == '/': res = n1 / n2 if n2 != 0 else "Error (Div by 0)"
            result_label.config(text=f"Result: {res}")
        except ValueError:
            result_label.config(text="Result: Invalid Input")

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="+", width=4, command=lambda: calculate('+')).pack(side=tk.LEFT, padx=2)
    ttk.Button(btn_frame, text="-", width=4, command=lambda: calculate('-')).pack(side=tk.LEFT, padx=2)
    ttk.Button(btn_frame, text="*", width=4, command=lambda: calculate('*')).pack(side=tk.LEFT, padx=2)
    ttk.Button(btn_frame, text="/", width=4, command=lambda: calculate('/')).pack(side=tk.LEFT, padx=2)

    root.mainloop()

if __name__ == "__main__":
    main()
