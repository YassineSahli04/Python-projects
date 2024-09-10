def dict(s):
    s = list(s)
    s.sort()
    dict = {

    }
    i = 0
    while i < len(s):
        nombre = s[i]
        nombre_de_répétition = str(s.count(s[i]))
        x = i + 1
        while x < len(s):
            if s[i] == s[x]:
                del s[x]
                x = x - 1
            x += 1
        dict[nombre] = nombre_de_répétition
        i += 1
    return dict
s = (2, 3,3,2,2,2,1,1,3)
print(dict(s))
