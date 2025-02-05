from tkinter import PhotoImage
import tkinter as tk

color = {"primary": "#212021", "orange": "#fff", "darkorange": "#212021","red": "#3b3b3b"}

root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg=color["primary"])
root.geometry("400x600+850+50")

btnState = False

navIcon = PhotoImage(file="menu.png",height=50,width=50)
closeIcon = PhotoImage(file="menu.png",height=50,width=50)

def switch():
    global btnState
    if btnState is True:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # brandLabel.config(bg=color["primary"], fg="green")
        root.config(bg=color["primary"])
        btnState = False
    else:
        # brandLabel.config(bg=color["primary"], fg="#5F5A33")
        homeLabel.config(bg=color["primary"])
        topFrame.config(bg=color["primary"])
        root.config(bg=color["darkorange"])

        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        btnState = True

topFrame = tk.Frame(root, bg=color["primary"])
topFrame.pack(side="top", fill=tk.X)

homeLabel = tk.Button(topFrame,text="history", bg=color["orange"],  bd=0, command=switch)

homeLabel.pack(side="right")



# brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", bg="gray17", fg="green")
# brandLabel.place(x=100, y=250)

# brandLabel1 = tk.Label(root, text="Pythonista", font="System 30", bg="gray17", fg="green")
# brandLabel1.place(x=130, y=290)
button_frame = tk.Frame(root)
button_frame.grid(row=1,sticky='nsew')

buttons = [
    '7', '8', '9', 
    '4', '5', '6', 
    '1', '2', '3',
    '+/-', '0', '.'
]

for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    if i < 3:  
        button_frame.columnconfigure(i, weight=1)

for i in range(4):  
    for j in range(3): 
        button_text = buttons[i*3 + j]
        button = tk.Button(button_frame, text=button_text, width=5, height=2)
        button.grid(row=i, column=j, sticky='nsew')
        
        
        
navbarBtn = tk.Button(topFrame,text="☰", bg=color["darkorange"],  bd=0,activebackground=color["darkorange"], command=switch)
navbarBtn.place(x=10, y=10)
standardLabel = tk.Button(topFrame,text="Standard", bg=color["primary"],  bd=0, command=switch)
standardLabel.pack(side="left",padx=50,pady=20)

navRoot = tk.Frame(root, bg=color["red"], height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["red"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)
y = 80

options = {
    "Calculator": ["Standard", "Scientific", "Graphing", "Programmer", "Date calculation"],
    "Converter" : ["Currency","Volume","Length","Weight and mass","Temperature","Enery","Area","Speed","Time","Power","Data","Pressure","Angle"]
    }
for key in options:
    tk.Label(navRoot, text=key, font="Arial 12 bold", bg=color["red"], fg=color["orange"]).place(x=25, y=y)
    y += 20  

    for option in options[key]:
        tk.Button(navRoot, text=option, font="Arial 9", bg=color["red"], fg=color["orange"],
                  activebackground="gray17", activeforeground=color["darkorange"], bd=0).place(x=25, y=y)
        y += 40  
closeBtn = tk.Button(navRoot, text="☰", bg=color["red"], activebackground=color["darkorange"], bd=0, command=switch)
closeBtn.place(x=10, y=10)

root.mainloop()
