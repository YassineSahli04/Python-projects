def multiplication_matrice(M_1, M_2):
    C = []
    for l_m1 in range(len(M_1)):
        c = []
        for c_m2 in range(len(M_2[0])):
            somme = 0
            for c_m1 in range(len(M_1[0])):
                l_m2 = c_m1
                produit = M_1[l_m1][c_m1]*M_2[l_m2][c_m2]
                somme += produit
            c.append(somme)
        C.append(c)
    return C
M_1 = [[1,2,3],[4,5,6]]
M_2 = [[1,2],[3,4],[5,6]]
multiplication_matrice(M_1, M_2)
