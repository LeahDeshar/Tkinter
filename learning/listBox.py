import tkinter as tk

def on_listbox_select(event):
    selected_items = listbox.curselection()
    selected_text.set("Selected Item(s): " + ", ".join(listbox.get(idx) for idx in selected_items))

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a StringVar to track the selected items
selected_text = tk.StringVar()

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.insert(4, "Item 4")
listbox.bind("<<ListboxSelect>>", on_listbox_select)

# Label to display the selected items
label_selected = tk.Label(root, textvariable=selected_text)

# Pack widgets into the main window
listbox.pack(pady=10)
label_selected.pack()

# Start the Tkinter event loop
root.mainloop()
