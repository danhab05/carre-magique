class CarreMagique:
    def __init__(self, carre):
        self.carre = carre

        
    def somme_ligne(self, carre):
        s = []
        for i in carre:
            sum = 0
            for el in i:
                sum += el
            s.append(sum)
        if s.count(s[0]) == 3:
            return True
        else:
            return False

    def somme_colonne(self, carre):
        s = []
        for i in range(len(carre)):
            sum = 0
            for el in carre:
                sum += el[i]
            s.append(sum)

        if s.count(s[0]) == 3:
            return True
        else:
            return False

    def somme_diagonale(self, carre):
        s = []
        sum1 = 0
        sum2 = 0
        for f, b in zip(range(len(carre)), range(len(carre)-1,-1,-1)):
            sum1 += carre[b][f]
            sum2 += carre[f][f]

        s.append(sum1)
        s.append(sum2)
        if s.count(s[0]) == 2:
            return True
        else:
            return False


carre = [
    [4,9,2],
    [3,5,7],
    [8,1,6],
]
verif = CarreMagique(carre)


if verif.somme_ligne(carre) and verif.somme_colonne(carre) and verif.somme_diagonale(carre):
    print("Le carré est magique !")
else:
    print("Le carré n'est pas magique !")