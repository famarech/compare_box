from tkinter import *
import tkinter.ttk
import tkinter.filedialog
from os.path import abspath
from main import Liste

global var_ldp
global var_ldm
global var_res


def explorateur_ldp():
    path = tkinter.filedialog.askopenfilename()
    var_ldp.set(path)

def explorateur_ldm():
    path = tkinter.filedialog.askopenfilename()
    var_ldm.set(path)

def explorateur_res():
    path = tkinter.filedialog.askdirectory()
    var_res.set(path)

def lancer_resultat():
    # global var_ldp
    # global var_ldm
    # global var_res
    # ligne = Liste(var_ldp.get())
    # walls = Liste(var_ldm.get())
    # wal.resultat(lig, var_res.get())
    return 0


def gui():

    global var_ldp
    global var_ldm
    global var_res

    fenetre = Tk()
    fenetre.geometry('450x200')
    fenetre.title("CompareBox V1.0")

    layer = tkinter.ttk.Frame(fenetre)

    intitule_ldp = Label(layer, text="Fichier Ligne de production")
    var_ldp = StringVar()
    var_ldp.set(abspath('./Ressources/Ligne_de_Prod/capacite_ligne.csv'))
    saisie_ldp = Entry(layer, textvariable=var_ldp)
    btn_ldp = Button(layer, text="Rechercher", command=explorateur_ldp)
    intitule_ldp.grid(row=0, column=0)
    saisie_ldp.grid(row=0, column=1)
    btn_ldp.grid(row=0, column=2)

    intitule_ldm = Label(layer, text="Fichier Liste des murs")
    var_ldm = StringVar()
    saisie_ldm = Entry(layer, textvariable=var_ldm)
    btn_ldm = Button(layer, text="Rechercher", command=explorateur_ldm)
    intitule_ldm.grid(row=1, column=0)
    saisie_ldm.grid(row=1, column=1)
    btn_ldm.grid(row=1, column=2)

    intitule_res = Label(layer, text="Dossier pour le fichier resultat")
    var_res = StringVar()
    var_res.set(abspath('./Ressources/Resultats/'))
    saisie_res = Entry(layer, textvariable=var_res)
    btn_res = Button(layer, text="Rechercher", command=explorateur_res)
    intitule_res.grid(row=2, column=0)
    saisie_res.grid(row=2, column=1)
    btn_res.grid(row=2, column=2)

    btn_lancer = tkinter.Button(layer, text="Lancer le Resultat", command=lancer_resultat())
    btn_lancer.grid(row=3, column=1)

    layer.pack()

    fenetre.mainloop()

gui()