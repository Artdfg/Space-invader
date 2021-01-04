
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : missiles et destruction des items et creer plusieurs aliens

renommer les variables de postion du vaisseau !!!!!!!!!!!!

"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox, LEFT #Importation des biblio

import time


#fenetre graphique
class jeu() :  

    def __init__ (self) : # crée ma fanetre du jeu space invader

        self.fenetre_principale = Tk()
        self.fenetre_principale.title("Space invaders")
    
    def f_lancerjeu(self): #lance le jeu apres avoir appuyé sur le bouton jouer

        print("Le jeu se lance")
        #self.Score = "0"
        self.boutonJouer.destroy()
        self.ecran_menu.destroy()

        self.ecran_jeu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
        self.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre
        self.ecran_jeu.config(height = 800, width = 800)

        self.labelScore = Label(self.fenetre_principale, text = "Score")
        self.labelScore.pack(side = 'top')

        self.joueur = joueur(self.ecran_jeu, self.fenetre_principale)
        self.alien = alien(self.ecran_jeu, self.fenetre_principale)


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
        self.ecran_menu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
        self.ecran_menu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre

        # affichage image menu
        self.img_ouverture = PhotoImage(file = "image_menu.gif")
        self.ecran_menu.create_image(0, 0, anchor = "nw", image = self.img_ouverture)
        self.ecran_menu.config(height = self.img_ouverture.height(), width = self.img_ouverture.width()) 
        self.ecran_menu.pack()
        
        #bouton jouer
        self.boutonJouer = Button(self.fenetre_principale, text="Jouer !", fg = 'red', command = self.f_lancerjeu)
        self.boutonJouer.pack()

        #bouton quitter
        self.boutonQuit = Button(self.fenetre_principale, text="Quitter", activebackground = 'red', activeforeground='white', command= self.f_quit)
        self.boutonQuit.pack(side= 'bottom')


        self.fenetre_principale.mainloop()

class joueur() :

    def __init__ (self, ecran_jeu,fenetre_principale) :
        self.fenetre_principale = fenetre_principale
        self.ecran_jeu = ecran_jeu
        self.img_joueur = PhotoImage(file = "vaisseau.gif")     #dire que img_joueur = vaisseau.gif
        self.moove = self.ecran_jeu.create_image(400, 750, image=self.img_joueur)       #Création de l'image et la place
        
        self.fenetre_principale.bind('<Right>' , lambda event : self.moove_droite()) #On se déplace sur la droite
        self.fenetre_principale.bind('<Left>' , lambda event : self.moove_gauche()) #On se déplace sur la gauche
        self.posX = 400
        #ecran_jeu.move(self.moove,100,100)      #Exemple mouvement 

    def moove_droite (self) : #Quand l'event touche droite est activé 
        if self.posX < 800 :    #On vérif qu'on va pas sortir de l'écran
            self.ecran_jeu.move(self.moove,50,0)    #On bouge
            self.posX = self.posX+50    #On actualise la valeur de posX

    def moove_gauche (self) :
        if self.posX > 0 :
            self.ecran_jeu.move(self.moove,-50,0)
            self.posX = self.posX-50







class alien() :
    
    def __init__ (self, ecran_jeu, fenetre_principale) :


        self.pos_alienX = 0
        self.pos_alienY = 50

        self.fenetre_principale = fenetre_principale
        self.ecran_jeu = ecran_jeu

        self.sens = 1

        self.img_alien = PhotoImage(file = "alien.gif")     #dire que img_alien = vaisseau.gif
        self.moove = self.ecran_jeu.create_image(self.pos_alienX, self.pos_alienY, image=self.img_alien)       #Création de l'image et la place


        self.posX = 0
        self.posY = 0


        self.deplacement()





    def deplacement (self) :


        
        if self.posX <= 800 and self.posX >= 0:

            self.ecran_jeu.move(self.moove, 25*self.sens, 0)
            self.posX = self.posX + 25*self.sens 
        
            self.ecran_jeu.after(self.pos_alienY, self.deplacement)
        

        if self.posX == 800 or self.posX == 0:
        
            self.sens = -self.sens 
            self.ecran_jeu.move(self.moove, 0, 100)
            self.pos_alienY = self.pos_alienY + 100

        
        if self.pos_alienY == 750 :

            self.fenetre_principale.destroy()



  

        
        
            

            

        


        

        







        



jouer = jeu()

jouer.f_affichage()





