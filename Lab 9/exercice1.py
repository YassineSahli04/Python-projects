from random import *
def cherche(lst, val):
    n_pas = 0
    for i in lst:
        n_pas += 1
        if i == val:
            return f"True, {n_pas}"
    return False
lst = []

for i in range(40):
    v = randrange(1, 50+1)
    lst.append(v)

print(cherche(lst , 46))