# Question 1
def transl(d, s):
    s_f = ""
    words = s.split()  
    for word in words:
        if word in d:
            s_f += d[word]
        elif s in d.values():
            for cle, valeur in d.items():
                if valeur == s:
                    return cle
        else:
            return "Unknown"
    return s_f


#Question 2:
def setOp(list1,list2) :
    l = set(list1 + list2)
    return l


#Question 3:
def matrixMinMax(M):
    max = M[0][0]  
    min = M[0][0]    
    for m in M:
        for e in m:
            if e > max:
                max = e
            elif e < min:
                min = e
    tup = (min, max)
    return tup

