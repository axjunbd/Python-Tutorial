import tkinter as tk
from tkinter import ttk, messagebox

def main():
    root = tk.Tk()
    root.title("Bill Generation")
    root.geometry("400x500")
    
    form_frame = ttk.Frame(root)
    form_frame.pack(pady=10)
    
    ttk.Label(form_frame, text="Item Name:").grid(row=0, column=0, padx=5, pady=5)
    item_entry = ttk.Entry(form_frame)
    item_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(form_frame, text="Price:").grid(row=1, column=0, padx=5, pady=5)
    price_entry = ttk.Entry(form_frame)
    price_entry.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(form_frame, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
    qty_entry = ttk.Entry(form_frame)
    qty_entry.grid(row=2, column=1, padx=5, pady=5)
    
    bill_text = tk.Text(root, height=15, width=40)
    bill_text.pack(pady=10)
    
    total_amount = [0]
    
    def add_item():
        try:
            name = item_entry.get()
            price = float(price_entry.get())
            qty = int(qty_entry.get())
            if not name:
                raise ValueError
            cost = price * qty
            total_amount[0] += cost
            bill_text.insert(tk.END, f"{name} - {qty} x ${price:.2f} = ${cost:.2f}\n")
            item_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            qty_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for name, price, or quantity")
            
    def generate_bill():
        bill_text.insert(tk.END, "-"*30 + "\n")
        bill_text.insert(tk.END, f"Total: ${total_amount[0]:.2f}\n")
        bill_text.insert(tk.END, "="*30 + "\n")
        
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=5)
    ttk.Button(btn_frame, text="Add Item", command=add_item).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Generate Bill", command=generate_bill).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
