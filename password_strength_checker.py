import tkinter as tk
from tkinter import ttk
import re

def main():
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("350x250")
    
    ttk.Label(root, text="Enter Password:").pack(pady=(30, 5))
    pwd_entry = ttk.Entry(root, show="*", width=30)
    pwd_entry.pack(pady=5)
    
    result_lbl = ttk.Label(root, text="Strength: N/A", font=('Helvetica', 12, 'bold'))
    result_lbl.pack(pady=20)
    
    def check_strength(*args):
        p = pwd_entry.get()
        if not p:
            result_lbl.config(text="Strength: N/A", foreground="black")
            return
        
        score = 0
        if len(p) >= 8: score += 1
        if re.search(r'[A-Z]', p): score += 1
        if re.search(r'[a-z]', p): score += 1
        if re.search(r'[0-9]', p): score += 1
        if re.search(r'[@$!%*?&#]', p): score += 1
        
        if score < 3:
            result_lbl.config(text="Strength: WEAK", foreground="red")
        elif score == 3 or score == 4:
            result_lbl.config(text="Strength: MEDIUM", foreground="orange")
        else:
            result_lbl.config(text="Strength: STRONG", foreground="green")
            
    pwd_entry.bind('<KeyRelease>', check_strength)

    root.mainloop()

if __name__ == "__main__":
    main()
