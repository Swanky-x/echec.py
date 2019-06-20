#######Importations des fonctions########

from tkinter import *
from random import * #pour la génération aléatoire des pions

#######Définition des fonctions##########
def cercle(x, y, r, coul ='red'):#pour le dessin des pions
    "tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)
    
def remplir(y):#calcul des coord de la ligne
    x=0
    liste=[]
    while x<200:
        liste.append([x,y,x+20,y+20])
        x=x+20
    return liste

def figure_1():
    "dessiner le damier"
    global x,y,damier
    x=0
    y=0
    # Effacer d'abord tout dessin préexistant :
    can.delete(ALL)
    #definition de la matrice du damier
    damier=[]
    while y<200:
        damier.append(remplir(y))#on remplit avec les coordonnées des cases de la ligne
        y=y+20
    a=0
    while a<10:#on trace la premiere partie du damier
        
        al=damier[a]
        b=0
        while b<10:
            al1=al[b]
            can.create_rectangle(al1[0],al1[+1],al1[2],al1[3],fill='black')
            b=b+2   
        a=a+2
    a=1
    # while a<10:#on recommence avec un décalage de 1 en abcsisses et un en ordonnées pour la
    #     #deuxieme partie du damier
        
    #     al=damier[a]
    #     b=1
    #     while b<10:
    #         al1=al[b]
    #         can.create_rectangle(al1[0],al1[+1],al1[2],al1[3],fill='black')
    #         b=b+2   
    #     a=a+2
    
     
def figure_2():
    """dessiner des pions de manière aléatoire"""
    alea=randrange(10)#on sélectionne une position au hasard sur la matrice
    alea1=randrange(10)
    ligne=damier[alea]#on prend les coordonnées aléatoires
    case=ligne[alea1]
    x=case[0]+10#on centre le pion
    y=case[1]+10
    cercle(x,y,10,'red')#et on le dessine
   

def pointeur(event):
    """Dessine un pion la ou l'utilisateur a cliqué"""
    x=event.x%20
    x=(event.x-x)+10
    y=event.y%20
    y=(event.y-y)+10
    ##print x,y#debugging
    

    
    cercle(x,y,10,'green')

##### Programme principal : ############
global damier
fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='white')
can.bind("<Button-1>", pointeur)
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='damier', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='pions', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
b3 = Button(fen, text ='Quitter', command =fen.destroy)
b3.pack(side =BOTTOM,padx =3, pady =3)
fen.mainloop()