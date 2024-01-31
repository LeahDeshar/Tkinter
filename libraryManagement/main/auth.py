import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class LoginSignupWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Login or Sign Up")
        self.root.geometry("400x300")

        Style('darkly')

        self.on_login_success = on_login_success

        self.create_login_signup_form()

    def create_login_signup_form(self):
        tk.Label(self.root, text="Username:").pack(pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        login_button = ttk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=10)

        signup_button = ttk.Button(self.root, text="Sign Up", command=self.signup)
        signup_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        print(f"User logged in - Username: {username}, Password: {password}")

        if username and password:
            # Successful login
            self.on_login_success()
            self.root.destroy()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            print(f"User signed up - Username: {username}, Password: {password}")