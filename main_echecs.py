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

class piece(self,couleur,type,position,etat,moved):
    def __init__ (self, couleur, type, position, etat, moved):
        