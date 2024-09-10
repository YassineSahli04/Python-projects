def coder(a):
    element = list(a)
    s_f = ''

    i = 0
    x =0
    y = 0
    while x < len(element) and y < len(element):
        x = 2*i
        y = 2*i+2   
        element.insert(y,element[x])
        element.pop(x)
        i += 1
    
    for z in element:
        s_f += z
    
    return s_f

print(coder('Message'))
