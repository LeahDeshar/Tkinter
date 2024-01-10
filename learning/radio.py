import tkinter as tk

def on_radio_clicked():
    selected_text.set("Selected Option: " + radio_var.get())

# Create the main window
root = tk.Tk()
root.title("Radiobutton Example")

# Variable to track the selected Radiobutton
radio_var = tk.StringVar()

# Create Radiobuttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=on_radio_clicked)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=on_radio_clicked)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=on_radio_clicked)

# Variable to display the selected option
selected_text = tk.StringVar()

# Label to display the selected option
label_selected = tk.Label(root, textvariable=selected_text)

# Pack widgets into the main window
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
