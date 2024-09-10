def transpose(M):
    i = 0
    M_f = []
    for i in range(len(M[0])):
        L = []
        for l in M:
            c = l[i]
            L.append(c)
            if l == M[-1]:
                M_f.append(L)
    return M_f
M = input("Entrez votre matrice: ")
print(transpose(M))
