from tkinter import *
import pygame

window = Tk()
window.title('Meme SoundBoard')


pygame.mixer.init()

def cityfolk():
    pygame.mixer.music.load('C:\Users\HP ProBook 6550b\Downloads\City Folk.mp3')
    pygame.mixer.music.play(loop=0)

cityfolk = Button(window, text='City Folk', command=cityfolk)
cityfolk.pack()



window.mainloop()
