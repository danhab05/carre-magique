carre = [
    [4,9,2],
    [3,5,7],
    [8,1,6],
]

def somme_ligne(carre):
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

def somme_colonne(carre):
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

def somme_diagonale(carre):
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

def str_list_to_int_list(str_list):
    int_list = [int(n) for n in str_list]
    return int_list       

l1 = input("Entrez la premiere ligne du carré séparé par des virgules et sans espaces: ")
l2 = input("Entrez la deuxieme ligne du carré séparé par des virgules et sans espaces: ")
l3 = input("Entrez la troisieme ligne du carré séparé par des virgules et sans espaces: ")


carre = [str_list_to_int_list(l1.split(",")), str_list_to_int_list(l2.split(",")),str_list_to_int_list(l3.split(",")),]
if somme_ligne(carre) and somme_colonne(carre) and somme_diagonale(carre):
    print("Le carré est magique !")
else:
    print("Le carré n'est pas magique !")