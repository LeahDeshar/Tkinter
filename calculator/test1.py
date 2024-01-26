import tkinter as tk

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Tkinter Example")

# Create a Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create a Canvas widget
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Attach the scrollbar to the canvas
scrollbar.config(command=canvas.yview)

# Bind the canvas to a function that updates the scroll region when the canvas is resized
canvas.bind("<Configure>", on_canvas_configure)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# Add some content to the frame
for i in range(100):
    tk.Label(frame, text="This is line number " + str(i)).pack()

root.mainloop()