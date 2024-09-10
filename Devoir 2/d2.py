#Question1:
#Je crée une fonction qui vérifie si c'est possible de patiner en fonction de la température et de l'épesseur de la glace
def patinage(épaisseur, temp):
    if épaisseur >= 30 and temp <= -10:
        return True
    else:
        return False


#Question2:
#La fonction vérifie la correspondance d'une note en nombre à une lettre aphabétique.

def alphaNote(notefinale):
    if  90 <= notefinale <= 100:
        return "A+"
    elif  85 <= notefinale <= 89:
        return "A"
    elif  80 <= notefinale <= 84:
        return "A-"
    elif  75 <= notefinale <= 79:
        return "B+"
    elif  70 <= notefinale <= 74:
        return "B"
    elif  65 <= notefinale <= 69:
        return "C+"
    elif  60 <= notefinale <= 64:
        return "C"
    elif  55 <= notefinale <= 59:
        return "D+"
    elif  50 <= notefinale <= 54:
        return "D"
    elif  40 <= notefinale <= 49:
        return "E"
    elif  0 <= notefinale <= 39:
        return "F"
#(float)->str

#Question3:
#Cette fonction vérifie tout d'abord si la note est comprise entre 0 et 100 puis voit si l'lève a réussi ou non en fonction de sa note
def  alphaNoteVerif(notefinale):
    
    while notefinale < 0 or notefinale > 100 :
        notefinale = float(input("Réintroduits une autre note entre 0 et 100: "))
    
    resultat = alphaNote(notefinale)
    print(resultat)
    if resultat == 'E' or resultat == 'F':
        print("Echoue")
    else:
        print("Reussi")
notefinale = float(input("Entrer votre note finale: "))
alphaNoteVerif(notefinale)


#Question4
#Cette fonction prend un entier et affiche chaque 2 valeurs de 1 à n 
def boucle(n):
    if n%2 ==0:
        x = int(n/2)
    else:
        x = int(n/2) + 1
    for i in range(x):
        a = 2*i + 1
        print(a)
    print(' ')

    if n%2 == 0:
        x = int(n/2)
    else:
        x = int(n/2) + 1
    for i in range(x):
        a = n - 2*i 
        print(a)
    print(' ')
#(int) --> none
boucle(10)
        







#Question5:
#Cette fonction donne les facteur d'un entier et ensuite donne leur somme
def facteursDeN(n):
    lst = []
    for i in range(2,n-1):
        if n%i == 0:
            lst.append(i)
            print(i)
            i += 1
            
    
    somme = sum(lst)
    print(somme)
    if somme < n:
        return True
    else:
        return False

#(int) --> boolean 
facteursDeN(6)



#Question 6:
#Cette fonction vérifie si un nombre est un carré parfait ou non 
def carreParfait(x):
    n = 1
    a = int(x/2)
    while n <= x:
        if n**2 == x:
            print(f"{x} est un carré parfait.")
            return True
            break
        elif n**2 != x and n == a:
            print(f"{x} n'est pas un carré parfait.")
            return False
        
        n += 1
carreParfait(10)

#Question 7:
#cette fonction prend un nombre entier est rend le résultat d'une fonction : ((-1)**n)/(2*n+1)
def maFun(n):
    res = ((-1)**n)/(2*n+1)
    return res


#Question 8:
#Cette fonction prend un entier et retourne le résultat de cette fonction: 4(1-(1/3)+(1/5)-(1/7)+ ... +(((-1)**n)/(2*n+1)))
def maFun_bis(n):
    tot = 0
    for i in range(n):

        x = maFun(i)
        tot += x

    res = 4*tot
    return res
maFun_bis(10000)
