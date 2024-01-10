import tkinter as tk

def on_scale_change(value):
    selected_value.set("Selected Value: " + str(value))

# Create the main window
root = tk.Tk()
root.title("Scale Example")

# Create a StringVar to track the selected value
selected_value = tk.StringVar()

# Create a Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_change)

# Label to display the selected value
label_selected = tk.Label(root, textvariable=selected_value)

# Pack widgets into the main window
scale.pack(pady=10)
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
