#Question 1
#(liste) --> int
def compte100(liste):
    counter = 0
    for i in range(len(liste)):
        if liste[i] > 100:
            counter += 1
    return counter

#Question 2
#(liste) --> float
def sommeListeDiv2(liste):
    sum = 0
    for i in range(len(liste)):
        if liste[i] % 2 ==0:
            sum += liste[i]
    return sum


#Question 3
#(str) --> bool
def triples(s):
    for i in range((len(s)-2)):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return True
            break
    return False

#Question 4
#(str) --> str
def momo(s): 
    i = 0
    lst = []
    while i < len(s):
        counter = 1
        lettre = s[i]
        lst.append(lettre)
        while i < len(s)-1 and s[i] == s[i+1]:
            counter += 1
            i += 1
        lst.append(str(counter))
        i += 1
    s_f =''
    for i in range(len(lst)):
        s_f += lst[i]
    return s_f

#Question 5
#(str) --> str
def noDup(s):
    i = 0
    s_1 = ''
    while i < len(s):
        lettre = s[i]
        while i < len(s)-1 and s[i] == s[i+1]:
            i += 1
        i += 1
        s_1 += lettre
    #Partie non comprise dans la question
    #cette partie de la fonction élimine les lettres qui se répètent dans la chaine de caractère corrigée et laisse le caractère affiché en premier
    ''' for x in range(len(s_1)):
        y = x+1
        while y < len(s_1):
            if s_1[x] == s_1[y]:
                y = abs(y)
                s_1 = s_1[:y]+s_1[y+1:]
                y += 1
            y += 1
        y += 1  '''
    return s_1 