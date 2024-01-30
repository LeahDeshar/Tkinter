import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

from Book import AddBookWindow
from Student import AddStudentWindow
        
class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        Style('darkly') 
        notebook = ttk.Notebook(root)
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

    # def add_book(self):
    #     add_book_window = AddBookWindow(self.root, self.book_tree)
        
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

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
