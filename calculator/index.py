from tkinter import *
from PIL import ImageTk,Image

w=Tk()
w.geometry('900x500')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.title('Toggle Menu')


def default_home():
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Calculator',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)

   
def home():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
 


def toggle_win():
    global f1
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'H O M E','#0f9d9a','#12c4c0',home)
    bttn(0,117,'A C E R','#0f9d9a','#12c4c0',acer)
    bttn(0,154,'D E L L','#0f9d9a','#12c4c0',dell)
    bttn(0,191,'A S U S','#0f9d9a','#12c4c0',None)
    bttn(0,228,'A P P L E','#0f9d9a','#12c4c0',None)
    bttn(0,265,'A C E R','#0f9d9a','#12c4c0',None)

    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("menu.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

default_home()

img1 = ImageTk.PhotoImage(Image.open("menu.png"))




global b2
b2=Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)


w.mainloop()

# import tkinter as tk


# def toggle_sidebar():
#     if sidebar_visible.get():
#         canvas.move(sidebar_frame, -sidebar_width, 0)
#     else:
#         canvas.move(sidebar_frame, sidebar_width, 0)
#     sidebar_visible.set(not sidebar_visible.get())

# # Create the main window
# root = tk.Tk()
# root.title("Sidebar Example")

# # Set up sidebar variables
# sidebar_width = 150
# sidebar_visible = tk.BooleanVar()
# sidebar_visible.set(False)

# # Create a canvas for the main content
# canvas = tk.Canvas(root, width=500, height=300, bg="white")
# canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
# # Define sidebar_frame
# sidebar_frame = canvas.create_rectangle(0, 0, sidebar_width, 300, fill="grey")

# # Create a frame for the sidebar
# sidebar_frame = tk.Frame(root, width=sidebar_width, height=300, bg="lightgray")
# sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# # Create a button to toggle the sidebar
# toggle_button = tk.Button(canvas, text="Toggle Sidebar", command=toggle_sidebar)
# toggle_button.pack(pady=10)

# # Your main content goes here...

# # Start the main event loop
# root.mainloop()


# import tkinter as tk

# def toggle_sidebar():
#     if sidebar_visible.get():
#         canvas.move(sidebar_rect, -sidebar_width, 0)
#     else:
#         canvas.move(sidebar_rect, sidebar_width, 0)
#     sidebar_visible.set(not sidebar_visible.get())

# # Create the main window
# root = tk.Tk()
# root.title("Sidebar Example")

# # Set up sidebar variables
# sidebar_width = 150
# sidebar_visible = tk.BooleanVar()
# sidebar_visible.set(False)

# # Create a canvas for the main content
# canvas = tk.Canvas(root, width=500, height=300, bg="white")
# canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# # Define sidebar_rect
# sidebar_rect = canvas.create_rectangle(0, 0, sidebar_width, 300, fill="grey")



# # Create a frame for the sidebar
# sidebar_frame = tk.Frame(root, width=sidebar_width, height=300, bg="lightgray")
# sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
# label = tk.Label(sidebar_frame,text="Enter the number")
# label.pack()
# # Create a button to toggle the sidebar
# toggle_button = tk.Button(canvas, text="☰", command=toggle_sidebar)
# toggle_button.pack(pady=10)

# # Your main content goes here...

# # Start the main event loop
# root.mainloop()