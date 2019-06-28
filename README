# JEUX D'ECHEC .py

#### Liste des fichiers utils

##### Serveur Python
* /echec.py/Serveur/server.py


##### Page de connxion / création de compte
* /echec.py/Serveur/cgi-bin/index.py
* /echec.py/Serveur/cgi-bin/result.py
* /echec.py/Serveur/cgi-bin/action_page.py
* /echec
.py/Serveur/stylesheet.css

##### fichier de déplacement des pièces
* /echec.py/main_echecs_v2.py

##### DUMP BDD
* /echec.py/dump_jeux
* /echec.py/schema_bddd.pdf
* user UNIX : echec / MDP "echec"
* role : echec / mdp "echec"
_______________________________
* pg_hba.conf :
* \# Database administrative login by Unix domain socket
* local   all             postgres                                trust
* local	jeuxechec	echec					trust



__________________________________

##### Page de cnx et création de compte en détail :
* index.py > html et regex // champ de formulaire
* result.py > récupère les informations du formulaire, requettes à la bdd, 6 msg d'erreurs ou de validation.
* action_page > récupère les information de login validé de result.py, affiche un bouton pour lancer le plateau, lance et positionne les pièces sur le plateau


##### Modules python utilisés
* import cgi
* import psycopg2
* import bcrypt
* from tkinter import *
* from random import randrange
* import re

