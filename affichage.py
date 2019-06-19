from tkinter import *
import tkinter.messagebox


def Fermer():
    Canevas.delete(ALL)
    Mafenetre.title("Image")


def Apropos():
    tkinter.messagebox.showinfo("A propos", " jeu d'echec V1.0")


def ligneDamier(x, y1, y2):
    coord = [
        [0, y1],
        [x * 2, y1],
        [x * 4, y1],
        [x * 6, y1],
        [x, y2],
        [x * 3, y2],
        [x * 5, y2],
        [x * 7, y2],
    ]

    coul = "black"
    i = 0

    while i < len(coord):
        can.create_rectangle(
            coord[i][0],
            coord[i][1],
            coord[i][0] + x,
            coord[i][1] + x,
            width=2,
            fill=coul,
        )
        i += 1


def damier(x):
    y1 = 0
    y2 = x
    b = y2

    while y1 <= int(7 * b) and y2 <= int(8 * b):
        ligneDamier(x, y1, y2)
        y1 = y1 + (x * 2)
        y2 = y2 + (x * 2)


x = 100


# Construction de la fenêtre principale «root»
root = Tk()
root.title("EchecPorn")
root.geometry("750x450+350+150")
root.configure(bg="light grey")
# Construction d'un simple bouton
qb = Button(root, text="Quitter", command=root.quit)

# Menu deroulant :

menubarre = Menu(root)
menufichier = Menu(menubarre, tearoff=0)
menufichier.add_command(label="Ouvrir une image")
menufichier.add_command(label="Fermer l'image", command=Fermer)
menufichier.add_command(label="Quitter", command=root.destroy)
menubarre.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubarre, tearoff=0)
menuaide.add_command(label="A propos", command=Apropos)
menubarre.add_cascade(label="Aide", menu=menuaide)


can = Canvas(root, width=x * 8, height=x * 8, bg="white")

can.pack(side=TOP, padx=5, pady=5)
b1 = Button(root, command=damier(x))
b1.pack(side=RIGHT, padx=3, pady=3)

# Affichage du menu
root.config(menu=menubarre)
qb.pack()

# Lancement de la «boucle principale»
root.mainloop()
