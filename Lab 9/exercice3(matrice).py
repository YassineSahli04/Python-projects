def compteur_m(l,v) :
    ''' (list, int) -> bool'''
    n_pas = 0
    n = 0
    for r_v in l :
        for c_v in r_v :
            n_pas += 1
            if c_v == v :
                n += 1
    print("Nombre de pas: ", n_pas)
    return n

l1 = [[1,2,10],[7,5,6], [8,8,9], [5,2,8]]
print(l1)

print(compteur_m(l1,8))

