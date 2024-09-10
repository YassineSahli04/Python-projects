def anneeBis(an):
    an = int(an)
    if an % 4 != 0:
        print(f"L'année {an} n'est pas bissextile.")
    else:
        if an % 100 == 0 and an % 400 != 0:
            print(f"L'année {an} n'est pas bissextile.")
        else:
            print(f"L'année {an} est bissextile.")
an = input("Entrer une année pour voir si elle est bissextile ou non: ")
anneeBis(an)
#strg
