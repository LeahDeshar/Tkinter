import tkinter as tk

root = tk.Tk()
root.title("my app")


label_options = {
    "text": "Enter Your Name",
    "font": ("Arial", 16),
    "fg": "blue",  
}


tk.Label(root,**label_options).pack()

label_output = tk.Label(root, text="")
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
label_output.pack()


def get_entry_text():
    entered_text = entry.get()
    label_output.config(text=f"You entered: {entered_text}")
    
    
button_options = {
    "text": "Click me!",
    "font": ("Arial", 16),
    "fg": "red",
    "bg": "lightgray",
    "command":get_entry_text
}
button = tk.Button(root, **button_options)
button.pack(side="left")


quit_button = tk.Button(root,text="Quit", command=root.destroy)
quit_button.pack(side="left")
root.mainloop()
