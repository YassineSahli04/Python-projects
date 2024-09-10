def compteur_m(l,v) :
    ''' (list, int) -> bool'''
    n_pas = 0
    n = 0
    for val in l :
        n_pas += 1
        if val == v :
            n += 1
    print("Nombre de pas: ", n_pas)
    return n
