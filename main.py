class CarreMagique:
    def __init__(self, carre):
        self.carre = carre

        
    def somme_ligne(self, ):
        s = []
        for i in self.carre:
            sum = 0
            for el in i:
                sum += el
            s.append(sum)
        if s.count(s[0]) == 3:
            return True
        else:
            return False

    def somme_colonne(self, ):
        s = []
        for i in range(len(self.carre)):
            sum = 0
            for el in self.carre:
                sum += el[i]
            s.append(sum)

        if s.count(s[0]) == 3:
            return True
        else:
            return False

    def somme_diagonale(self, ):
        s = []
        sum1 = 0
        sum2 = 0
        for f, b in zip(range(len(self.carre)), range(len(self.carre)-1,-1,-1)):
            sum1 += self.carre[b][f]
            sum2 += self.carre[f][f]

        s.append(sum1)
        s.append(sum2)
        if s.count(s[0]) == 2:
            return True
        else:
            return False
    def verifAll(self):
        if self.somme_ligne() and self.somme_colonne() and self.somme_diagonale():
            return True
        else:
            return False

carre = [
    [4,9,2],
    [3,5,7],
    [8,1,6],
]
verif = CarreMagique(carre)


if verif.verifAll():
    print("Le carré est magique !")
else:
    print("Le carré n'est pas magique !")