import tkinter as tk
from tkinter import ttk
# Create the main window
root = tk.Tk()
root.title("Separator Example")

# Create widgets
label1 = tk.Label(root, text="Section 1")
separator1 = ttk.Separator(root, orient="horizontal")
label2 = tk.Label(root, text="Section 2")
separator2 = ttk.Separator(root, orient="horizontal")
label3 = tk.Label(root, text="Section 3")

# Pack widgets into the main window
label1.pack(pady=5)
separator1.pack(fill="x", pady=5)  # Horizontal separator
label2.pack(pady=5)
separator2.pack(fill="x", pady=5)  # Horizontal separator
label3.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
