import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen.mp3 import MP3
import threading
import pygame
import time 
import os 


pygame.mixer.init()

current_position = 0
paused = False 
selected_folder_path = ""

def previous_song():
    pass
def play_music():
    pass
def next_music():
    pass
def pause_music():
    pass
def select_music_folder():
    pass
# create the main window
window = tk.Tk()
window.title("Music Player App")
window.geometry("600x500")


l_music_player = tk.Label(window,text="Music Player",font=("TKDefaultFont",30,"bold"))
l_music_player.pack(pady=10)


btn_select_folder = ctk.CTkButton(window,text="Select Music Folder",command=select_music_folder,font=("TKDefaultFont",18))
btn_select_folder.pack(pady=20)

lbox = tk.Listbox(window,width=50,font=("TkDefaultFont",16))
lbox.pack(pady=10)



btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)


btn_previous = ctk.CTkButton(btn_frame,text="<",command=previous_song,width=50,font=("TkDefaultFont",18))
btn_previous.pack(side=tk.LEFT,padx=5)

btn_play = ctk.CTkButton(btn_frame,text="Play",command=play_music,width=50,font=("TkDefaultFont",18))
btn_play.pack(side=tk.LEFT,padx=5)

btn_pause = ctk.CTkButton(btn_frame,text="Pause",command=pause_music,width=50,font=("TkDefaultFont",18))
btn_pause.pack(side=tk.LEFT,padx=5)

btn_next = ctk.CTkButton(btn_frame,text=">",command=next_music,width=50,font=("TkDefaultFont",18))
btn_next.pack(side=tk.LEFT,padx=5)


pdar = Progressbar(window,length=300,mode="determinate")
pdar.pack(pady=10)

window.mainloop()
