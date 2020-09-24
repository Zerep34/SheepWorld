from Monde import Monde
from Mouton import Mouton
from Loup import Loup
from random import randint


class Simulation:

    def __init__(self, nombre_moutons, maxMoutons, nombre_loups,fin_du_monde):
        self.nombre_moutons = nombre_moutons
        self.nombre_loups = nombre_loups
        self.horloge = 0
        self.maxMoutons = maxMoutons
        self.fin_du_monde = fin_du_monde
        self.moutons = []
        self.loups = []

        # Génération des Loups
        for i in range(self.nombre_loups):
            self.loups.append(Loup((randint(0, 49), randint(0, 49))))

        # Génération des moutons
        for i in range(self.nombre_moutons):
            self.moutons.append(Mouton((randint(0, 49), randint(0, 49))))

        self.monde = Monde(50)
        self.resultats_herbe = []
        self.resultats_moutons = []
        self.resultats_loups = []

    def simMouton(self):
        while 0 < len(self.moutons) <= self.maxMoutons and self.horloge < self.fin_du_monde:
            print(self.monde.nbHerbe())
            self.horloge += 1
            self.monde.herbePousse()
            self.variationEnergie()
            self.reproduction()

            # Déplacement des moutons et Mange herbe
            for tempMouton in self.moutons:
                tempMouton.deplacement(self.monde.dimension)
                self.monde.nbHerbe()
                self.monde.herbeMange(tempMouton.position[0], tempMouton.position[1])
                self.monde.nbHerbe()


            # Déplacement des loups et mange moutons
            for tempLoup in self.loups:
                tempLoup.deplacement(self.monde.dimension)
                self.eatSheep(tempLoup.position[0], tempLoup.position[1], self.moutons)

            # Sauvegarde des cases herbus
            self.resultats_herbe.append(self.monde.nbHerbe())

            # Sauvegarde du nb Moutons
            self.resultats_moutons.append(len(self.moutons))

            # Sauvegarde du nb Loups
            self.resultats_loups.append(len(self.loups))

        print(self.resultats_moutons)
        print(self.resultats_loups)
        print(self.horloge)


    def variationEnergie(self):
        listePositionDoneMouton = []
        for tempMouton in self.moutons:
            if self.monde.carte[tempMouton.position[0]][tempMouton.position[1]] < self.monde.duree_repousse:
                tempMouton.energie -= 1
            elif tempMouton.energie == 0:
                self.moutons.remove(tempMouton)
            elif tempMouton.position not in listePositionDoneMouton:
                tempMouton.energie += tempMouton.gain_nourriture
                listePositionDoneMouton.append(tempMouton.position)
        listePositionDoneLoup = []
        for tempLoup in self.loups:
            if tempLoup.energie == 0:
                self.loups.remove(tempLoup)
            elif tempLoup.position not in listePositionDoneLoup:
                tempLoup.energie += tempLoup.gain_nourriture
                listePositionDoneLoup.append(tempLoup.position)

    def reproduction(self):
        # Reproduction Mouton
        tempListMouton = []
        for tempMouton in self.moutons:
            aleaMouton = randint(1, 100)
            if aleaMouton < tempMouton.taux_reproduction:
                tempListMouton.append(Mouton(tempMouton.position))
        self.moutons = self.moutons + tempListMouton

        # Reproduction Loup
        tempListLoup = []
        for tempLoup in self.moutons:
            aleaLoup = randint(1, 100)
            if aleaLoup < tempLoup.taux_reproduction:
                tempListLoup.append(Loup(tempLoup.position))
        self.loups = self.loups + tempListLoup

    def eatSheep(self, i, j, listeMoutons):
        for sheep in listeMoutons:
            if sheep.position == (i, j):
                listeMoutons.remove(sheep)
                break

s = Simulation(50, 1000, 10, 100)
s.simMouton()