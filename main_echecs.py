"""
@-- jeu echecs en reseau --@ :-)

Proposer un jeu d'echecs, ou je peux affronter un adversaire sur le reseau

[ COTE USER ]
____
> chessX
____

*- un affichage terminal serait plus simple pour commencer -*
*- un affichage avec Tkinter serait excellent par la suite -*

[ COTE APPLICATION ]

architecture client-serveur.

Un serveur http python pourrait "d'emmeteur" sur les emplacements des nouveaux coups.
on affichera toutes les pieces sur les nouvelles positions coté utilisateur.


               SERVEUR
            /          
           / "fou A3"    \ "fou A3"
    player1              player2       ----> *affiche le fou en A3*

     ----------------------->

-logs

[ A suivre ]

-tableaux des derniers match sur index.html
-systeme de sauvegarde de partie coté serveur
-a vous de trouver
"""


# liste_pieces=[]
# liste_positions=[]
# liste_positions_noire=[]
# liste_positions_blanche=[]
# liste_colonnes=("A","B","C","D","E","F","G","H")
# liste_lignes=(1,2,3,4,5,6,7,8)

# cadre=[]
# for i in 1,2,3,4,5,6,7,8:
#     for j in 1,2,3,4,5,6,7,8:
#         cadre.append(int(f"{i}{j}"))

# print(cadre)

# def surLePlateau(case):
#     if case in cadre:
#         print(case,"est sur le plateau")
#         return True
#     else:
#         print(case, "n'est pas sur le plateau")

# surLePlateau(88)
# surLePlateau(59)



class piece():
    def __init__ (self, couleur, typePiece, position):
        self.couleur = couleur #'requete sql' #blanc ou noir
        self.typePiece= typePiece  # king queen fou cavalier tour pion
        self.position= position # coordonnées
        self.enjeu=True #enjeu ou pas (pris)
        self.moved=False # a bougé (True) ou non (False)
        self.controle=[] #liste des cases sur laquelle la pièce peut se déplacer ou prendre une pièce
        self.echec=False #pour le roi 
    def mouvement(arrivee):
        # TODO : vérifier que le mouvement appartient à la liste de self.controle
        if arrivee in self.controle:
            self.position=arrivee 
            self.moved=True # on change l'état du moved pour marquer que la pièce a bougé (pour le roc ou le pion)
    def casescontrolees():
        pass
    
# J'ai besoin que tous les objets pièces soient dans une liste liste_pieces
# pour pouvoir faire une liste des positions liste_positions
# pour ensuite tester ces positions dans les mouvements


# w=piece('noir','pion',56)
# liste_pieces.append(v)
# liste_pieces.append(w)
# for i in liste_pieces:
#     liste_positions.append(i.position)
#     if i.couleur=="blanc":
#         liste_positions_blanche.append(i.position)
#     else:
#         liste_positions_noire.append(i.position)
# print(v)
# print(liste_positions)
# print(liste_positions_blanche)
# print(liste_positions_noire)

#essai de programmation des mouvements
#ou plutôt des cases valides pour un déplacement

# def casescontrolees():
#     #si la pièce est un pion
#     if self.typePiece=="pion":
#         #le pion ne peux qu'avancer tout droit
#         #ou prendre en biais
#         #en fonction de sa couleur : vers le haut pour les blancs, vers le bas pour les noirs
#         if self.couleur=="blanc":
#             colonne=self.position[0]
#             ligne=self.position[1]
#             #case devant
#             if (colonne,ligne+1) not in liste_positions:
#                 self.casescontrolees.append((colonne,ligne+1))
#             #case avant gauche
#             #Si on est pas sur le bord gauche, on regarde la case avant gauche,
#             #si elle n'est pas occupée par une pièce de notre couleur
#             coordtemp = (liste_colonnes[index(colonne)-1],liste_lignes[index(ligne)+1])
#             if colonne!="A" and temp in liste_positions_noire:
#                 self.casescontrolees.append((coordtemp))
#             #case avant droite
#             coordtemp = (liste_colonnes[index(colonne)+1],liste_lignes[index(ligne)+1])
#             if colonne!="H" and temp in liste_positions_noire:
#                 self.casescontrolees.append((coordtemp))
#             # 2 cases devant pour le premier mouvement du pion
#             if self.moved==False:
#                 coordtemp = (liste_colonnes[index(colonne)],liste_lignes[index(ligne)+2])
#                 if coordtemp not in liste_positions:
#                     self.casescontrolees.append(coordtemp)
#         if self.couleur=="noir":
#             colonne=self.position[0]
#             ligne=self.position[1]
#             #case devant
#             if (colonne,ligne-1) not in liste_positions:
#                 self.casescontrolees.append((colonne,ligne-1))
#             #case avant gauche
#             #Si on est pas sur le bord gauche, on regarde la case avant gauche,
#             #si elle n'est pas occupée par une pièce de notre couleur
#             if colonne!="A" and temp in liste_positions_blanche:
#                 coordtemp = (liste_colonnes[index(colonne)-1],liste_lignes[index(ligne)-1])
#                 self.casescontrolees.append((coordtemp))
#             #case avant gauche
#             if colonne!="H" and temp in liste_positions_blanche:
#                 coordtemp = (liste_colonnes[index(colonne)+1],liste_lignes[index(ligne)-1])
#                 self.casescontrolees.append((coordtemp))
#             # 2 cases devant pour le premier mouvement du pion
#             if self.moved==False:
#                 coordtemp = (liste_colonnes[index(colonne)],liste_lignes[index(ligne)-2])
#                 if coordtemp not in liste_positions:
#                     self.casescontrolees.append(coordtemp)


# valeur de départ
# valeur d'arrivée

#v=piece('blanc','pion',11)


#mvt du pion
def mvtPion(pieceActive):
    patern=[]
    if pieceActive.couleur=='blanc':
        patern.append(pieceActive.position+1)
        patern.append(pieceActive.position+11)
        patern.append(pieceActive.position+9)
        if pieceActive.moved==False:
            patern.append(pieceActive.position+2)
    if pieceActive.couleur=='noir':
        patern.append(pieceActive.position-1)
        patern.append(pieceActive.position-11)
        patern.append(pieceActive.position-9)
        if pieceActive.moved==False:
            patern.append(pieceActive-2)
    patern.sort()
    return patern

#mvt de la tour
def mvtTour(pieceActive):
    patern=[]
    for i in -7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7:
        patern.append(pieceActive.position+10*i)
        patern.append(pieceActive.position+1*i)
    patern.sort()
    return patern
#mvt du fou
def mvtFou(pieceActive):
    patern=[]
    for i in -7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7:
        patern.append(pieceActive.position+11*i)
        patern.append(pieceActive.position+9*i)
    patern.sort()
    return patern
#mvt de la reine
def mvtQueen(pieceActive):
    patern=[]
    for i in -7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7:
        patern.append(pieceActive.position+11*i)
        patern.append(pieceActive.position+9*i)
        patern.append(pieceActive.position+10*i)
        patern.append(pieceActive.position+1*i)
    patern.sort()
    return patern
#mvt du cavalier
def mvtCavalier(pieceActive):
    patern=[]
    for i in -21,-19,-12,-8,8,12,19,21:
        patern.append(pieceActive.position+i)
    patern.sort()
    return patern
#mvt du roi
def mvtKing(pieceActive):
    patern=[]
    for i in -1,1:
        patern.append(pieceActive.position+11*i)
        patern.append(pieceActive.position+9*i)
        patern.append(pieceActive.position+10*i)
        patern.append(pieceActive.position+1*i)
    patern.sort()
    return patern

#la fonction mvt calcule les trajectoires de la pièce
def mvt(pieceActive):
    if active.typePiece=='pion':
        # print (mvtPion(pieceActive))
        return mvtPion(pieceActive)
    if active.typePiece=='tour':
        # print (mvtTour(pieceActive))
        return mvtTour(pieceActive)
    if active.typePiece=='fou':
        # print (mvtFou(pieceActive))
        return mvtFou(pieceActive)
    if active.typePiece=='queen':
        # print (mvtQueen(pieceActive))
        return mvtQueen(pieceActive)
    if active.typePiece=='king':
        #print (mvtKing(pieceActive))
        return mvtKing(pieceActive)
    if active.typePiece=='cavalier':
        #print (mvtCavalier(pieceActive))
        return mvtCavalier(pieceActive)

#check mouvement vérifie que la caseArrivee est sur les trajectoire de la pièce
def checkmvt(pieceActive, caseArrivee):
    if caseArrivee in mvt(pieceActive):
        print ("mouvement correct")
        return True
    else:
        print("mouvement interdit")
        return False


#la fonction chemin donne le chemin le plus direct pour aller à la destination
def leChemin(pieceActive, caseArrivee):
    if not checkmvt(pieceActive,caseArrivee):
        return False
    if pieceActive.typePiece=='king' or pieceActive.typePiece=='cavalier':
        print("pas d'obstacle pour le roi ou le cavalier")
        chemin=[]
        return chemin
    difference=abs(pieceActive.position-caseArrivee)
    print(difference)
    for i in 11,10,9:
        if difference%i==0:
            quotient=i
            print (quotient)
    if difference%11==0 or difference%10==0 or difference%9==0:
        pass
    else:
        quotient=1
    #     else:
    #         quotient=1
    #         print(quotient)
    # droite=[]
    # for i in mvt(pieceActive):
    #     if i%quotient==0:
    #         droite.append(i)
    chemin=[]
    # if pieceActive.position < caseArrivee:
    #     for i in droite:
    #         if i > pieceActive.position:
    #             chemin.append(i)
    #     chemin.sort()
    # else:
    #     for i in droite:
    #         if i<pieceActive.position:
    #             chemin.append(i)
    #     chemin.sort(reverse=True)
    if pieceActive.position < caseArrivee:
        temp=0
        i=1
        while temp!=caseArrivee:
            temp=pieceActive.position+i*quotient
            chemin.append(temp)
            i+=1
            print(temp)
        chemin.sort()
    if pieceActive.position > caseArrivee:
        temp=0
        i=1
        while temp!=caseArrivee:
            temp=pieceActive.position-i*quotient
            chemin.append(temp)
            i+=1
            print(temp)
        chemin.sort(reverse=True)
    #on sort la desitination de la liste
    chemin.pop()
    print(chemin)
    return chemin

#la maintenant on va taper dans la bdd
# pour vérifier les positions du chemin et vérifier qu'il n'y a rien sur le chemin
#def verifObstacle(pieceActive, caseArrivee):



active=piece('blanc','fou',22)
# mvt(active)
# checkmvt(active, 55)
leChemin(active,31)


"""
Je vais créer des modules pour les mouvements de base (les 8 directions cardinales)
pour faire des tests dans les mouvements des différentes pièces
En gros : 
1. on regarde la couleur de la pièce (self.couleur)
2. dans les directions du déplacement de la pièce, on regarde si la case est libre 
ou occupée par une pièce adverse (d'une autre couleur voir 
liste_positions_noire et liste_positions_blanc)
Alors on enregistre la case dans les lignes controlées
3. On continue dans les directions
4. si on atteint un bord ou une pièce de notre couleur, on arrête
5. la liste des cases controlées permet de savoir si les déplacements demandés sont légaux ou pas.
de voir si le roi est en échec
si le roi a le droit de bouger dans une case...

"""
