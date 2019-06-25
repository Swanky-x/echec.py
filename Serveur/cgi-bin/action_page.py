#!/usr/bin/python3
#coding:UTF-8
import cgi
import psycopg2
from tkinter import *
from random import randrange
import re

import cgitb
cgitb.enable()

form = cgi.FieldStorage()
print("Content-Type: text/html")
print()

conn = psycopg2.connect (
    database = "jeuxechec",
    user = "echec",
    password = "echec",
    host = "127.0.0.1",
    port = "5432"
)


cursor = conn.cursor()
cursor.execute("SELECT id_piece, couleur, position, type, nom FROM pieces")
pions = cursor.fetchall()

liste = []
for i in pions :
    tmp = list(i)
    liste.append(tmp)

cursor.close()
conn.close()


##########################################################################


def pointeur(event=None):
    print(f"Click en X = {str((event.x // PICT_SIZE) + 1)}, Click en Y = {str((event.y // PICT_SIZE) + 1)}")
    coord = (f"{((event.x // SIDE) + 1)}{((event.y // SIDE) + 1)}")
    test.set(coord)
    kesako(test.get())
    return coord

def kesako(coord):
    for i in range(len(liste)):
        if int(coord) == liste[i][2]:
            print(liste[i][4])

def verifPiece(i,str):
    x = re.search(str, liste[i][3])
    if (x):
        return x.string


liste2 = []
for i in range(len(liste)):
    a = str(liste[i][2])
    liste2.append([a])

col2 = []
ligne2 = []

for i in liste2:
    for y in i:
        a = int(y[0])-1
        b = int(y[1])-1
        col2.append(a)
        ligne2.append(b)

# col2 = col2[::1]
# ligne2 = ligne2[::1]

PICT_SIZE = 66
PAD = 1
SIDE = PICT_SIZE + PAD

NB_LINES = 8
NB_COLS = 8
WIDTH = SIDE * NB_COLS
HEIGHT = SIDE * NB_LINES
X0 = Y0 = SIDE // 2

FenPrincpale = Tk()
can0 = Canvas(FenPrincpale, width=WIDTH, height=HEIGHT, background="black")
can0.bind("<Button-1>", pointeur)
can0.pack()

caseNoir = PhotoImage(file="img/noir.png")
caseBlanche = PhotoImage(file="img/blanc.png")
pionNoir = PhotoImage(file="img/Chess_pdt60.png")
pionBlanc = PhotoImage(file="img/Chess_plt60.png")
tourNoir = PhotoImage(file="img/Chess_rdt60.png")
tourBlanc = PhotoImage(file="img/Chess_rlt60.png")
cavalierNoir = PhotoImage(file="img/Chess_ndt60.png")
cavalierBlanc = PhotoImage(file="img/Chess_nlt60.png")
fouNoir = PhotoImage(file="img/Chess_bdt60.png")
fouBlanc = PhotoImage(file="img/Chess_blt60.png")
reineNoir = PhotoImage(file="img/Chess_qdt60.png")
reineBlanc = PhotoImage(file="img/Chess_qlt60.png")
roiNoir = PhotoImage(file="img/Chess_kdt60.png")
roiBlanc = PhotoImage(file="img/Chess_klt60.png")

for ligne in range(NB_LINES):
    for col in range(NB_COLS):
        centre = (X0+col*SIDE, Y0+ligne*SIDE)
        if (centre[0] + centre[1]) % 2 == 0:
            can0.create_image(centre, image=caseBlanche)
        else:
            can0.create_image(centre, image=caseNoir)


def placementPiece(liste) :
    ligne3 = 0
    while ligne3//4 <= 31 :
        #print(ligne3)
        for ligne in range(NB_LINES):
            # print(ligne2[ligne])
            for col in range(NB_COLS):
                centre = (X0+col*SIDE, Y0+ligne*SIDE)
                if col == (int(col2[col])) and ligne == (int(ligne2[ligne3//4])):
                    for i in range(len(liste)):
                        # ** piece noir
                        if liste[i][3] == verifPiece(i, "^cav(.)+n(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=cavalierNoir)
                        if liste[i][3] == verifPiece(i, "^tou(.)+n(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=tourNoir)
                        if liste[i][3] == verifPiece(i, "^fou(.)?n(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=fouNoir)
                        if liste[i][3] == verifPiece(i, "^ro(.)+n(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=roiNoir)
                        if liste[i][3] == verifPiece(i, "^re(.)+en(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=reineNoir)
                        if liste[i][3] == verifPiece(i, "^pi(.)+nn(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=pionNoir)
                        # ** Piece blanche
                        if liste[i][3] == verifPiece(i, "^cav(.)+b(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=cavalierBlanc)
                        if liste[i][3] == verifPiece(i, "^tou(.)+b(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=tourBlanc)
                        if liste[i][3] == verifPiece(i, "^fou(.)?b(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=fouBlanc)
                        if liste[i][3] == verifPiece(i, "^ro(.)+b(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=roiBlanc)
                        if liste[i][3] == verifPiece(i, "^re(.)+eb(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=reineBlanc)
                        if liste[i][3] == verifPiece(i, "^pi(.)+nb(.)?"):
                            if liste[i][2] == int(f"{(int(col2[col])+1)}{(int(ligne2[ligne3//4])+1)}"):
                                can0.create_image(centre, image=pionBlanc)

        ligne3 += 1


test = IntVar()
placementPiece(liste)


FenPrincpale.mainloop()