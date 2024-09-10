from random import *
num = randint(1,10)


def devine(num_utilisateur):
    conteur = 1
    while num_utilisateur != num:
        if num_utilisateur > num:
            print("Ce n'est le bon nombre. Le nombre que vous cherchez est plus petit.")
            num_utilisateur = int(input('Entrez un nouveau nombre: '))
        elif num_utilisateur < num:
            print("Ce n'est le bon nombre. Le nombre que vous cherchez est plus grand.")
            num_utilisateur = int(input('Entrez un nouveau nombre: '))
        conteur += 1
    print(f'Bravo, vous avez trouver le bon nombre après {conteur} essaie')
    return conteur
    
    

num_utilisateur = int(input('Entrez un nombre entier entre 1 et 10 pour essayer de deviner le nombre choisi par le programme: '))
devine(num_utilisateur)
                        
