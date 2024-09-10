def bibformat(auteur, titre, ville, maisonEdition, annee):
    chaine = auteur + " (" + f"{annee}" + "). " + titre + "." + ville + ": " + maisonEdition
    return chaine
bibformat('sa','dd','ee','rr',2020)
