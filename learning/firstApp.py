import tkinter as tk

root = tk.Tk()
root.title("my app")

root.geometry("500x300+100+100")

label_options = {
    "text": "Enter Your Name",
    "font": ("Arial", 16),
    "fg": "blue",  
    "bg": "red"
}


tk.Label(root,**label_options).pack(fill="y",expand=True)


def get_entry_text():
    entered_text = entry.get()
    label_output.config(text=f"You entered: {entered_text}")
    
    
    
label_output = tk.Label(root, text="")
entry = tk.Entry(
    relief=tk.SOLID,
    selectbackground='yellow',
    selectborderwidth=2,
    selectforeground='black',
    textvariable=get_entry_text,
    validate='key'  
)
entry.pack(pady=10)
label_output.pack()



    
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
