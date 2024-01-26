import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the toggleable sidebar
sidebar_visible = False

def toggle_sidebar():
    global sidebar_visible
    if sidebar_visible:
        sidebar.pack_forget()
        sidebar_visible = False
    else:
        sidebar.pack(side=tk.LEFT)
        sidebar_visible = True

sidebar = tk.Frame(window, width=100, bg="gray")
toggle_button = tk.Button(window, text="Toggle Sidebar", command=toggle_sidebar)
toggle_button.pack()

# Create the number buttons
numbers_frame = tk.Frame(window)
numbers_frame.pack()

for i in range(1, 10):
    button = tk.Button(numbers_frame, text=str(i), width=5)
    button.grid(row=(i-1)//3, column=(i-1)%3)

# Run the main loop
window.mainloop()
