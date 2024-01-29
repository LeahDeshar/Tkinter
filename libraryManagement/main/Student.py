import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class AddStudentWindow:
    def __init__(self, parent, student_tree, update_student_func=None):
        self.window = tk.Toplevel(parent)
        self.window.title("Add Student")
        self.window.geometry("400x500")

        self.student_tree = student_tree  
        self.update_student_func = update_student_func  

        tk.Label(self.window, text="Name:").pack(pady=10)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Email:").pack(pady=10)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack(pady=5)

        tk.Label(self.window, text="Phone Number:").pack(pady=10)
        self.number_entry = tk.Entry(self.window)
        self.number_entry.pack(pady=5)

        tk.Label(self.window, text="Address:").pack(pady=10)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.pack(pady=5)

        submit_button = ttk.Button(self.window, text="Submit", command=self.submit_form)
        submit_button.pack(pady=10)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        ph_number = self.number_entry.get()
        address = self.address_entry.get()

        if self.update_student_func:
            self.update_student_func(name, email, ph_number, address)
        else:
            self.student_tree.insert('', 'end', values=(name, email, ph_number, address))

        self.window.destroy()