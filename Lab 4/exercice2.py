
def x(N):
    for i in range (1,N+1):
        print(i)
def y(N):
    compteur = 1
    while(compteur <= N):
        print(compteur)
        compteur = compteur + 1

N = int(input("Entrez une valeur de N (entier): "))
y(N)
print(' ')
x(N)

