import tkinter as tk
from tkinter import ttk

def on_combobox_selected(event):
    selected_text.set("Selected Option: " + combobox_var.get())

# Create the main window
root = tk.Tk()
root.title("Combobox Example")

# Create a StringVar to track the selected item
combobox_var = tk.StringVar()

# Create a Combobox
combobox = ttk.Combobox(root, textvariable=combobox_var, values=["Option 1", "Option 2", "Option 3"])
combobox.bind("<<ComboboxSelected>>", on_combobox_selected)

# Variable to display the selected option
selected_text = tk.StringVar()

# Label to display the selected option
label_selected = tk.Label(root, textvariable=selected_text)

# Pack widgets into the main window
combobox.pack(pady=10)
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
