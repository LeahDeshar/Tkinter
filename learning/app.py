import tkinter as tk


root = tk.Tk()
root.title("my app")
label_options = {
    "text": "Hello, Tkinter!",
    "font": ("Arial", 16),
    "fg": "blue",  # Foreground color
    "bg": "lightgray",  # Background color
    "width": 20,
    "height": 3,
}
tk.Label(root,**label_options).pack()
# tk.Label(root,text="Hello World!").pack()


root.mainloop()