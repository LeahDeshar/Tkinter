import tkinter as tk

def on_checkbox_clicked():
    selected_text.set("Checkbutton State: " + str(checkbox_var.get()))

# Create the main window
root = tk.Tk()
root.title("Checkbutton Example")

# Variable to track the state of the Checkbutton
checkbox_var = tk.IntVar()

# Create a Checkbutton
checkbox = tk.Checkbutton(root, text="Enable Feature", variable=checkbox_var, command=on_checkbox_clicked)

# Variable to display the selected state
selected_text = tk.StringVar()

# Label to display the selected state
label_selected = tk.Label(root, textvariable=selected_text)

# Pack widgets into the main window
checkbox.pack(pady=10)
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
