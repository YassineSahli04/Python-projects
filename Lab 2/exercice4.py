#NAME: Yassine Sahli
#Student Number: 300383586
from math import *
def surface_triangle(coté1, coté2, coté3):
    p = coté1 +coté2 + coté3
    s = sqrt(p*(p-2*coté1)*(p-2*coté2)*(p-2*coté3))/4
    return s
coté1 =10
coté2 =15
coté3 =18
s = surface_triangle(coté1, coté2, coté3)
print(f"L'aire du triangle ayant les trois côtés: ({coté1, coté2, coté3}) est {s}") 
