import tkinter as tk

def on_spinbox_change():
    selected_value.set("Selected Value: " + spinbox_var.get())

# Create the main window
root = tk.Tk()
root.title("Spinbox Example")

# Create a StringVar to track the selected value
spinbox_var = tk.StringVar()

# Create a Spinbox
spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=spinbox_var, command=on_spinbox_change)

# Variable to display the selected value
selected_value = tk.StringVar()

# Label to display the selected value
label_selected = tk.Label(root, textvariable=selected_value)

# Pack widgets into the main window
spinbox.pack(pady=10)
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
