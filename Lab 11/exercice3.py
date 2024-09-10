def pgcd(x,y):
    if x==y:
        return x
    if x>y:
       i= x-y
    else:
        i=y-x
    return pgcd(min(x,y),i)
