# import tkinter as tk
# from tkinter import ttk


# root = tk.Tk()
# root.geometry("500x500")
# root.title("Grid table")
# root.resizable(0, 0)


# root.rowconfigure(0,weight=1)
# root.rowconfigure(1,weight=1)


# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=1)

# # Create frames for each grid cell
# frame1 = tk.Frame(root, bg='red')
# frame1.grid(row=0, column=0)


# button1 = tk.Button(frame1,text="button1")
# button1.grid(row=0, column=0)

# frame2 = tk.Frame(root, bg='blue')
# frame2.grid(row=0, column=1,sticky="W")

# button2 = tk.Button(frame2,text="button2")
# button2.grid(row=0, column=0,sticky="W")

# frame3 = tk.Frame(root, bg='green')
# frame3.grid(row=1, column=0)

# frame4 = tk.Frame(root, bg='yellow')
# frame4.grid(row=1, column=1)

# # label1 = ttk.Label(root,text="Label 1")
# # label1.grid(row=0,column = 0)

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.geometry("500x500")
# root.title("Grid table")
# root.resizable(0, 0)

# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)

# # Create frames for each grid cell
# frame1 = tk.Frame(root, bg='red')
# frame1.grid(row=0, column=0, sticky='nsew')

# button1 = tk.Button(frame1, text="button1")
# button1.pack(padx=20, pady=20)

# frame2 = tk.Frame(root, bg='blue')
# frame2.grid(row=0, column=1, sticky='nsew')

# button2 = tk.Button(frame2, text="button2")
# button2.pack(padx=20, pady=20)

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Calculator Grid Layout")
# root.geometry("200x300")

# buttons = [
#     '7', '8', '9', 
#     '4', '5', '6', 
#     '1', '2', '3',
#     '+/-', '0', '.'
# ]

# for i in range(4): 
#     for j in range(3):  
#         button_text = buttons[i*3 + j]
#         button = tk.Button(root, text=button_text, width=5, height=2)
#         button.grid(row=i, column=j)

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Calculator")
root.geometry("200x300")

buttons = [
    '7', '8', '9', 
    '4', '5', '6', 
    '1', '2', '3',
    '+/-', '0', '.'
]

for i in range(4):
    root.rowconfigure(i, weight=1)
    if i < 3:  
        root.columnconfigure(i, weight=1)

for i in range(4):  
    for j in range(3): 
        button_text = buttons[i*3 + j]
        button = tk.Button(root, text=button_text, width=5, height=2)
        button.grid(row=i, column=j, sticky='nsew')

root.mainloop()