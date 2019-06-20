import tkinter as tk


















TITLE_FONT = ("Helvetica", 22, "bold")
BUTTON_FONT = ("Helvetica", 18)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FenMenuPrincipal, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            print(frame)

            frame.grid(row=0, column=0, sticky="nsew", pady=100)


        self.show_frame("FenMenuPrincipal")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class FenMenuPrincipal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bienvenue sur EchecTest", font=TITLE_FONT)
        label.pack(side="top", fill="both", pady=25)
        frame1 = tk.Frame(self)

        button1 = tk.Button(frame1, text="Login",
                            command=lambda: controller.show_frame("PageOne"),
                            font=BUTTON_FONT,
                            pady=15)
        button2 = tk.Button(frame1, text="Création de compte",
                            command=lambda: controller.show_frame("PageTwo"),
                            font=BUTTON_FONT)
        button3 = tk.Button(self, text="Quitter",
                            command=exit,
                            font=BUTTON_FONT)
        button1.pack()
        button2.pack()
        frame1.pack()
        button3.pack(side="bottom")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        x = 50
        tk.Frame.__init__(self, parent)
        frame1 = tk.Frame(self)
        label = tk.Label(frame1, text="Menu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        can = tk.Canvas(frame1, width=x * 8, height=x * 8, bg="white")

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

        damier(x)
        frame1.pack()
        can.pack(side="top", padx=5, pady=5)
        b1 = tk.Button(self, command=exit)
        b1.pack(side="bottom")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Retour au menu principal",
                           command=lambda: controller.show_frame("FenMenuPrincipal"))
        button.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Retour au menu principal",
                           command=lambda: controller.show_frame("FenMenuPrincipal"))
        button.pack()

if __name__ == "__main__":
    fenPrincipal = SampleApp()
    # ? Creation de la fenetre principal
    # titre de la fenetre
    fenPrincipal.title("EchecTest")
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


    # ** permet le maintient de l'affichage
    fenPrincipal.mainloop()