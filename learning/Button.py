import tkinter as tk

root = tk.Tk()
root.title("my app")

button_options = {
    "text": "Click me!",
    "font": ("Arial", 16),
    "fg": "red",
    "bg": "lightgray",
    # "width": 20,
    # "height": 3,
    "command": lambda: print("Hello, Tkinter!")
}
button = tk.Button(root, **button_options)
button.pack(side="left")


# click to destroy the window
quit_button = tk.Button(root,text="Quit", command=root.destroy)
quit_button.pack(side="left")
root.mainloop()
