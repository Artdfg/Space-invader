
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : Canevas principal, label du score actuel, bouton qui lance la partie, bouton qui quitte proprement, Alien qui bouge tout seul, Joueur qui bouge
"""
print("arthur le jul")
from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar #Importation des biblio

def f_lancerjeu():
    print("Le jeu se lance")

fenetre_principale = Tk()
fenetre_principale.title("Space invaders")
fenetre_principale.geometry("800x600")

Score = "0"
labelScore = Label(fenetre_principale, text = "Score")
labelScore.pack()

buttonJouer = Button(fenetre_principale, text="Jouer !", fg = 'red', command = f_lancerjeu)
buttonJouer.pack()


fenetre_principale.mainloop()

