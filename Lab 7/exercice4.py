def move_zeros_v1(lst):
    i = 0
    lst_f = []
    for i in range (len(lst)):
        if lst[i] != 0:
            lst_f.append(lst[i])
    for i in range (len(lst)):
        if lst[i] == 0:
            lst_f.append(lst[i])
    print(lst_f)

def move_zeros_v2(lst):
    i = 0
    counter = 0
    while i < len(lst):
        if lst[i] == 0:
            del lst[i]
            counter += 1
            i = i - 1
        i += 1
    for x in range(counter):
        lst.append(0)
    print(lst)

def move_zeros_v3(lst):
    i = 0
    while i < len(lst)-1:
        a = 1
        if lst[i] == 0 and lst[i+1] != 0:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
        elif lst[i] == 0 and lst[i+a] == 0:
            while lst[i+a] == 0 and i+a < len(lst)-1:
                a +=1
            lst[i], lst[i+a] = lst[i+a], lst[i]
            i += 1
        else:
            i += 1
    print(lst)

        
            
            



lst =  [0,0,1, 0, 3, 0, 0, 5, 7]  
move_zeros_v3(lst)
