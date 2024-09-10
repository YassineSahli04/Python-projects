# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
    et ça continue jusqu'à la fin du paquet p.
    '''  
    donneur=[]
    autre=[]
    for x in range((int(len(p)//2+1))):
        i = 2*x
        donneur.append(p[i])
        if x < len(p)//2:
            autre.append(p[i+1]) 
    return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat = l
    i = 0
    while i < len(resultat):
        x = i+1
        while x < len(resultat):
            if resultat[i][0] == resultat[x][0]:
                del resultat[i]
                del resultat[x-1]
                i=-1
                break
            x += 1
        i += 1
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    s = ''
    for element in p:
        s += (element + ' ')
    print (s)

    
def entrez_position_valide(n):
    '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
    '''
    while n < 1 or n > num_tot_d:
        n=int(input(f"SVP entrez un entier de 1 à {num_tot_d}: "))
    return n
    





    


def joue():
    '''()->None
     Cette fonction joue le jeu'''
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()


    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    global num_tot_d
    num_tot_d = len(donneur)
    num_tot_h = len(humain)


    while num_tot_d > 1 or num_tot_h > 1:
        num_tot_d = len(donneur)
        num_tot_h = len(humain)
        print('''
Votre tour.
Votre main est:''')
        affiche_cartes(humain)

        #Prise de carte par humain
        num_h = int(input(f"J'ai {num_tot_d} cartes. Si 1 est la position de ma première carte et {num_tot_d} la position de ma dernière carte, laquelle de mes cartes voulez-vous? "))
        num_h = entrez_position_valide(num_h)
        global carte_h
        carte_h = donneur[num_h-1]
        humain.append(carte_h)
        del(donneur[num_h-1])
        print(f'''
Vous avez demandé ma carte numéro {num_h}.
La voilà. C'est un {carte_h}''')
        print(f'''
Avec  {carte_h} ajouté, votre main est: 
        ''')
        affiche_cartes(humain)
        print(f'''
Après avoir défaussé toutes les paires et mélangé les cartes, votre main est: 
        ''')
        humain = elimine_paires(humain)
        affiche_cartes(humain)
        num_tot_h = len(humain)
        num_tot_d = len(donneur)
        if num_tot_h == 0:
            print("Bravo, tu as gagné.")
            break
            
        attend_le_joueur()

        #Prise de carte par le donneur
        global index_d
        index_d = random.randint(0,num_tot_h-1)
        donneur.append(humain[index_d])
        del(humain[index_d])
        print(f'''
Mon tour.
J'ai pris votre {index_d+1}ème carte. 
        ''')
        donneur = elimine_paires(donneur)
        num_tot_h = len(humain)
        num_tot_d = len(donneur)
        if num_tot_d == 0:
            print("J'ai gagné.")
            break   
        attend_le_joueur()

# programme principale
joue()


