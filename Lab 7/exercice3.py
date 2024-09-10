def somme_de_trois(tuple):
    i = 0
    while i < len(tuple)-2:
        sum = tuple[i]+tuple[i+1]+tuple[i+2]
        if sum == 0:
            return True
            break
        i += 1
    return False
tuple = (2,3,3,2,2,2,1,1,3)
print(somme_de_trois(tuple))
