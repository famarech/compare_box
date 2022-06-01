from tkinter import *

class Cube:

    def __init__(self, name, x, y, z):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)




class Interval:

    def __init__(self, name, mif, min, max, maf):
        self.name = name
        self.mif = Interval.valeur(mif)
        self.min = Interval.valeur(min)
        self.max = Interval.valeur(max)
        self.maf = Interval.valeur(maf)

    def valeur(valeur):
        if valeur == '':
            return 0
        if isinstance(valeur, str) is True:
            return int(valeur)
        return valeur




class Binome:

    def __init__(self, wall, deck):
        self.wall = Cube(str(wall[0]), wall[1], wall[2], wall[3])
        self.deckname = deck[0]
        self.deckx = Interval('Longueur', deck[1], deck[2], deck[3], deck[4])
        self.decky = Interval('Hauteur', deck[5], deck[6], deck[7], deck[8])
        self.deckz = Interval('Epaisseur', deck[9], deck[10], deck[11], deck[12])

    def afficher(self):
        self.wall.afficher()
        print(f"Comparé avec le poste {self.deckname} :")
        self.deckx.afficher()
        self.decky.afficher()
        self.deckz.afficher()

    def compare(self):
        message = "Le mur n°" + self.wall.name + " sur le poste " + self.deckname + " est :\n"
        message += Binome.comp_one_size(self.wall.x, self.deckx) + " en " + self.deckx.name + "\n"
        message += Binome.comp_one_size(self.wall.y, self.decky) + " en " + self.decky.name + "\n"
        message += Binome.comp_one_size(self.wall.z, self.deckz) + " en " + self.deckz.name + "\n"
        return message

    def comp_one_size(size, dimension):
        if dimension.maf == 0:
            dimension.maf = size + 1
        if dimension.max == 0:
            dimension.max = size + 1
        message = ""
        if (size < dimension.mif or size > dimension.maf):
            message = "IMPOSSIBLE"
        elif (size >= dimension.min and size < dimension.max):
            message = "OK"
        else:
            message = "Possible"
        return message




class Liste:

    def __init__(self, path):
        self.path = path
        self.tab = Liste.tab(self)

    def tab(self):
        file_in = open(self.path, "r")
        str = file_in.readlines()
        file_in.close()
        tab = []
        for line in str:
            line = line.replace('\n', '')
            line = line.split(";")
            tab.append(line)
        del tab[0]
        return tab

    def resulter(self, ligne, path):
        for wall in self.tab:
            for poste in ligne.tab:
                file_in = open(path, "a")
                b = Binome(wall, poste)
                print(b.compare())
                file_in.write(b.compare())
                file_in.close()



general_path = 'G:/Reconversion Pro/00_formations/Formation Python appronfondie/Projet boite comparé/'
chaine_de_prod = general_path + 'capacité_ligne.csv'
chantier = general_path + 'liste_murs.csv'
resultat = general_path + 'resultat_possibilites_de_fabrication.txt'

ligne = Liste(chaine_de_prod)
walls = Liste(chantier)

walls.resulter(ligne, resultat)




























