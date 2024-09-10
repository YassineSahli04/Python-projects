age = int(input("Quel est votre age: "))
if age >= 18 and age <= 55:
    valeur = True
else:
    valeur = False

if valeur == True:
    print("Transaction acceptée")
else:
    print("Transaction refusée")
