import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class AddBookWindow:
    def __init__(self, parent, book_tree,update_book_func=None):
        self.window = tk.Toplevel(parent)
        self.window.title("Add Book")
        self.window.geometry("400x500")

        self.book_tree = book_tree  
        self.update_book_func = update_book_func
         
        tk.Label(self.window, text="Book Name:").pack(pady=10)
        self.book_entry = tk.Entry(self.window)
        self.book_entry.pack(pady=5)
        
        tk.Label(self.window, text="Author Of Book:").pack(pady=10)
        self.author_entry = tk.Entry(self.window)
        self.author_entry.pack(pady=5)
        
        tk.Label(self.window, text="ISBN").pack(pady=10)
        self.isbn_entry = tk.Entry(self.window)
        self.isbn_entry.pack(pady=5)
        
        submit_button = ttk.Button(self.window, text="Submit", command=self.submit_form)
        submit_button.pack(pady=10)
        
        
    def submit_form(self):
        book_name = self.book_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        
        if self.update_book_func:
            self.update_book_func(book_name, author, isbn)
        else:
            self.student_tree.insert('', 'end', values=(book_name, author, isbn))
            
        # self.book_tree.insert('', 'end', values=(book_name, author,isbn))

        self.window.destroy()