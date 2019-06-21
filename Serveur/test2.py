from tkinter import *
from random import randrange


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
can0.pack()

caseNoir = PhotoImage(file="img/noir.png")
caseBlanche = PhotoImage(file="img/blanc.png")
pionNoir = PhotoImage(file="img/Chess_pdt60.png")
pionBlanche = PhotoImage(file="img/Chess_plt60.png")
tourNoir = PhotoImage(file="img/Chess_rdt60.png")
tourBlanche = PhotoImage(file="img/Chess_rlt60.png")
cavalierNoir = PhotoImage(file="img/Chess_ndt60.png")
cavalierBlanc = PhotoImage(file="img/Chess_nlt60.png")
fouBlanc = PhotoImage(file="img/Chess_bdt60.png")
fouNoir = PhotoImage(file="img/Chess_blt60.png")
reineNoir = PhotoImage(file="img/Chess_qdt60.png")
reineBlanche = PhotoImage(file="img/Chess_qlt60.png")
roiNoir = PhotoImage(file="img/Chess_kdt60.png")
roiBlanc = PhotoImage(file="img/Chess_klt60.png")

for ligne in range(NB_LINES):
    for col in range(NB_COLS):
        centre = (X0+col*SIDE, Y0+ligne*SIDE)
        if (centre[0] + centre[1]) % 2 == 0:
            can0.create_image(centre, image=caseBlanche)
        else:
            can0.create_image(centre, image=caseNoir)

for ligne in range(NB_LINES):
    for col in range(NB_COLS):
        centre = (X0+col*SIDE, Y0+ligne*SIDE)
        if col == 2 and ligne == 6:
            can0.create_image(centre, image=pionNoir)
        else:
            can0.create_image(centre, image=tourNoir)
FenPrincpale.mainloop()
