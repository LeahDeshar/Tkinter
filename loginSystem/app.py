
from tkinter import *
from tkinter import messagebox

def login():
    if userName.get() == "" or password.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif userName.get() == "admin" and password.get() == "admin":
        messagebox.showinfo("Success", "Login Successful")
        open_main_page()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def open_main_page():
    main_screen.withdraw()
    main_page = Toplevel()
    main_page.title("Main Page")
    main_page.geometry("800x600")
    main_page.configure(bg="#d7dae2")
    
    

def reset():
    userName.set("")
    password.set("")

# create main screen
main_screen = Tk()
main_screen.geometry("600x400")
main_screen.configure(bg="#d7dae2")
main_screen.title("Login System")


# main title
label_title = Label(text="Login System", font=("Arial", 40, "bold"), fg="black", bg="#d7dae2")
label_title.pack(pady=20)

main_frame = Frame(main_screen, bg="#fff", width=500, height=200)
main_frame.pack(padx=20, pady=20)

Label(main_frame, text="Username", font=("Arial", 20, "bold"), bg="#fff").place(x=50, y=50)
Label(main_frame, text="Password", font=("Arial", 20, "bold"), bg="#fff").place(x=50, y=100)

userName = StringVar()
password = StringVar()

entry_name = Entry(main_frame, textvariable=userName, width=16, bd=1, font=("Arial", 20))
entry_name.place(x=200, y=50)
entry_password = Entry(main_frame, textvariable=password, width=16, bd=1, font=("Arial", 20), show="*")
entry_password.place(x=200, y=100)

Button(main_frame, text="Login", height="2", width=15, bg="green", fg="white", bd=0, command=login).place(x=100, y=150)
Button(main_frame, text="Reset", height="2", width=15, bg="green", fg="white", bd=0, command=reset).place(x=250, y=150)

main_screen.mainloop()


