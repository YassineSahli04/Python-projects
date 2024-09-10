def compte(s,c):
    n =  s.count(c)
    return n
def compte2(s,c):
    c_element = list(c)
    s_element = list(s)
    counter = 0
    y_max =len(c_element)-1
    for x in range(len(s_element)):
        y = 0
        while s_element[x] == c_element[y]:
            if y == y_max:
                counter += 1
                break
            y += 1
            x += 1
    return counter
s = input('Entrez une chaine de caractère: ')
c = 'a'
print(compte(s,c))
print(compte2(s,c))
print(' ')
c = 'de la'
print(compte(s,c))
print(compte2(s,c))
