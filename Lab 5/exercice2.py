def note(lst):
    print(lst)
    list = []
    n_element = len(lst)
    somme = 0
    for i in lst:
        somme += i
    moyenne = somme / n_element
    list.append(moyenne)
    print(f'La moyenne de cette liste est {moyenne}')
    max = lst[0]
    for i in range(1,n_element):
        if max < lst[i]:
            max = lst[i]
    list.append(max)
    print(f'La valeur maximale de cette liste est {max}')
    min = lst[0]
    for i in range(1,n_element):
        if min > lst[i]:
            min = lst[i]
    list.append(min)
    print(f'La valeur minale de cette liste est {min}')
    return list 
lst = []
element = float(input('entrez une une première note dans cette liste: '))
lst.append(element)
answer = 'y'
while answer.capitalize() == 'Y':
    element = float(input('entrez une autre note dans la liste: '))
    lst.append(element)
    answer = input("Voulez-vous entrer une nouvelle note ( Y , N ): ")
note(lst)
