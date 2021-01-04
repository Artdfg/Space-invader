
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : Canevas principal, label du score actuel, bouton qui lance la partie, bouton qui quitte proprement, Alien qui bouge tout seul, Joueur qui bouge
"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox #Importation des biblio


gif_dict = {}


#fenetre graphique
class jeu() :
    

    def __init__ (self) : # crée ma fanetre du jeu space invader

        self.fenetre_principale = Tk()
        self.fenetre_principale.title("Space invaders")
    
    def f_lancerjeu(self): #lance le jeu apres avoir appuyé sur le bouton jouer

        print("Le jeu se lance")
        #self.Score = "0"
        self.boutonJouer.destroy()
        self.labelScore = Label(self.fenetre_principale, text = "Score")
        self.labelScore.pack(side = 'top')


    def f_quit(self): #fenetre confirmation quitter le jeu

        self.Quitt = Tk()
        self.Quitt.title("Etes vous sur de quitter ?")
        self.Quitt.geometry('300x100')
        self.boutonOui = Button(self.Quitt,bg = 'red', text="Oui", command = self.quitter) #lance la fct quitter
        self.boutonNon = Button(self.Quitt,bg = 'blue', text ="Non", command = self.Quitt.destroy ) #renvoie a la fenetre principale
        self.boutonOui.grid(row=1, column=1)
        self.boutonNon.grid(row=1, column=2)
        self.Quitt.mainloop()

    def quitter(self): # quitte le jeu apres avoir cliqué sur oui

        self.Quitt.destroy()
        self.fenetre_principale.destroy()

    def f_affichage(self) :

        # canvas ecran de jeu
        self.ecran_jeu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
        self.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre

        # affichage image menu
        self.img_ouverture = PhotoImage(file = "image_menu.gif")
        self.ecran_jeu.create_image(0, 0, anchor = "nw", image = self.img_ouverture)
        self.ecran_jeu.config(height = self.img_ouverture.height(), width = self.img_ouverture.width()) 
        self.ecran_jeu.pack()
        
        #bouton jouer
        self.boutonJouer = Button(self.fenetre_principale, text="Jouer !", fg = 'red', command = self.f_lancerjeu)
        self.boutonJouer.pack()

        # bouton quitter
        self.boutonQuit = Button(self.fenetre_principale, text="Quitter", activebackground = 'red', activeforeground='white', command= self.f_quit)
        self.boutonQuit.pack(side= 'bottom')


        self.fenetre_principale.mainloop()



jouer = jeu()

jouer.f_affichage()





