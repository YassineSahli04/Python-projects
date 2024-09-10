#Question 1:
#La fonction tempsVoyage prend les valeurs de la distance et de la vitesse et calcule le temps en minutes
def tempsVoyage(distance, vitesse):
    temps = (distance*60) / vitesse 
    return temps  
tempsVoyage(400, 100)


#Question 2:
#La fonction prend 5 variables (les notes d'un élève) et retourne la note finale
def noteFinale(labos, devoirs, quiz, examen_partiel, examen_final):
    notefinale = labos*0.1 + devoirs*0.25 + quiz*0.05 + examen_partiel*0.2 + examen_final*0.4
    return notefinale
noteFinale(80,95,86,79,92)


#Question 3:
#Cette fonction prend 5 variables (4 chaines de caractère et un entier) et puis retourne une chaine de caractère sous un format donné.
def bibformat(auteur, titre, ville, maisonEdition, annee):
    chaine = auteur + " (" + f"{annee}" + "). " + titre + ". " + ville + ": " + maisonEdition
    return chaine
bibformat('sa','dd','ee','rr',2020)
 


#Question 4:
#La fonction intègre 5 variable du clavier d'un utilisateur, puis grace à la fonction de la question 3 affiche une chaine de caractère contenant les variable sous le format demandé et finalement la fonction affiche la chaine de caractère mais ne retourne rien.
def bibformatPrint():
    titre = input("Entrez le titre du livre: ")
    auteur = input("Entrez le nom de l'auteur du livre: ")
    annee = int(input("Entrez l'année de publication du livre: "))
    maisonEdition = input("Entrez la maison d'édition du livre: ")
    ville = input("Entrez la ville de la maison d'édition du livre: ")
    chaine = bibformat(auteur, titre, ville, maisonEdition, annee)
    print(chaine)
bibformatPrint()



#Question 5:
#Cette fonction prend un nombre positif et résoud pour ce nombre l'équation  10**4y=x+3 puis renvoie la valeur de y qui satisfait l'équation.
#(float) --> float
def logFun(x):
    import math
    y = math.log((x+3),10)/4
    return y
x = float(input("Entrez un nombre positif: "))
print(logFun(x))



#Question 6:
#Cette fonction vérifie si une année (un nombre positif et supérieur 1582) est une année bisextile ou pas et renvoie vrai ou faux.
def anneeBis(an):
    an = int(an)
    if an > 1582:
        if an % 4 != 0:
            return False
        else:
            if an % 100 == 0 and an % 400 != 0:
                return False
            else:
                return True
an = input("Entrer une année (nombre entier et supérieur à 1582) pour voir si elle est bissextile ou non: ")
anneeBis(an)
#(float) --> (boolean)


