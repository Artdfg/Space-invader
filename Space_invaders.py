"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : barrieres
"""


#Importation des biblio
from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox 
import random


#fenetre graphique + dieu
class Jeu() :  


    def __init__ (self) : # crée ma fanetre du jeu space invader

        self.vie = 3 
        self.score = 0
        self.nb_aliens = 12

        self.liste_alien = [] #Contient les instances de la classe Alien

        #Crée la fenetre principale
        self.fenetre_principale = Tk() 
        self.fenetre_principale.title("Space invaders")
    

    def f_lancerjeu(self): #lance le jeu apres avoir appuyé sur le bouton jouer

        # dimension écran_jeu
        self.dim_ecran_jeu_x = 800 
        self.dim_ecran_jeu_y = 600

        #enleve les boutons de lecran
        self.boutonJouer.destroy()
        self.ecran_menu.destroy()

        # crée l'écran de jeu
        self.ecran_jeu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas a linterieur de la fenetre tkinter auquel on peut ajouter des éléments
        self.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre
        self.ecran_jeu.config(height = self.dim_ecran_jeu_y, width = self.dim_ecran_jeu_x) #dimension ecran_jeu
        
        #Crée 12 instances de Alien et les place dans la liste
        for indice_alien in range (self.nb_aliens) : 

            self.alien = Alien(self, indice_alien) #cree les aliens
            self.liste_alien.append(self.alien) #cree les aliens

        self.joueur = Joueur(self) #cree le vaisseau

        self.f_comportement_alien() # fct qui définit le comportement des aliens.


    def f_comportement_alien(self) :

        for alien in self.liste_alien : #comportement a adopter pour chacun des aliens en vie
            
            alien.f_deplacement()
            alien.f_tirer()

        if self.liste_alien != [] : #se répete tant qu'il y a toujours un alien sur le terrain
    
            self.ecran_jeu.after(30*len(self.liste_alien) , self.f_comportement_alien)


    def f_quit(self): #fenetre confirmation quitter le jeu

        self.Quitt = Tk()
        self.Quitt.title("Etes vous sur de quitter ?")
        self.Quitt.geometry('50x25') #dimension fentre quitter
        self.boutonOui = Button(self.Quitt,bg = 'red', text="Oui", command = self.f_quitter) #bouton qui lance la fct quitter
        self.boutonNon = Button(self.Quitt,bg = 'blue', text ="Non", command = self.Quitt.destroy ) # bouton qui renvoie a la fenetre principale
        self.boutonOui.grid(row=1, column=1) #placement boutons
        self.boutonNon.grid(row=1, column=2)
        self.Quitt.mainloop()


    def f_quitter(self): # quitte le jeu apres avoir cliqué sur oui

        self.Quitt.destroy()
        self.fenetre_principale.destroy()


    def f_affichage(self) : #cree le menu 

        # canvas ecran de jeu
        self.ecran_menu = Canvas(self.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter auquel on peut ajouter des éléments
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

        #Label vie
        self.affichage_vie = StringVar()
        self.affichage_vie.set('Vie : ' + str(self.vie))
        self.texteLabel_vie = Label(self.fenetre_principale, textvariable = self.affichage_vie)
        self.texteLabel_vie.pack(side = 'bottom')

        #label score
        self.affichage_score = StringVar()
        self.affichage_score.set('Score : ' + str(self.score))
        self.texteLabel_score = Label(self.fenetre_principale, textvariable = self.affichage_score)
        self.texteLabel_score.pack(side = 'bottom')



        self.fenetre_principale.mainloop()



#class alien
class Alien() :
    

    def __init__ (self, jeu, indice_alien) :

        self.jeu = jeu

        #recupere des variabales de la classe dieu utiles
        self.vie = jeu.vie
        self.score = jeu.score
        self.fenetre_principale = jeu.fenetre_principale
        self.ecran_jeu = jeu.ecran_jeu
        self.dim_ecran_jeu_x = jeu.dim_ecran_jeu_x

        self.role = "alien" #définit le role et permet de savoir qui tire le missile

        self.indice_alien = indice_alien #numéro de création de l'alien

        #pos initiale alien
        self.pos_alien_x = 5 + self.indice_alien*50
        self.pos_alien_y = 10
        
        self.sens = 1 #vaut plus ou moins 1 selon le sens de déplacement des aliens

        # création de l'image et la place
        self.img_alien = PhotoImage(file = "alien.gif")    
        self.moove_Alien = self.ecran_jeu.create_image(self.pos_alien_x, self.pos_alien_y, image=self.img_alien)     


    #deplacement alien
    def f_deplacement (self) :

        #deplacement latéraux
        if self.pos_alien_x <= self.dim_ecran_jeu_x and self.pos_alien_x >= 0:

            self.ecran_jeu.move(self.moove_Alien, 25*self.sens, 0)
            self.pos_alien_x = self.pos_alien_x + 25*self.sens 
        
            
        #déplacement vers le bas des qu'on arrive à une extrémité de l'écran
        if self.pos_alien_x >= self.dim_ecran_jeu_x or self.pos_alien_x <= 0:

            self.sens = -self.sens 
            self.pos_alien_x = self.pos_alien_x + 25*self.sens
            self.ecran_jeu.move(self.moove_Alien, 0, 40)
            self.pos_alien_y = self.pos_alien_y + 40

        #game over si alien sur la même ligne que vaisseau
        if self.pos_alien_y >= 550 : 

            self.ecran_jeu.destroy() #detruit l'ecran de jeu

            self.jeu.ecran_jeu = Canvas(self.jeu.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter 
            self.jeu.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre

            #affiche l'image de game over
            self.img_gameover = PhotoImage(file = "game_over.gif")
            self.jeu.ecran_jeu.create_image(0, 0, anchor = "nw", image = self.img_gameover)
            self.jeu.ecran_jeu.config(height = self.img_gameover.height(), width = self.img_gameover.width()) 
            self.jeu.ecran_jeu.pack()
        
    #tire alien
    def f_tirer(self) :

        #Probabilité de tirer d'un alien
        if random.randint(0,100)%25 == 0 : 

            Missile(self.jeu, self.role, self.moove_Alien, self.indice_alien)

         


#classe vaisseau
class Joueur() :


    def __init__ (self, jeu) :

        self.jeu = jeu

        self.vie = jeu.vie
        self.score = jeu.score
        self.fenetre_principale = jeu.fenetre_principale
        self.ecran_jeu = jeu.ecran_jeu
        self.dim_ecran_jeu_x = jeu.dim_ecran_jeu_x

        self.role = "joueur"

        #position initiale du vaisseau
        self.pos_x_max = 400
        self.pos_y_max = 550
        
        #Création de l'image et la place
        self.img_joueur = PhotoImage(file = "vaisseau.gif")   
        self.moove_Joueur = self.ecran_jeu.create_image(self.pos_x_max, self.pos_y_max, image=self.img_joueur)       
        
        self.fenetre_principale.bind('<Right>' , lambda event : self.f_moove_droite()) #On se déplace sur la droite
        self.fenetre_principale.bind('<Left>' , lambda event : self.f_moove_gauche()) #On se déplace sur la gauche
        self.fenetre_principale.bind('<space>' , lambda event : self.f_tirer()) #On envoie un missile
        
    
    def f_moove_droite (self) : #Quand l'event touche droite est activé 

        if self.pos_x_max < self.dim_ecran_jeu_x :    #On vérif qu'on va pas sortir de l'écran
        
            self.ecran_jeu.move(self.moove_Joueur, 25, 0)    #On bouge
            self.pos_x_max = self.pos_x_max + 25    #On actualise la valeur de pos_x_max


    def f_moove_gauche (self) : #Quand l'event touche gauche est activé 

        if self.pos_x_max > 0 :#On vérif qu'on va pas sortir de l'écran

            self.ecran_jeu.move(self.moove_Joueur, -25, 0) #On bouge
            self.pos_x_max = self.pos_x_max - 25 #On actualise la valeur de pos_x_max

    #Quand l'évent touche espace est activé
    def f_tirer (self) :

        Missile(self.jeu, self.role, self.moove_Joueur, False)



#classe missile + gestion collision + sortie d'écran + morts
class Missile() :

    def __init__(self, jeu, role, moove, indice):

        self.jeu = jeu
        self.vie = jeu.vie
        self.score = jeu.score
        self.role = role
        self.ecran_jeu = jeu.ecran_jeu

        #Si un joueur tire le missile
        if self.role == "joueur" :

            self.moove_Joueur = moove #tag tKinter du joueur
            self.pos_missile_x = jeu.joueur.pos_x_max #pos initiale du missile
            self.pos_missile_y = jeu.joueur.pos_y_max
            self.img_missile = PhotoImage(file = "missile1.gif") #image missile vers le haut
            self.sens = -1 
        
        #Si un alien tire le missile
        else : 

            self.moove_Alien = moove #tag tKinter de l'alien
            self.indice_alien = indice
            self.pos_missile_x = self.jeu.liste_alien[self.indice_alien - 1].pos_alien_x #pos initiale du missile
            self.pos_missile_y = self.jeu.liste_alien[self.indice_alien - 1].pos_alien_y
            self.img_missile = PhotoImage(file = "missile2.gif") #image missile vers le bas
            self.sens = 1
            
        #Création de l'image d'un missile et la place
        self.moove_Missile = self.ecran_jeu.create_image(self.pos_missile_x, self.pos_missile_y + self.sens*25, image=self.img_missile)     

        #lance les méthodes importantes de la classe missile
        self.f_prop_missile()
        

    def f_prop_missile (self) :
        
        self.f_mvt_missile()    
        self.f_sortie_ecran() 
        self.f_contact()

        if not self.out_of_screen :
        
            self.ecran_jeu.after(200, self.f_prop_missile)


    #Déplacement du missile
    def f_mvt_missile(self) :
        
        #vers le haut si self.sens = -1 et vers le bas si self.sens = 1
        self.ecran_jeu.move(self.moove_Missile, 0, self.sens*25)
        self.pos_missile_y = self.pos_missile_y + self.sens*25


    #Gère les contacts entre les missiles et les autres entitées
    def f_contact(self) :

        if self.role == "joueur" :#missile tiré par le vaisseau
        
            #parcourt la liste des instances de alien et teste pour chacun des aliens si il y a collision
            for ali in self.jeu.liste_alien : 

                 if len(self.ecran_jeu.find_overlapping(ali.pos_alien_x, ali.pos_alien_y , ali.pos_alien_x + 28, ali.pos_alien_y + 20 )) >=2 :
                    
                    self.jeu.score = self.jeu.score + 100 #Le score augmente
                    self.jeu.affichage_score.set('Score : ' + str(self.jeu.score)) #maj de l'affichage du score
                    
                    self.ecran_jeu.delete(self.moove_Missile) #On supprime la référence du missile
                    self.ecran_jeu.delete(ali.moove_Alien)  #On supprime la référence de l'alien
                    self.jeu.liste_alien.remove(ali) #on enleve l'instance de l'alien de la liste les contenant

                    self.out_of_screen = True #Permet d'arréter de lancer la méthode prop_missile

                    # Réasigne les rangs des aliens une fois l'un d'eux détruit
                    for al in self.jeu.liste_alien :

                        al.indice_alien = self.jeu.liste_alien.index(al) + 1

                    break 

            
            #victoire tous les aliens sont morts
            if len(self.jeu.liste_alien) == 0 :

                self.ecran_jeu.destroy() #detruit l'ecran de jeu

                self.jeu.ecran_jeu = Canvas(self.jeu.fenetre_principale)#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter 
                self.jeu.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre

                #affiche l'image de game over
                self.img_victoire = PhotoImage(file = "victoire.gif")
                self.jeu.ecran_jeu.create_image(0, 0, anchor = "nw", image = self.img_victoire)
                self.jeu.ecran_jeu.config(height = self.img_victoire.height(), width = self.img_victoire.width()) 
                self.jeu.ecran_jeu.pack()

              
        #missile tiré par l'alien
        if self.role == "alien" and len(self.ecran_jeu.find_overlapping(jouer.joueur.pos_x_max, jouer.joueur.pos_y_max , jouer.joueur.pos_x_max + 45, jouer.joueur.pos_y_max + 45 )) >=2 :
            
            self.jeu.vie = self.jeu.vie - 1 #la vie diminue de 1
            self.jeu.affichage_vie.set('Vie : ' + str(self.jeu.vie)) #met a jour l'affichage des vies
            self.ecran_jeu.delete(self.moove_Missile)  #on supprime le missile de l'ecran

            self.out_of_screen = True #Permet d'arréter de lancer la méthode prop_missile


            # Game over : demarre le script finale lorsque le joueur n'a plus de vie
            if self.jeu.vie == 0 :

                self.ecran_jeu.destroy() #detruit l'ecran de jeu

                self.jeu.ecran_jeu = Canvas(self.jeu.fenetre_principale, bg='white')#creation d'un canvas, zone de dessin a linterieur de la fenetre tkinter 
                self.jeu.ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre

                #affiche l'image de game over
                self.img_gameover = PhotoImage(file = "game_over.gif")
                self.jeu.ecran_jeu.create_image(0, 0, anchor = "nw", image = self.img_gameover)
                self.jeu.ecran_jeu.config(height = self.img_gameover.height(), width = self.img_gameover.width()) 
                self.jeu.ecran_jeu.pack()
          

    # Détruit le missile à la sortie de l'écran pour éviter d'utiliser des ressources inutiles
    def f_sortie_ecran(self) :

        self.out_of_screen = False

        if self.role == "joueur" : # si le missile est tiré par un joueur, on cherche à savoir si le missile a dépassé le haut de l'écran

            if self.pos_missile_y < 0 :

                #Supprime le missile
                self.ecran_jeu.delete(self.moove_Missile)
                self.out_of_screen = True
            
        else :

            if self.pos_missile_y > 600 : # si le missile est tiré par un joueur, on cherche à savoir si le missile a dépassé le bas de l'écran

                #Supprime le missile
                self.ecran_jeu.delete(self.moove_Missile)
                self.out_of_screen = True


#programme principal
if __name__ == "__main__":

    jouer = Jeu()
    jouer.f_affichage()