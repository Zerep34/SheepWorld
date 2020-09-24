import numpy as np
from random import random
from random import randint

class Monde:

    def __init__(self, dimension, duree_repousse = 30):
        if dimension < 50:
            self.dimension = 50
        else :
            self.dimension = dimension

        self.duree_repousse = duree_repousse
        self.carte = np.random.randint(self.duree_repousse, 100, size=(self.dimension,self.dimension))

        numberOfWithoutGrass = (self.dimension * self.dimension) / 2
        while numberOfWithoutGrass > 0:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if random() > 0.5 and numberOfWithoutGrass >= 0:
                        self.carte[i][j] = randint(0, duree_repousse)
                        numberOfWithoutGrass = numberOfWithoutGrass - 1


    def herbePousse(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.carte[i][j] = self.carte[i][j] + 1

    def herbeMange(self, i, j):
        if self.carte[i][j] >= self.duree_repousse:
            self.carte[i][j] = 0

    def nbHerbe(self):
        count = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.carte[i][j] >= self.duree_repousse :
                    count += 1
        return count

    def getCoefCarte(self, i, j):
        return self.carte[i][j]

    def getCarte(self):
        return self.carte

    def getDimension(self):
        return self.dimension

    def getDureeRepousse(self):
        return self.duree_repousse

    def afficheMap(self):
        print(self.carte)

    def numberUnderZero(self):
        count = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.carte[i][j] <= self.duree_repousse:
                    count += 1
        print(count)

monde = Monde(50)
monde.afficheMap()
monde.herbePousse()
monde.afficheMap()
monde.numberUnderZero()

