def matrice_somme(M_1, M_2):
    C = []
    for a in range(len(M_1)):
        c = []
        for b in range(len(M_1[0])):
            M_1[a][b]
            M_2[a][b]
            s = M_1[a][b] + M_2[a][b]
            c.append(s)
            if b == len(M_1[0])-1:
                    C.append(c)
    return C
M_1 = [[1,2,3],[4,5,6]]
M_2 = [[1,2,4],[4,5,5]]
print(matrice_somme(M_1, M_2))
