
def verif(l,i=0):
    if i==len(l):
        return True
    if not 0<=l[i]<=9:
        return False
    return verif(l,i+1)


