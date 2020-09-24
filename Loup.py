from random import randint

class Loup:

    def __init__(self, position, taux_reproduction=5, gain_nourriture=19):
        self.position = position
        self.gain_nourriture = gain_nourriture
        self.energie = randint(1, 2) * self.gain_nourriture
        self.taux_reproduction = taux_reproduction

    def deplacement(self, dimension):
        randI = randint(self.position[0] - 1, self.position[0] + 1)
        randJ = randint(self.position[1] - 1, self.position[1] + 1)
        if randI == dimension or randJ == dimension:
            randI = (randI + 1) % dimension
            randJ = (randJ + 1) % dimension
        elif randI == -1 or randJ == -1:
            if randI == -1:
                randI = (randI - 1 + dimension) % dimension
            if randJ == -1:
                randJ = (randJ - 1 + dimension) % dimension
        return (randI, randJ)

    def setPosition(self, i, j):
        self.position = (i, j)
