import socket
from threading import Thread
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

window = tk.Tk()


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def setup():
    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    musicWindow()

    setup()


def musicWindow():
    window.title('Music Window')
    window.geometry("400x900")
    window.configure(bg='LightSkyBlue')

selectSong = tk.Label(window, text="Select the Song : ", bg='LightSkyBLue', font = ("Calibri", 8))
selectSong.place(x=60,y=2)

SonglistBox = tk.Listbox(window, height=10, width=39, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font = ("Calibri",10))
SonglistBox.place(x=10,y=10)

scrollbar1 = tk.Scrollbar(SonglistBox)
scrollbar1.place(relheight=1, relx=1)
scrollbar1.config(command = SonglistBox.yview)

playButton = tk.Button(window, text="Play",width=10, bd=1, bg='SkyBlue', font=("Calibri",10))
playButton.place(x=30,y=200)

Stop = tk.Button(window, text="Stop",width=10, bd=1, bg='SkyBlue', font=("Calibri",10))
Stop.place(x=200,y=200)

Upload = tk.Button(window, text="upload",width=10, bd=1, bg='SkyBlue', font=("Calibri",10))
Upload.place(x=30,y=250)

Download = tk.Button(window, text="Download",width=10, bd=1, bg='SkyBlue', font=("Calibri",10))
Download.place(x=200,y=250)

infoLabel = tk.Label(window, text="", fg="blue", font = ("Calibri",8))
infoLabel.place(x=4,y=280)

window.mainloop()

musicWindow()
    
