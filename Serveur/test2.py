from tkinter import *
from random import randrange
import re


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

liste = [[1,'blanc',11,'tourb1','tour'],
[2,'blanc',21,'cavalierb1','cavalier'],
[3,'blanc',31,'foub1','fou'],
[4,'blanc',41,'reineb','queen'],
[5,'blanc',51,'roib','king'],
[6,'blanc',61,'foub2','fou'],
[7,'blanc',71,'cavalierb2','cavalier'],
[8,'blanc',81,'tourb2','tour'],
[9,'blanc',12,'pionb1','pion'],
[10,'blanc',22,'pionb2','pion'],
[11,'blanc',32,'pionb3','pion'],
[12,'blanc',42,'pionb4','pion'],
[13,'blanc',52,'pionb5','pion'],
[14,'blanc',62,'pionb6','pion'],
[15,'blanc',72,'pionb7','pion'],
[16,'blanc',82,'pionb8','pion'],
[17,'noir',18,'tourn1','tour'],
[18,'noir',28,'cavaliern1','cavalier'],
[19,'noir',38,'foun1','fou'],
[20,'noir',48,'reinen','queen'],
[21,'noir',58,'roin','king'],
[22,'noir',68,'foun2','fou'],
[23,'noir',78,'cavaliern2','cavalier'],
[24,'noir',88,'tourn2','tour'],
[25,'noir',17,'pionn1','pion'],
[26,'noir',27,'pionn2','pion'],
[27,'noir',37,'pionn3','pion'],
[28,'noir',47,'pionn4','pion'],
[29,'noir',57,'pionn5','pion'],
[30,'noir',67,'pionn6','pion'],
[31,'noir',77,'pionn7','pion'],
[32,'noir',87,'pionn8','pion']]


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
