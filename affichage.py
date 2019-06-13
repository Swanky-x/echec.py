from tkinter import *

# Construction de la fenêtre principale «root»
root = Tk()
root.title('EchecPorn')
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=root.quit)

# Placement du bouton dans «root»
qb.pack()

# Lancement de la «boucle principale»
root.mainloop()