from math import *
def distance(v):
    lst0 = [0,10,20,30,40,50,60,70,80,90]
    lst = []
    for i in range(len(lst0)):
        a = (pi*lst0[i])/180
        distance = (2*(v**2)*cos(a)*sin(a))/9.8
        lst.append(format(distance,'.3f'))
    print(lst)
distance(10)
