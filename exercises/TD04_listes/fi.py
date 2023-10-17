carre_mag = [
    [4, 14, 15, 1],
    [9, 7, 6, 12],
    [5, 11, 10, 8],
    [16, 2, 3, 13]
]

carre_pas_mag = [
    [4, 14, 15, 1],
    [9, 7, 6, 12],
    [5, 11, 10, 8],
    [16, 2, 7, 13]
]

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    print("_"*23)
    for i in range(4):
        ligne = "  ".join(str(x).zfill(2) for x in carre[i])
        print(f"|   {ligne}    |")
    print(""*20)


def testCarreMagique(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = 0
    diagonale_haut = 0
    diagonale_bas = 0
    for i in range(4):
        somme += carre[0][i]
        diagonale_haut += carre[i][i]
        diagonale_bas += carre[(i-1)%4][(i-1)%4]

    if somme != diagonale_bas or somme != diagonale_haut:
        return -1

    for x in range(4):
        somme_ligne = [0, 0]
        for y in range(4):
            somme_ligne[0] += carre[x][y]
            somme_ligne[1] += carre[y][x]
        if somme != somme_ligne[0] or somme != somme_ligne[1]:
            somme = -1
            break

    return somme

def carre_normal(carre):
    liste_entiers = [i for i in range(1, len(carre)**2+1)]
    for x in range(len(carre)):
        for y in range(len(carre[x])):
            if carre[x][y] in liste_entiers:
                del liste_entiers[liste_entiers.index(carre[x][y])]
            else:
                return "Non normal"
    return "Carré normal"

print(carre_normal(carre_pas_mag))