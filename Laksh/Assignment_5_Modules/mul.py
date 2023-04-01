def list_f():
    list_1 = [1,2]
    list_2 = [3,4]
    l = []
    for i in list_1:
        for j in list_2:
            l.append(i * j)
    print(l)
    