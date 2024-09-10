n= int(input("Entrez un nombre n:"))
def creer(ls,n,i):
    if i==n:
        return l
    if i < n:
        l.append(i)
    return creer(l,n,i+1)
l=[]
print(creer(l,n,0))
