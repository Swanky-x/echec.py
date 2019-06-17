import tkinter as tk
from tkinter import messagebox

def test():

    mainframe = tk.Frame(fenPrincipal)
    btn = tk.Button(mainframe, text="blablabla")
    mainframe.pack()
    btn.pack()

def test2(a, b):
    a.tkraise()
    b


# ? Creation de la fenetre principal
# Creation de la fenetre
fenPrincipal = tk.Tk()
# titre de la fenetre
fenPrincipal.title("EchecPorn")
# taile mini
fenPrincipal.minsize(640, 480)
# ** taille d'affichage standard
# On recup la taille de l'ecran utilisateur
screen_x = int(fenPrincipal.winfo_screenwidth())
screen_y = int(fenPrincipal.winfo_screenheight())
# Taille de l'ecran voulu
fenPrincipalX = 800
fenPrincipalY = 600
# calcule pour centrer la fenetre
coordX = (screen_x // 2) - (fenPrincipalX // 2)
coordY = (screen_y // 2) - (fenPrincipalY // 2)

# Creation de la forme pour lafenetre
fenPrincipal.geometry(f"{fenPrincipalX}x{fenPrincipalY}+{coordX}+{coordY}")


# ! Frame 0
frame0 = tk.Frame(fenPrincipal)
btn0 = tk.Button(frame0, text="ok", command=test2(frame0, test()))
btn0.pack()
frame0.pack()













# ** permet le maintient de l'affichage
fenPrincipal.mainloop()
