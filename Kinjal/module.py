def num():
    list_1=[1,2,3]
    list_2=[4,5,6]
    list_3=[]
    for j in list_1:
        for k in list_2:
            list_3.append(j*k)
    print(list_3)