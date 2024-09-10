class CompteBancaire(object):
    def __init__(self, nom='Dupont', solde=1000):
        self.nom, self.solde = nom, solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print("Le solde du compte bancaire de {} est de {} dollars.".format(self.nom, self.solde))


class CompteEpargne(CompteBancaire):
    def __init__(self, nom='Durand', solde=500):
        super().__init__(nom, solde)  
        self.taux = 0.3

    def changeTaux(self, taux):
        self.taux = taux

    def capitalisation(self, nombreMois=6):
        print("Capitalisation {} mois au taux mensuel de {}%".format(nombreMois, self.taux))
        for m in range(nombreMois):
            self.solde = self.solde * (100 + self.taux) / 100

compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()

c1.capitalisation(12)

c1.affiche()

c1.changeTaux(.5)
c1.capitalisation(12)

c1.affiche()


