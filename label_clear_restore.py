import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Clear/Restore Label")
    root.geometry("350x200")
    
    original_text = "Hello! This label can be cleared and restored."
    volatile_label = ttk.Label(root, text=original_text, font=('Helvetica', 10))
    volatile_label.pack(pady=40)
    
    def clear_lbl():
        volatile_label.config(text="")
        
    def restore_lbl():
        volatile_label.config(text=original_text)
        
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="Clear Label", command=clear_lbl).pack(side=tk.LEFT, padx=10)
    ttk.Button(btn_frame, text="Restore Label", command=restore_lbl).pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
