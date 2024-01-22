from tkinter import PhotoImage
import tkinter as tk

# dictionary of colors:
color = {"primary": "#212021", "orange": "#fff", "darkorange": "#3a3a3b"}

# setting root window:
root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg="gray17")
root.geometry("400x600+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="menu.png",height=50,width=50)
closeIcon = PhotoImage(file="menu.png",height=50,width=50)

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["primary"], fg="#5F5A33")
        homeLabel.config(bg=color["primary"])
        topFrame.config(bg=color["primary"])
        root.config(bg=color["primary"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["primary"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Button(topFrame,text="history", bg=color["orange"],  bd=0, command=switch)
# homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["darkorange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")



brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame,text="☰", bg=color["darkorange"],  bd=0,activebackground=color["darkorange"], command=switch)
navbarBtn.place(x=10, y=10)
standardLabel = tk.Button(topFrame,text="Standard", bg=color["primary"],  bd=0, command=switch)
# homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["darkorange"], fg="gray17", height=2, padx=20)
standardLabel.pack(side="left",padx=50,pady=20)
# Main label text:
# setting Navbar frame:
navRoot = tk.Frame(root, bg=color["darkorange"], height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["primary"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
tk.Label(navRoot, font="Bahnschrift 15", bg=color["primary"], fg="black",text="Calculator", padx=20).place(x=0, y=0)
options = ["Standard", "Scientific", "Graphing", "Programmer", "Date calculation"]
# Navbar Option Buttons:
for i in range(5):
    tk.Button(navRoot, text=options[i], font="Arial 9", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground=color["darkorange"], bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, text="☰", bg=color["primary"], activebackground=color["darkorange"], bd=0, command=switch)
closeBtn.place(x=10, y=10)

# window in mainloop:
root.mainloop()