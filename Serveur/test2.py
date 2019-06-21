from tkinter import *
from random import randrange

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
