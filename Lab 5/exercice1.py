def moyenne(lst):
    n_element = len(lst)
    somme = 0
    for i in lst:
        somme += i
    moyenne = somme / n_element
    print(lst)
    print(f'La moyenne de cette liste est {moyenne}')
lst = []
element = float(input('entrez un élément de votre liste: '))
lst.append(element)
answer = 'y'
while answer.capitalize() == 'Y':
    element = float(input('entrez un autre élément de votre liste: '))
    lst.append(element)
    answer = input("Voulez-vous entrer un nouveau nombre ( Y , N ): ")
moyenne(lst)
    
