from Monde import Monde


class Simulation:

    def __init__(self, nombre_moutons, fin_du_monde):
        self.nombre_moutons = nombre_moutons
        self.horloge = 0
        self.fin_du_monde = fin_du_monde
        self.moutons = []
        self.monde = Monde(50)
        self.resultats_herbe = []
        self.resultats_moutons = []

    def simMouton(self):
        self.horloge += 1
        self.monde.herbePousse()