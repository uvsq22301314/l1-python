"""
# Exercice 1
a, b = input("Entrer deux nombres entiers ").split()
if a > b:
    a, b = b, a

# Exercice 2 
from random import randint
nb = randint(10, 99) 
user_nb = int(input("Entrer un nombre "))
if user_nb > 1 and nb/user_nb == nb//user_nb:
    print("Diviseur")

# Exercice 3
var1, var2 = 2, 3
if (var1 >= 0 and var2 >= 0) or (var1 <= 0 and var2 <= 0):
    var1, var2 = var2, var1
else:
    produit = var1 * var2
    var1 = var1 ** var2
    produit = var2 # ??????????
"""

#! WHILE
# Exercice 1
def pgcd(a, b):
    pg = 1
    if b > a:
        a, b = b, a
    for i in range(2, a+1):
        if a/i == a//i and b/i == b//i:
            pg = i
    return pg

def anniversaire():
    solde = 0
    n = input("Combien d'anniversaire ")
    for i in range(int(n)):
        solde = solde + 3 * i + 120
    return solde 


def oe():
    nb = int(input("Nombre : "))
    for i in range(nb-1, nb - 10, -1):
        print(i)
