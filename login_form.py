import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Login Form")
    root.geometry("300x250")
    
    ttk.Label(root, text="Username:").pack(pady=(30, 5))
    username_entry = ttk.Entry(root)
    username_entry.pack(pady=5)
    
    ttk.Label(root, text="Password:").pack(pady=5)
    password_entry = ttk.Entry(root, show="*")
    password_entry.pack(pady=5)
    
    status_label = ttk.Label(root, text="")
    status_label.pack(pady=10)
    
    def attempt_login():
        user = username_entry.get()
        pwd = password_entry.get()
        if user == "admin" and pwd == "password":
            status_label.config(text="Login Successful!", foreground="green")
        else:
            status_label.config(text="Invalid credentials", foreground="red")
            
    ttk.Button(root, text="Login", command=attempt_login).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
