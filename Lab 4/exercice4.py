
def calculeFact(N):
    while N < 0:
        print('Vous devez rentrez un nombre positif')
        N = int(input("Entrez une nouvelle valeur de N (entier) positif: "))
    
    if N != 0:
        res = 1
        for i in range (1, N+1):
            res = i * res
        print(res)
    else:
        print('1')
N = int(input("Entrez une valeur de N (entier) positif: "))
calculeFact(N)
