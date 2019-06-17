from tkinter import *
from random import randrange


PICT_SIZE = 100
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

caseNoir = PhotoImage(file=r"img\noir.png")
caseBlanche = PhotoImage(file=r"img\blanc.png")

for ligne in range(NB_LINES):
    for col in range(NB_COLS):
        centre = (X0+col*SIDE, Y0+ligne*SIDE)
        if (centre[0] + centre[1]) % 2 == 0:
            can0.create_image(centre, image=caseBlanche)
        else:
            can0.create_image(centre, image=caseNoir)

FenPrincpale.mainloop()