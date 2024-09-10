def cherche_m(M, val):
    n_pas = 0
    for l in M:
        for e in l:
            n_pas += 1
            if e == val:
                return f"True, {n_pas}"              
    return False
M = [[1,2,10],[7,5,6], [8,8,9,10]]
print(cherche_m(M,5))