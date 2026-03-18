import tkinter as tk
from tkinter import ttk, messagebox

def main():
    root = tk.Tk()
    root.title("Student Management")
    root.geometry("500x400")
    
    input_frame = ttk.Frame(root)
    input_frame.pack(pady=10)
    
    ttk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(input_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(input_frame, text="Roll No:").grid(row=1, column=0, padx=5, pady=5)
    roll_entry = ttk.Entry(input_frame)
    roll_entry.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(input_frame, text="Course:").grid(row=2, column=0, padx=5, pady=5)
    course_entry = ttk.Entry(input_frame)
    course_entry.grid(row=2, column=1, padx=5, pady=5)
    
    tree = ttk.Treeview(root, columns=("Name", "Roll", "Course"), show="headings", height=8)
    tree.heading("Name", text="Name")
    tree.heading("Roll", text="Roll No")
    tree.heading("Course", text="Course")
    tree.pack(padx=10, pady=10, fill='both', expand=True)
    
    def add_student():
        n = name_entry.get()
        r = roll_entry.get()
        c = course_entry.get()
        if n and r and c:
            tree.insert("", "end", values=(n, r, c))
            name_entry.delete(0, tk.END)
            roll_entry.delete(0, tk.END)
            course_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Incomplete", "Please fill all fields")
            
    def delete_student():
        selected = tree.selection()
        if selected:
            for item in selected:
                tree.delete(item)
                
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="Add Student", command=add_student).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Delete Selected", command=delete_student).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
