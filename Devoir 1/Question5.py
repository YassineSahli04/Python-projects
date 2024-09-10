def logFun(x):
    import math
    y = math.log((x+3)**(1/4),10)
    return y
x = float(input("Entrez un nombre positif: "))
print(logFun(x))
#float
