from tkinter import *
import tkinter.filedialog



class Trio:

    def __init__(self, name, position, frame):
        self.name = name
        self.position = position
        self.frame = frame
        self.var = StringVar()
        self.path = ''

    def afficher(self):
        intitule = Label(self.frame, text=self.name)
        saisie = Entry(self.frame, textvariable=self.var)
        btn = Button(self.frame, text="Rechercher", command=Trio.explorateur)

        intitule.grid(row=self.position, column=0)
        saisie.grid(row=self.position, column=1)
        btn.grid(row=self.position, column=3)

    def explorateur():
        path = tkinter.filedialog.askopenfilename()
        self.var.set(path)
        # chemin = path.replace("/", "\\\\")

# def explorateur():
#     path = tkinter.filedialog.askopenfilename()
#     path_walls_var.set(path)
#     chemin = path.replace("/", "\\\\")



fenetre = Tk()
fenetre.geometry('400x200')
fenetre.title("CompareBox V1.0")






# def trio(name, position, frame):
#     path = Label(frame, text=name)
#     path_var = StringVar()
#     # # path_walls_var.trace("w", create_auto)
#     saisie_path = Entry(frame, textvariable=path_var)
#     btn_path = Button(frame, text="Rechercher", command=explorateur)
#
#
#
#     path.grid(row=position, column=0)
#     saisie_path.grid(row=position, column=1)
#     btn_path.grid(row=position, column=3)

# trio("Chemin du chantier", 0, fenetre)
# trio("Chemin de la ligne", 1, fenetre)
# trio("Chemin du resultat", 2, fenetre)

un = Trio("Chemin du chantier", 0, fenetre)
un.afficher()


fenetre.mainloop()


