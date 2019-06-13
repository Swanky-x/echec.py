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

class piece():
    def __init__ (self, couleur, typePiece, position):
        self.couleur = couleur #blanc ou noir
        self.typePiece= typePiece  # king queen bishop cavalier tour pion
        self.position= position # coordonnées
        self.enjeu=True #enjeu ou pas (pris)
        self.moved=False # a bougé (True) ou non (False)
    def mouvement(arrivee):
        self.position=arrivee 
        self.moved=True #on change l'état du moved pour marquer que la pièce a bougé (pour le roc)

#J'ai besoin que tous les objets pièces soient dans une liste liste_pieces
# pour pouvoir faire une liste des positions liste_positions
#pour ensuite tester ces positions dans les mouvements

for i in liste_pieces:
    liste_positions.append(i.position)

