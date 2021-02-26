from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.geometry("600x300")
root.iconbitmap('assets/reproductor.ico')

root.resizable(0,0)





def addSong():
    songs = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__)))
    for song in songs:
        song = song.replace(os.path.dirname(os.path.abspath(__file__)),"")
        song = song.replace('.ogg', '')

    # add to screen
    screen.insert(songs)
def pause():
    mixer.music.pause()


def play():
    
    mixer.init()
    mixer.music.load()
    mixer.music.play()


def resume():
    mixer.music.unpause()

# def buscar():
#     canciones = filedialog.askopenfile()

#     for cancion in canciones:
#         cancion = cancion.replace('C:/Download', types=".mp3")
#     print(file)




## Interfaz Reproductor 


screen = Listbox(root, bg='lightblue', width=60, selectbackground= 'white', selectforeground='black')
screen.pack(pady=20)

btnAdd = Button(root, text="Agregar", command=addSong).pack(side = LEFT, padx=20, pady=10)


title = Label(root, text="Welcome to music player")
title['font'] = ("Consolas", 25, "bold")
title.pack()
btnPlay = Button(root, text="Play", command=play).pack(side = LEFT, padx=20, pady=10)
btnPause = Button(root,text="Pause", command=pause).pack(side = LEFT)
btnNextSong = Button(root,text="Resume", command=resume).pack(side = LEFT)
btnBackSong = Button(root,text="Quit", command=quit).pack(side = LEFT)

root.mainloop()
