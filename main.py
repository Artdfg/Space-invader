
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : Canevas principal, label du score actuel, bouton qui lance la partie, bouton qui quitte proprement, Alien qui bouge tout seul, Joueur qui bouge
"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, messagebox #Importation des biblio

dim_fenetre_principale_x = 800
dim_fenetre_principale_y = 600


fenetre_principale = Tk()
fenetre_principale.title("Space invaders")
fenetre_principale.geometry(str(dim_fenetre_principale_x) + "x" + str(dim_fenetre_principale_y))


def f_lancerjeu():
    print("Le jeu se lance")
    #Score = "0"
    boutonJouer.destroy()
    labelScore = Label(fenetre_principale, text = "Score")
    labelScore.pack(side = 'top')

def f_quit():
    global Quitt
    Quitt = Tk()
    Quitt.title("Etes vous sur de quitter ?")
    Quitt.geometry('300x100')
    boutonOui = Button(Quitt,bg = 'red', text="Oui", command = quitter)
    boutonNon = Button(Quitt,bg = 'blue', text ="Non", command = Quitt.destroy ) 
    boutonOui.grid(row=1, column=1)
    boutonNon.grid(row=1, column=2)
    Quitt.mainloop()

def quitter():
    Quitt.destroy()
    fenetre_principale.destroy()

def f_affichage() :

    ecran_jeu = Canvas(fenetre_principale , width = dim_fenetre_principale_x, height = dim_fenetre_principale_y*0.80 , bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
    ecran_jeu.pack()#inclusion, affichage du canvas dans la fenetre

    
    #img_ouverture = tk.PhotoImage(file = "../pendu_nico/hangman.gif")
    #canvas.create_image(0, 0, anchor = "nw", image = img_ouverture)
    #canvas.config(height = img_ouverture.height(), width = img_ouverture.width()) 
    #canvas.pack()

    global boutonJouer 
    boutonJouer = Button(fenetre_principale, text="Jouer !", fg = 'red', command = f_lancerjeu)
    boutonJouer.pack()

    boutonQuit = Button(fenetre_principale, text="Quitter", activebackground = 'red', activeforeground='white', command= f_quit)
    boutonQuit.pack(side= 'bottom')

f_affichage()


fenetre_principale.mainloop()

