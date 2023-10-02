# Exercice 01 :
n = int(input("Donner un nombre :"))
if n % 5 == 0: 
    print("Hello")
else:
    print("Bye")

# Exercice 02 :
nombres = input("Entrer deux nombres et un opérateur ").split()
match nombres[2]:
    case "+":
        print(int(nombres[1]) + int(nombres[0]))
    case "-":
        print(int(nombres[1]) - int(nombres[0]))
    case "*":
        print(int(nombres[1]) * int(nombres[0]))
    case "/":
        print(int(nombres[1]) / int(nombres[0]))
    
# Exercice 03 
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))


if nombre1 >= nombre2 >= nombre3 or nombre3 >= nombre2 >= nombre1:
    deuxieme_plus_grand = nombre2
elif nombre2 >= nombre1 >= nombre3 or nombre3 >= nombre1 >= nombre2:
    deuxieme_plus_grand = nombre1
else:
    deuxieme_plus_grand = nombre3

print("Le deuxième plus grand nombre est :", deuxieme_plus_grand)


# Exercice 04 :
cotes = input("Entrer trois côtés ").split()
cotes = [int(cotes[i]) for i in range(len(cotes))]
for i in range(3):
    if cotes[i]**2 == cotes[(i+1)%3]**2 + cotes[(i+2)%3]**2:
        print("Configuration correcte :", "hypothénuse :", cotes[i], "Deux autres côtés :", str(cotes[(i+1)%3]) + ", " +  str(cotes[(i+2)%3]))