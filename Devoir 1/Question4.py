def bibformat(auteur, titre, ville, maisonEdition, annee):
    chaine = auteur + " (" + f"{annee}" + "). " + titre + "." + ville + ": " + maisonEdition
    return chaine


def bibformatPrint():
    titre = input("Entrez le titre du livre: ")
    auteur = input("Entrez le nom de l'auteur du livre: ")
    annee = input("Entrez l'année de publication du livre: ")
    maisonEdition = input("Entrez la maison d'édition du livre: ")
    ville = input("Entrez la ville de la maison d'édition du livre: ")
    chaine = bibformat(auteur, titre, ville, maisonEdition, annee)
    print(chaine)

bibformatPrint()
    
