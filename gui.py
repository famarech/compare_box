from tkinter import *
import tkinter.filedialog



class Trio:

    def __init__(self, name, position, frame):
        self.name = name
        self.position = position
        self.frame = frame
        self.var = ''
        # self.path = ''

    def afficher(self):
        intitule = Label(self.frame, text=self.name)
        saisie = Entry(self.frame, textvariable=self.var)
        btn = Button(self.frame, text="Rechercher", command=Trio.explorateur)

        intitule.grid(row=self.position, column=0)
        saisie.grid(row=self.position, column=1)
        btn.grid(row=self.position, column=3)

    def explorateur():
        path = tkinter.filedialog.askopenfilename()
        self.var = StringVar().set(path)



fenetre = Tk()
fenetre.geometry('400x200')
fenetre.title("CompareBox V1.0")







# trio("Chemin du chantier", 0, fenetre)
# trio("Chemin de la ligne", 1, fenetre)
# trio("Chemin du resultat", 2, fenetre)

un = Trio("Chemin du chantier", 0, fenetre)
un.afficher()
deux = Trio("Chemin de la ligne", 1, fenetre)
deux.afficher()


fenetre.mainloop()


