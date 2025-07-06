import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length=int(length_entry.get())
        if not 8 <= length<=32:
            raise ValueError
        
        char_sets=[]
        if lowercase_var.get():
            char_sets.append(string.ascii_lowercase)
        if uppercase_var.get():
            char_sets.append(string.ascii_uppercase)
        if numbers_var.get():
            char_sets.append(string.digits)
        if special_var.get():
            char_sets.append(string.punctuation)
        if not char_sets:
            messagebox.showwarning("Warning", "Select at least one character type.")
            return
        base=[]
        for char_set in char_sets:
            base.append(secrets.choice(char_set))
        
        all_chars=''.join(char_sets)
        remaining_length=length-len(base)
        for i in range(remaining_length):
            radom_char=secrets.choice(all_chars)
            base.append(radom_char)
        secrets.SystemRandom().shuffle(base)
        password=''.join(base)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error","Enter a valid Number between 8-32")

root=tk.Tk()
root.title("Password Generator")
root.resizable(True,True)

tk.Label(root,text="password length (8-32):",font=("Arial",12),justify="center").pack(pady=5)
length_entry=tk.Entry(root,font=("Arial",12),justify="center")
length_entry.pack(pady=5)
lowercase_var=tk.BooleanVar(value=True)
uppercase_var=tk.BooleanVar(value=True)
numbers_var=tk.BooleanVar(value=True)
special_var=tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include lowercase Letters", variable=lowercase_var, font=("Arial", 10),justify="center").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=("Arial", 10),justify="center").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include numbers ", variable=numbers_var, font=("Arial", 10),justify="center").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include special character", variable=special_var, font=("Arial", 10),justify="center").pack(anchor="w", padx=40)

tk.Button(root,text="Generate Password",command=generate_password,font=('Arial',12),bg="green",fg="white").pack(pady=10)
result_entry=tk.Entry(root,font=('Arial',12),width=30,justify="center")
result_entry.pack(pady=15,padx=15)
root.mainloop()