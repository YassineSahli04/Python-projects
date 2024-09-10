a = float(input("Entrer un nombre 'a' correspondant à l'equation quadratique ax² + bx + c = 0 : "))
b = float(input("Entrer un nombre 'b' correspondant à l'equation quadratique ax² + bx + c = 0 : "))
c = float(input("Entrer un nombre 'c' correspondant à l'equation quadratique ax² + bx + c = 0 : "))

delta = b**2 - 4*a*c

if delta > 0:
    print("Il y a deux racines réelles.")
    
elif delta < 0:
    print("Il y a aucune racine réelle.")

else:
    print("Il y a une racine réelle.")

    
