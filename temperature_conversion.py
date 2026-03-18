import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("300x250")
    
    ttk.Label(root, text="Temperature:").pack(pady=(20, 5))
    temp_entry = ttk.Entry(root)
    temp_entry.pack(pady=5)
    
    var = tk.StringVar(value="C2F")
    ttk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C2F").pack(pady=5)
    ttk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F2C").pack(pady=5)
    
    res_label = ttk.Label(root, text="Result: ")
    res_label.pack(pady=15)
    
    def convert():
        try:
            t = float(temp_entry.get())
            if var.get() == "C2F":
                res = (t * 9/5) + 32
                res_label.config(text=f"Result: {res:.2f} °F")
            else:
                res = (t - 32) * 5/9
                res_label.config(text=f"Result: {res:.2f} °C")
        except ValueError:
            res_label.config(text="Result: Invalid Input")
            
    ttk.Button(root, text="Convert", command=convert).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
