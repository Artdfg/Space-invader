
"""
Code UTF-8
Created on Mon Dec 14
TP3-4 Space Invader
@Author : Roman Grim and Arthur Laudien
Todo : Canevas principal, label du score actuel, bouton qui lance la partie, bouton qui quitte proprement, Alien qui bouge tout seul, Joueur qui bouge
"""


from tkinter import Tk, Button, Canvas, Label, StringVar, IntVar, PhotoImage, filedialog, messagebox #Importation des biblio


dim_fenetre_principale_x = 800
dim_fenetre_principale_y = 600

gif_dict = {}

fenetre_principale = Tk()
fenetre_principale.title("Space invaders")
#fenetre_principale.geometry(str(dim_fenetre_principale_x) + "x" + str(dim_fenetre_principale_y))


class jeu() #fenetre graphique



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
    ecran_jeu.pack(padx = 5, pady = 5)#inclusion, affichage du canvas dans la fenetre




    #Affichage image ecran menu
    ecran_jeu.delete('all') # on efface la zone graphique
    file_name = filedialog.askopenfilename(title="Ouvrir une image", filetypes=[('gif files','.gif'),('all files','.*')])
    print (file_name)
    img_ouverture = PhotoImage(file = file_name)
    gif_dict[file_name] = img_ouverture  # référence
    print (gif_dict)
    
    """
    ecran_jeu.delete('all') # on efface la zone graphique

    img_ouverture = PhotoImage(file = "image_menu.gif")
    """

    ecran_jeu.create_image(0, 0, anchor = "nw", image = img_ouverture)
    ecran_jeu.config(height = img_ouverture.height(), width = img_ouverture.width()) 
    ecran_jeu.pack()

    global boutonJouer 
    boutonJouer = Button(fenetre_principale, text="Jouer !", fg = 'red', command = f_lancerjeu)
    boutonJouer.pack()


    #Score = "0"
    labelScore = Label(fenetre_principale, text = "Score")
    labelScore.pack()

    buttonJouer = Button(fenetre_principale, text="Jouer !", fg = 'red', command = f_lancerjeu)
    buttonJouer.pack()

    boutonQuit = Button(fenetre_principale, text="Quitter", activebackground = 'red', activeforeground='white', command= f_quit)
    boutonQuit.pack(side= 'bottom')

f_affichage()


fenetre_principale.mainloop()

