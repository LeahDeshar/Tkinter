import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import threading
import pygame
from mutagen.mp3 import MP3
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Store the current position of the music
current_position = 0
paused = False
selected_folder_path = ""  # Store the selected folder path

# Function to update the progress bar in a separate thread
def update_progress():
    global current_position
    while True:
        if pygame.mixer.music.get_busy() and not paused:
            current_position = pygame.mixer.music.get_pos() / 1000
            pbar["value"] = current_position

            # Check if the current song has reached its maximum duration
            if current_position >= pbar["maximum"]:
                stop_music()  # Stop the music playback
                pbar["value"] = 0  # Reset the progress bar
            window.update()
        time.sleep(0.1)

# Function to play the selected song
def play_selected_song():
    global current_position, paused
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        selected_song = lbox.get(current_index)
        full_path = os.path.join(selected_folder_path, selected_song)  # Add the full path again

        try:
            pygame.mixer.music.load(full_path)  # Load the selected song
        except pygame.error:
            print(f"Error loading {full_path}. Invalid or corrupt MP3 file.")
            return

        pygame.mixer.music.play(start=current_position)  # Play the song from the current position
        paused = False
        audio = MP3(full_path)
        song_duration = audio.info.length
        pbar["maximum"] = song_duration  # Set the maximum value of the progress bar to the song duration

# Function to play or unpause the music
def play_music():
    global paused
    if pygame.mixer.music.get_busy() and paused:
        # If the music is paused, unpause it
        pygame.mixer.music.unpause()
        paused = False
    else:
        # If no music is playing or paused, play the selected song
        play_selected_song()

# Function to pause the music
def pause_music():
    global paused
    # Pause the currently playing music
    pygame.mixer.music.pause()
    paused = True

# Function to stop the music
def stop_music():
    global paused
    # Stop the currently playing music and reset the progress bar
    pygame.mixer.music.stop()
    paused = False

# Function to select the music folder
def select_music_folder():
    global selected_folder_path
    selected_folder_path = filedialog.askdirectory()
    if selected_folder_path:
        lbox.delete(0, tk.END)
        for filename in os.listdir(selected_folder_path):
            if filename.endswith(".mp3"):
                lbox.insert(tk.END, filename)  # Insert only the filename, not the full path

# Function to go to the previous song
def previous_song():
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        if current_index > 0:
            lbox.selection_clear(0, tk.END)
            lbox.selection_set(current_index - 1)
            play_selected_song()

# Function to go to the next song
def next_song():
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        if current_index < lbox.size() - 1:
            lbox.selection_clear(0, tk.END)
            lbox.selection_set(current_index + 1)
            play_selected_song()

# Create a thread to update the progress bar
progress_thread = threading.Thread(target=update_progress)
progress_thread.daemon = True
progress_thread.start()

# Create the main window
window = tk.Tk()
window.title("Music Player App")
window.geometry("600x500")

# Create a label for the music player title
l_music_player = tk.Label(window, text="Music Player", font=("TkDefaultFont", 30, "bold"))
l_music_player.pack(pady=10)

# Create a button to select the music folder
btn_select_folder = tk.Button(window, text="Select Music Folder", command=select_music_folder,
                              font=("TkDefaultFont", 18))
btn_select_folder.pack(pady=20)

# Create a listbox to display the available songs
lbox = tk.Listbox(window, width=50, font=("TkDefaultFont", 16))
lbox.pack(pady=10)

# Create a frame to hold the control buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

# Create a button to go to the previous song
btn_previous = tk.Button(btn_frame, text="<", command=previous_song,
                         width=5, font=("TkDefaultFont", 18))
btn_previous.pack(side=tk.LEFT, padx=5)

# Create a button to play or pause the music
btn_play = tk.Button(btn_frame, text="Play/Reset", command=play_music,
                     width=10, font=("TkDefaultFont", 18))
btn_play.pack(side=tk.LEFT, padx=5)

# Create a button to pause the music
btn_pause = tk.Button(btn_frame, text="Pause", command=pause_music,
                      width=5, font=("TkDefaultFont", 18))
btn_pause.pack(side=tk.LEFT, padx=5)

# Create a button to go to the next song
btn_next = tk.Button(btn_frame, text=">", command=next_song,
                     width=5, font=("TkDefaultFont", 18))
btn_next.pack(side=tk.LEFT, padx=5)

# Create a progress bar to indicate the current song's progress
pbar = Progressbar(window, length=300, mode="determinate")
pbar.pack(pady=10)

window.mainloop()
