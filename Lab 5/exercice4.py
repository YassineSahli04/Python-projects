def ecart_type(lst):
    n_element = len(lst)
    somme = 0
    for i in lst:
        somme += i
    moyenne = somme / n_element
    somme_carre = 0
    for i in range(n_element):
        somme_carre += ((lst[i] - moyenne)**2)
    
    s =((somme_carre/n_element)**(1/2))
    s = format(s, '.5f')
    print(f"L'écart type  de cette liste est {s}")


lst = []
element = float(input('entrez une une première note dans cette liste: '))
lst.append(element)
answer = 'y'
while answer.capitalize() == 'Y':
    element = float(input('entrez une autre note dans la liste: '))
    lst.append(element)
    answer = input("Voulez-vous entrer une nouvelle note ( Y , N ): ")
ecart_type(lst)
