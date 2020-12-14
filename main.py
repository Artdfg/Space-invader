
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : Canevas principal, label du score actuel, bouton qui lance la partie, bouton qui quitte proprement, Alien qui bouge tout seul, Joueur qui bouge
"""



from tkinter import Tk, Button, Canvas, StringVar, IntVar


dim_fenetre_principale_x = 800
dim_fenetre_principale_y = 600


fenetre_principale = Tk()
fenetre_principale.title("Space invaders")
fenetre_principale.geometry(str(dim_fenetre_principale_x) + "x" + str(dim_fenetre_principale_y))



def f_affichage() :

    ecran_jeu = Canvas(fenetre_principale , width = dim_fenetre_principale_x, height = dim_fenetre_principale_y*0.80 , bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
    ecran_jeu.pack()#inclusion, affichage du canvas dans la fenetre

    
    #img_ouverture = tk.PhotoImage(file = "../pendu_nico/hangman.gif")
    #canvas.create_image(0, 0, anchor = "nw", image = img_ouverture)
    #canvas.config(height = img_ouverture.height(), width = img_ouverture.width()) 
    #canvas.pack()







f_affichage()



fenetre_principale.mainloop()
