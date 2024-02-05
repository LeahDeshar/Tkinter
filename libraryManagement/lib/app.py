import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from Book import AddBookWindow
from Student import AddStudentWindow
import sqlite3

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")
        
        self.conn = sqlite3.connect('library.db')
        self.create_tables()
        
        
        Style('darkly')

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill=tk.BOTH)

        self.login_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.login_frame, text="Login")
        self.create_login_page(self.login_frame)

        self.register_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.register_frame, text="Register")
        self.create_register_page(self.register_frame)

        
        # Dashboard Page
        self.dashboard_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.dashboard_frame, text="Dashboard")
        self.notebook.tab(self.dashboard_frame, state="disabled")


        # Initialize login status
        self.logged_in = False
        notebook = ttk.Notebook(self.dashboard_frame)
        notebook.pack(pady=10, fill=tk.BOTH, expand=True)

        student_tab = ttk.Frame(notebook)
        
        notebook.add(student_tab, text="Students")
        self.create_student_tab(student_tab)

        # Create Book tab
        book_tab = ttk.Frame(notebook)
        notebook.add(book_tab, text="Books")
        self.create_book_tab(book_tab)
        
        self.student_count_label = tk.Label(root, text="Total Students: 0", font=('Helvetica', 12))
        self.student_count_label.pack(pady=10)

        self.book_count_label = tk.Label(root, text="Total Books: 0", font=('Helvetica', 12))
        self.book_count_label.pack(pady=10)

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    phone_number TEXT,
                    address TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_name TEXT,
                    author TEXT,
                    isbn TEXT
                )
            ''')      

    def create_student_tab(self, parent):
        self.student_tree = ttk.Treeview(parent, columns=('Name', 'Email','Phone Number','Address'))
        self.student_tree.heading('#0', text='ID')
        self.student_tree.column('#0', width=50)
        self.student_tree.heading('#1', text='Name')
        self.student_tree.column('#1', width=150)
        self.student_tree.heading('#2', text='Email')
        self.student_tree.column('#2', width=150)
        self.student_tree.heading('#3', text='Phone Number')
        self.student_tree.column('#3', width=150)
        self.student_tree.heading('#4', text='Address')
        self.student_tree.column('#4', width=150)
        self.student_tree.pack(padx=10, pady=10)

        add_student_button = ttk.Button(parent, text="Add Student", command=self.add_student)
        add_student_button.pack(pady=10)
        
        update_student_button = ttk.Button(parent, text="Update Student", command=self.update_student)
        update_student_button.pack(pady=5)

        delete_student_button = ttk.Button(parent, text="Delete Student", command=self.delete_student)
        delete_student_button.pack(pady=5)

    def create_book_tab(self, parent):
        self.book_tree = ttk.Treeview(parent, columns=('ID', 'Book Name', 'Author','ISBN'))
        self.book_tree.heading('#0', text='ID')
        self.book_tree.column('#0', width=50)
        self.book_tree.heading('#1', text='Book Name')
        self.book_tree.column('#1', width=150)
        self.book_tree.heading('#2', text='Author')
        self.book_tree.column('#2', width=150)
        self.book_tree.heading('#3', text='ISBN')
        self.book_tree.column('#3', width=150)
        self.book_tree.pack(padx=10, pady=10)

        add_book_button = ttk.Button(parent, text="Add Book", command=self.add_book)
        add_book_button.pack(pady=10)

        update_book_button = ttk.Button(parent, text="Update Book", command=self.update_book)
        update_book_button.pack(pady=5)

        delete_book_button = ttk.Button(parent, text="Delete Book", command=self.delete_book)
        delete_book_button.pack(pady=5)

    def add_student(self):
        add_student_window = AddStudentWindow(self.root, self.student_tree,self.update_counts)

    def update_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            return

        name = self.student_tree.item(selected_item, 'values')[0]
        email = self.student_tree.item(selected_item, 'values')[1]
        ph_number = self.student_tree.item(selected_item, 'values')[2]
        address = self.student_tree.item(selected_item, 'values')[3]

        update_student_window = AddStudentWindow(self.root, self.student_tree, self.update_counts,self.update_student_func)
        update_student_window.name_entry.insert(0, name)
        update_student_window.email_entry.insert(0, email)
        update_student_window.number_entry.insert(0, ph_number)
        update_student_window.address_entry.insert(0, address)

    def update_student_func(self, name, email, ph_number, address):
        selected_item = self.student_tree.selection()
        if not selected_item:
            return

        self.student_tree.item(selected_item, values=(name, email, ph_number, address))

    def delete_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            return

        self.student_tree.delete(selected_item)
        self.update_counts()

    def add_book(self):
        add_book_window = AddBookWindow(self.root, self.book_tree, self.add_book_func)

    def add_book_func(self, book_name, author, isbn):
        self.book_tree.insert('', 'end', values=(book_name, author, isbn))
        self.update_counts()

    def update_book(self):
        selected_item = self.book_tree.selection()
        if not selected_item:
            return

        book_name = self.book_tree.item(selected_item, 'values')[0]
        author = self.book_tree.item(selected_item, 'values')[1]
        isbn = self.book_tree.item(selected_item, 'values')[2]

        update_book_window = AddBookWindow(self.root, self.book_tree, self.update_book_func)
        update_book_window.book_entry.insert(0, book_name)
        update_book_window.author_entry.insert(0, author)
        update_book_window.isbn_entry.insert(0, isbn)

    def update_book_func(self, book_name, author, isbn):
        selected_item = self.book_tree.selection()
        if not selected_item:
            return

        self.book_tree.item(selected_item, values=(book_name, author, isbn))

    def delete_book(self):
        selected_item = self.book_tree.selection()
        if not selected_item:
            return

        self.book_tree.delete(selected_item)
        self.update_counts()
        
    def update_counts(self):
        student_count = self.student_tree.get_children()
        book_count = self.book_tree.get_children()

        self.student_count_label.config(text=f"Total Students: {len(student_count)}")
        self.book_count_label.config(text=f"Total Books: {len(book_count)}")

    def create_login_page(self, frame):
        # Create login page components
        label_username = ttk.Label(frame, text="Username:")
        label_password = ttk.Label(frame, text="Password:")
        entry_username = ttk.Entry(frame)
        entry_password = ttk.Entry(frame, show="*")
        btn_login = ttk.Button(frame, text="Login", command=lambda: self.login(entry_username.get(), entry_password.get()))

        label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        entry_username.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        entry_password.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        btn_login.grid(row=2, column=1, pady=10)
        

    def create_register_page(self, frame):
        label_username = ttk.Label(frame, text="Username:")
        label_password = ttk.Label(frame, text="Password:")
        entry_username = ttk.Entry(frame)
        entry_password = ttk.Entry(frame, show="*")
        btn_register = ttk.Button(frame, text="Register", command=self.register)

        label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        entry_username.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        entry_password.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        btn_register.grid(row=2, column=1, pady=10)

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True
            self.show_dashboard()

    def register(self):
        print("Register button clicked")

   
    
    def show_dashboard(self):
        if self.logged_in:
        # Enable the Dashboard Page
            self.notebook.tab(self.dashboard_frame, state="normal")
            self.notebook.tab(self.login_frame, state="hidden")
            self.notebook.tab(self.register_frame, state="hidden")
            
            # Switch to the Dashboard Page
            self.notebook.select(self.dashboard_frame)
        else:
            print("Login first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
