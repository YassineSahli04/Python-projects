def dict(s):
    s = list(s)
    s.sort()
    dict = {}
    i = 0
    while i < len(s):
        lettre = s[i]
        nombre_de_répétition = str(s.count(s[i]))
        x = i + 1
        while x < len(s):
            if s[i] == s[x]:
                del s[x]
                x = x - 1
            x += 1
        dict[lettre] = nombre_de_répétition
        i += 1
    return dict
s = input("Entrez une chaine de caractère: ")
print(dict(s))
