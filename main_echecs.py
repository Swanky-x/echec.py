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
            /          \
           / "fou A3"    \ "fou A3"
    player1              player2       ----> *affiche le fou en A3*

     ----------------------->

-logs

[ A suivre ]

-tableaux des derniers match sur index.html
-systeme de sauvegarde de partie coté serveur
-a vous de trouver
"""

liste_pieces=[]
liste_positions=[]
liste_positions_noire=[]
liste_positions_blanche=[]
liste_colonnes=("A","B","C","D","E","F","G","H")
liste_lignes=(1,2,3,4,5,6,7,8)
class piece():
    def __init__ (self, couleur, typePiece, position):
        self.couleur = couleur #blanc ou noir
        self.typePiece= typePiece  # king queen bishop cavalier tour pion
        self.position= position # coordonnées
        self.enjeu=True #enjeu ou pas (pris)
        self.moved=False # a bougé (True) ou non (False)
        self.controle=[] #liste des cases sur laquelle la pièce peut se déplacer ou prendre une pièce
    def mouvement(arrivee):
        self.position=arrivee 
        self.moved=True #on change l'état du moved pour marquer que la pièce a bougé (pour le roc)
    def casescontrolees():
        pass
    
# J'ai besoin que tous les objets pièces soient dans une liste liste_pieces
# pour pouvoir faire une liste des positions liste_positions
# pour ensuite tester ces positions dans les mouvements


for i in liste_pieces:
    liste_positions.append(i.position)
    if i.couleur=="blanc":
        liste_positions_blanche.append(i.position)
    else:
        liste_positions_noire.append(i.position)


#essai de programmation des mouvements

def casescontrolees():
    if self.typePiece=="pion":
        #le pion ne peux qu'avancer tout droit
        #ou prendre en biais
        #en fonction de sa couleur : vers le haut pour les blancs, vers le bas pour les noirs
        if self.couleur=="blanc":
            colonne=self.position[0]
            ligne=self.position[1]
            #case devant
            if (colonne,ligne+1) not in liste_positions:
                self.casescontrolees.append((colonne,ligne+1))
            #case avant gauche
            if colonne!="A" and 
            #case avant droite



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
