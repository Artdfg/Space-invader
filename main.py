
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : missiles et destruction des items et creer plusieurs aliens

renommer les variables de postion du vaisseau !!!!!!!!!!!!

"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox, LEFT #Importation des biblio

import random


#fenetre graphique
class jeu() :  


    def __init__ (self) : # crée ma fanetre du jeu space invader

        self.fenetre_principale = Tk()
        self.fenetre_principale.title("Space invaders")
    

    def f_lancerjeu(self): #lance le jeu apres avoir appuyé sur le bouton jouer

        self.dim_ecran_jeu_x = 800 #dimension écran_jeu
        self.dim_ecran_jeu_y = 800

        self.boutonJouer.destroy()
        self.ecran_menu.destroy()

        self.ecran_jeu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas a linterieur de la fenetre tkinter auquel on peut ajouter des trucs
        self.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre
        self.ecran_jeu.config(height = self.dim_ecran_jeu_x, width = self.dim_ecran_jeu_y) #dimension ecran_jeu

        self.labelScore = Label(self.fenetre_principale, text = "Score") #affiche le score
        self.labelScore.pack(side = 'top')

        self.joueur = joueur(self.ecran_jeu, self.fenetre_principale, self.dim_ecran_jeu_x) #cree le vaisseau
        self.alien = alien(self.ecran_jeu, self.fenetre_principale, self.dim_ecran_jeu_x) #cree les aliens


    def f_quit(self): #fenetre confirmation quitter le jeu

        self.Quitt = Tk()
        self.Quitt.title("Etes vous sur de quitter ?")
        self.Quitt.geometry('50x25') #dimension fentre quitter
        self.boutonOui = Button(self.Quitt,bg = 'red', text="Oui", command = self.quitter) #bouton qui lance la fct quitter
        self.boutonNon = Button(self.Quitt,bg = 'blue', text ="Non", command = self.Quitt.destroy ) # bouton qui renvoie a la fenetre principale
        self.boutonOui.grid(row=1, column=1) #placement boutons
        self.boutonNon.grid(row=1, column=2)
        self.Quitt.mainloop()


    def quitter(self): # quitte le jeu apres avoir cliqué sur oui

        self.Quitt.destroy()
        self.fenetre_principale.destroy()


    def f_affichage(self) : #cree le menu 

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



#class alien
class alien() :
    

    def __init__ (self, ecran_jeu, fenetre_principale, dim_ecran_jeu_x) :

        #recupere des variabales dautres classes utiles
        self.fenetre_principale = fenetre_principale
        self.ecran_jeu = ecran_jeu
        self.dim_ecran_jeu_x = dim_ecran_jeu_x

        self.role = "alien" #définit le role et permet de savoir qui tire le missile

        #pos initiale alien
        self.pos_alien_x = 5 
        self.pos_alien_y = 10

        self.sens = 1 #vaut plus ou moins 1 selon le sens de déplacement des aliens

        self.img_alien = PhotoImage(file = "alien.gif")     #dire que img_alien = vaisseau.gif
        self.moove = self.ecran_jeu.create_image(self.pos_alien_x, self.pos_alien_y, image=self.img_alien)       #Création de l'image et la place

        self.deplacement()
        self.tirer()


    def deplacement (self) :
        
        print(self.pos_alien_x)
        print(self.pos_alien_y)


        if self.pos_alien_x <= self.dim_ecran_jeu_x and self.pos_alien_x >= 0:

            print(self.pos_alien_x)
            print(self.pos_alien_y)

            self.ecran_jeu.move(self.moove, 25*self.sens, 0)
            self.pos_alien_x = self.pos_alien_x + 25*self.sens 

        if self.pos_alien_x >= self.dim_ecran_jeu_x or self.pos_alien_x <= 0:
        
            self.sens = -self.sens 
            self.ecran_jeu.move(self.moove, 0, 25)
            self.pos_alien_y = self.pos_alien_y + 25

        if self.pos_alien_y >= 750 : #game over

            self.fenetre_principale.destroy()

        self.ecran_jeu.after(400, self.deplacement)


    def tirer(self) :

        if random.randint(0,100)%8 == 0 : 
            print("bsr!!!!!!!")
            print(self.pos_alien_y)
            self.missile = missile(self.pos_alien_x, self.pos_alien_y, self.ecran_jeu, self.role)

        self.ecran_jeu.after(400, self.tirer) 











#classe vaisseau
class joueur() :


    def __init__ (self, ecran_jeu, fenetre_principale, dim_ecran_jeu_x) :

        self.fenetre_principale = fenetre_principale
        self.ecran_jeu = ecran_jeu
        self.dim_ecran_jeu_x = dim_ecran_jeu_x

        self.role = "joueur"

        self.pos_x_max = 400
        self.pos_y_max = 750
        
        self.img_joueur = PhotoImage(file = "vaisseau.gif")     #dire que img_joueur = vaisseau.gif
        self.moove = self.ecran_jeu.create_image(self.pos_x_max, self.pos_y_max, image=self.img_joueur)       #Création de l'image et la place
        
        self.fenetre_principale.bind('<Right>' , lambda event : self.moove_droite()) #On se déplace sur la droite
        self.fenetre_principale.bind('<Left>' , lambda event : self.moove_gauche()) #On se déplace sur la gauche
        self.fenetre_principale.bind('<space>' , lambda event : self.tirer()) #On envoie un missile
        
    
    def moove_droite (self) : #Quand l'event touche droite est activé 

        if self.pos_x_max < self.dim_ecran_jeu_x :    #On vérif qu'on va pas sortir de l'écran
        
            self.ecran_jeu.move(self.moove, 25, 0)    #On bouge
            self.pos_x_max = self.pos_x_max + 25    #On actualise la valeur de pos_x_max


    def moove_gauche (self) :

        if self.pos_x_max > 0 :

            self.ecran_jeu.move(self.moove, -25, 0)
            self.pos_x_max = self.pos_x_max - 25


    def tirer (self) :

        self.missile = missile(self.pos_x_max, self.pos_y_max, self.ecran_jeu, self.role)






       


class missile() :


    def __init__(self, pos_x, pos_y, ecran_jeu, role) :

        self.pos_missile_x = pos_x
        self.pos_missile_y = pos_y

        self.ecran_jeu = ecran_jeu


        if role == "joueur" :

            self.img_missile = PhotoImage(file = "missile2.gif")
        
        else : 

            self.img_missile = PhotoImage(file = "missile3.gif")
            
        self.moove = self.ecran_jeu.create_image(self.pos_missile_x, self.pos_missile_y, image=self.img_missile)     #Création de l'image et la place

        if role == "joueur" :
    
            self.mvt_missile_vaisseau()
            self.contact_vaisseau()
        
        else : 

            self.mvt_missile_alien()
            self.contact_alien()
        




    def mvt_missile_vaisseau(self) :

        self.ecran_jeu.move(self.moove, 0, -25)
        self.pos_missile_y = self.pos_missile_y - 25

        self.ecran_jeu.after(100, self.mvt_missile_vaisseau) 


    def contact_vaisseau(self) :

        if self.pos_missile_x == jouer.alien.pos_alien_x and self.pos_missile_y == jouer.alien.pos_alien_y :

            print("touché !!!!!!!!!!!!!!!!!!")

            #score = score + 1

            #alien disparait

        self.ecran_jeu.after(100, self.contact_vaisseau)

        # if 0 alien sur le terrain alors win 




    def mvt_missile_alien(self) :
    
        self.ecran_jeu.move(self.moove, 0, 25)
        self.pos_missile_y = self.pos_missile_y + 25

        self.ecran_jeu.after(100, self.mvt_missile_alien) 


    def contact_alien(self) : #game over

        if self.pos_missile_x == jouer.alien.pos_alien_x and self.pos_missile_y == jouer.alien.pos_alien_y :

            print("touché !!!!!!!!!!!!!!!!!!")

            

        self.ecran_jeu.after(100, self.contact_alien)









if __name__ == "__main__":

    jouer = jeu()
    jouer.f_affichage()
    




