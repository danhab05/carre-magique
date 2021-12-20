class CarreMagique:
    def __init__(self, carre):
        self.carre = carre
        
    def somme_ligne_equal(self):
        sum_list = []
        for i in self.carre:
            sum = 0
            for el in i:
                sum += el
            sum_list.append(sum)
        if sum_list.count(sum_list[0]) == 3:
            return True
        else:
            return False

    def somme_colonne_equal(self):
        sum_list = []
        for i in range(len(self.carre)):
            sum = 0
            for el in self.carre:
                sum += el[i]
            sum_list.append(sum)

        if sum_list.count(sum_list[0]) == 3:
            return True
        else:
            return False

    def somme_diagonale_equal(self):
        sum_list = []
        sum1, sum2 = 0, 0
        for f, b in zip(range(len(self.carre)), range(len(self.carre)-1,-1,-1)):
            sum1 += self.carre[b][f]
            sum2 += self.carre[f][f]

        sum_list.append(sum1)
        sum_list.append(sum2)
        
        if sum_list.count(sum_list[0]) == 2:
            return True
        else:
            return False

    def verif_all(self):
        if self.somme_ligne() and self.somme_colonne() and self.somme_diagonale():
            return "Le carré est magique !"
        else:
            return "Le carré n'est pas magique !"

carre = [
    [4,9,2],
    [3,5,7],
    [8,1,6],
]
print(CarreMagique(carre).verif_all())
