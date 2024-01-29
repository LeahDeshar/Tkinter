#initial root config
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
root = tk.Tk()

root.title("Library Management System")
root.geometry("700x700")


# root.rowconfigure(1,weight=1)
# root.rowconfigure(2,weight=1)
# root.rowconfigure(3,weight=1)


# login


# dashboard
# title
title_label = tk.Label(root,text="Library Management System",font=("Arial",30,"bold"),justify="center")
title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

add_student_btn = ttk.Button(root,text="Add Button")
add_student_btn.grid(row=1,column=0)



book_tree = ttk.Treeview(master=root,columns=('S.N','Name','Author','ISBN'))
book_tree.heading('S.N',text='S.N')
book_tree.heading('Name',text='Name')
book_tree.heading('Author',text='Author')
book_tree.heading('ISBN',text='ISBN')



book_scrollbar = ttk.Scrollbar(root,command=book_tree.
                                 yview)
book_tree.configure(yscrollcommand=book_scrollbar.set)


book_tree.grid(row=2,column=0)
book_scrollbar.grid(row=2,column=1,sticky="NS")

# student list in table

# button for add book and student

# click on button and open new window to add the new book and student

# new window  
# book name,author,isbn,submit btn
# student name,email,ph number,address,submit btn
# form validation,error messages



# total number of books and total number of student


# student add 
# student CRUD
# book CRUD
# Table for book









root.mainloop()