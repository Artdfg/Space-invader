
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : faires plusieures aliens, avoir un nombre de vie/avoir de la vie, score, barrieres

"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox, LEFT #Importation des biblio

import random




#fenetre graphique
class jeu() :  


    def __init__ (self) : # crée ma fanetre du jeu space invader

        self.vie = 3
        self.score = 0

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

        self.labelScore = Label(self.fenetre_principale, textvariable = self.score) #affiche le score
        self.labelScore.pack(side = 'top')

        self.alien = alien(self) #cree les aliens
        self.joueur = joueur(self) #cree le vaisseau



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
    

    def __init__ (self, jeu) :

        self.jeu = jeu

        #recupere des variabales dautres classes utiles
        self.vie = jeu.vie
        self.score = jeu.score
        self.fenetre_principale = jeu.fenetre_principale
        self.ecran_jeu = jeu.ecran_jeu
        self.dim_ecran_jeu_x = jeu.dim_ecran_jeu_x
        self.alive = True
        self.role = "alien" #définit le role et permet de savoir qui tire le missile

        #pos initiale alien
        self.pos_alien_x = 5 
        self.pos_alien_y = 10
        

        self.sens = 1 #vaut plus ou moins 1 selon le sens de déplacement des aliens

        self.img_alien = PhotoImage(file = "alien.gif")     #dire que img_alien = vaisseau.gif
        self.moove_Alien = self.ecran_jeu.create_image(self.pos_alien_x, self.pos_alien_y, image=self.img_alien)       #Création de l'image et la place
        self.envie()

    def envie(self) :
        self.deplacement()
        self.tirer()

        if self.alive : 
            self.ecran_jeu.after(400, self.envie)
        
        

    def deplacement (self) :

        if self.pos_alien_x <= self.dim_ecran_jeu_x and self.pos_alien_x >= 0:

            self.ecran_jeu.move(self.moove_Alien, 25*self.sens, 0)
            self.pos_alien_x = self.pos_alien_x + 25*self.sens 
        
            

        if self.pos_alien_x >= self.dim_ecran_jeu_x or self.pos_alien_x <= 0:
            self.sens = -self.sens 
            self.pos_alien_x = self.pos_alien_x + 25*self.sens
            self.ecran_jeu.move(self.moove_Alien, 0, 25)
            self.pos_alien_y = self.pos_alien_y + 25

        if self.pos_alien_y >= 750 : #game over

            self.fenetre_principale.destroy()
        

    def tirer(self) :

        if random.randint(0,100)%8 == 0 : # revoir ca 
            print("bsr!!!!!!!")
            print(self.pos_alien_y)
            missile(self.jeu, self.role, self.moove_Alien)

         


#classe vaisseau
class joueur() :


    def __init__ (self, jeu) :
        self.jeu = jeu

        self.vie = jeu.vie
        self.score = jeu.score
        self.fenetre_principale = jeu.fenetre_principale
        self.ecran_jeu = jeu.ecran_jeu
        self.dim_ecran_jeu_x = jeu.dim_ecran_jeu_x

        self.role = "joueur"

        self.pos_x_max = 400
        self.pos_y_max = 750
        
        self.img_joueur = PhotoImage(file = "vaisseau.gif")     #dire que img_joueur = vaisseau.gif
        self.moove_Joueur = self.ecran_jeu.create_image(self.pos_x_max, self.pos_y_max, image=self.img_joueur)       #Création de l'image et la place
        

        self.fenetre_principale.bind('<Right>' , lambda event : self.moove_droite()) #On se déplace sur la droite
        self.fenetre_principale.bind('<Left>' , lambda event : self.moove_gauche()) #On se déplace sur la gauche
        self.fenetre_principale.bind('<space>' , lambda event : self.tirer()) #On envoie un missile
        
    
    def moove_droite (self) : #Quand l'event touche droite est activé 

        if self.pos_x_max < self.dim_ecran_jeu_x :    #On vérif qu'on va pas sortir de l'écran
        
            self.ecran_jeu.move(self.moove_Joueur, 25, 0)    #On bouge
            self.pos_x_max = self.pos_x_max + 25    #On actualise la valeur de pos_x_max


    def moove_gauche (self) :

        if self.pos_x_max > 0 :

            self.ecran_jeu.move(self.moove_Joueur, -25, 0)
            self.pos_x_max = self.pos_x_max - 25

    def tirer (self) :

        missile(self.jeu, self.role, self.moove_Joueur)




class missile() :

    def __init__(self, jeu, role, moove):
        self.jeu = jeu
        self.vie = jeu.vie
        self.score = jeu.score
        self.role = role
        self.ecran_jeu = jeu.ecran_jeu

        if self.role == "joueur" :
            self.pos_missile_x = jeu.joueur.pos_x_max
            self.pos_missile_y = jeu.joueur.pos_y_max
            self.moove_Joueur = moove
            self.img_missile = PhotoImage(file = "missile2.gif")
            self.sens = -1
        
        else : 
            self.moove_Alien = moove
            self.pos_missile_x = jeu.alien.pos_alien_x
            self.pos_missile_y = jeu.alien.pos_alien_y
            self.img_missile = PhotoImage(file = "missile3.gif")
            self.sens = 1
            
        self.moove_Missile = self.ecran_jeu.create_image(self.pos_missile_x, self.pos_missile_y + self.sens*25, image=self.img_missile)     #Création de l'image et la place

        self.prop_missile()
        
    def mvt_missile(self) :
    
        self.ecran_jeu.move(self.moove_Missile, 0, self.sens*25)
        self.pos_missile_y = self.pos_missile_y + self.sens*25

    def prop_missile (self) :
        
        self.mvt_missile()    
        self.sortie_ecran()
        self.contact()

        if not self.out_of_screen :
        
            self.ecran_jeu.after(100, self.prop_missile)

    def contact(self) :

        if self.role == "joueur" and len(self.ecran_jeu.find_overlapping(jouer.alien.pos_alien_x, jouer.alien.pos_alien_y , jouer.alien.pos_alien_x + 28, jouer.alien.pos_alien_y + 20 )) >=2 :
            print("h t a")
            #self.score = self.score + 100
            #print(self.score)
            self.jeu.alien.alive = False
            self.ecran_jeu.delete(self.moove_Missile)
            self.ecran_jeu.delete(jouer.alien.moove_Alien)
              
            
        if self.role == "alien" and len(self.ecran_jeu.find_overlapping(jouer.joueur.pos_x_max, jouer.joueur.pos_y_max , jouer.joueur.pos_x_max + 45, jouer.joueur.pos_y_max + 45 )) >=2 :
            print("A T H")
            self.jeu.vie = self.jeu.vie - 1
            print(self.jeu.vie)
            self.ecran_jeu.delete(self.moove_Missile)  
            if self.jeu.vie == 0 :
                self.ecran_jeu.delete(jouer.joueur.moove_Joueur) #et quitter
                print("quitter")
          

        self.ecran_jeu.after(100, self.contact)

        if not self.out_of_screen :
        
            self.ecran_jeu.after(100, self.prop_missile)

        # if 0 alien sur le terrain alors win 
    def sortie_ecran(self) :

        self.out_of_screen = False

        if self.role == "joueur" :

            if self.pos_missile_y < 0 :

                self.ecran_jeu.delete(self.moove_Missile)
                self.out_of_screen = True
            
        else :

            if self.pos_missile_y > 800 :

                self.ecran_jeu.delete(self.moove_Missile)
                self.out_of_screen = True






if __name__ == "__main__":

    jouer = jeu()
    jouer.f_affichage()
    




