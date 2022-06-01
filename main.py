from ClassModules import Binome
from os.path import abspath
from time import localtime

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
            line = line.replace('/n', '')
            line = line.split(";")
            tab.append(line)
        del tab[0]
        return tab

    def resultat(self, ligne, path):
        t  = localtime()
        path += "/resultats" +\
                "_" + str(t.tm_mday) + "_" + str(t.tm_mon) + "_" + str(t.tm_year) +\
                "_" + str(t.tm_hour) + "_" + str(t.tm_min) + "_" + str(t.tm_sec) + ".txt"
        for wall in self.tab:
            for poste in ligne.tab:
                file_in = open(path, "a")
                b = Binome(wall, poste)
                print(b.compare_complet())
                file_in.write(b.compare_necessaire())
                file_in.close()







chaine_de_prod = abspath('./Ressources/Ligne_de_Prod/capacite_ligne.csv')
chantier = abspath('./liste_murs.csv')
resultat = abspath('./Ressources/Resultats/')

ligne = Liste(chaine_de_prod)
walls = Liste(chantier)

walls.resultat(ligne, resultat)