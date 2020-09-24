from random import randint

class Mouton:

    def __init__(self, , position,  taux_reproduction = 4, gain_nourriture = 4):
        self.position = position
        self.gain_nourriture = gain_nourriture
        self.energie = randint(1,2) * self.gain_nourriture
        self.taux_reproduction = randint(1, 100)

    def variationEnergie(self):
        return

    def deplacement(self):
        return

    def setPosition(self, i, j):
        return 