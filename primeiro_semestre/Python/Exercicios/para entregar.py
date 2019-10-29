while True: 
    a=int(input('data 1 dia: '))
    b=int(input('data 1 mes: '))
    c=int(input('data 1 ano: '))
    d=int(input('data 2 dia: '))
    e=int(input('data 2 mes: '))
    f=int(input('data 2 ano: '))
    if c<f:
        print('data que ocorre primeiro: ', a,'/',b,'/',c)
    elif f<c:
        print('data que ocorre primeiro: ', d,'/',e,'/',f)
    elif b<e:
        print('data que ocorre primeiro: ', a,'/',b,'/',c)
    elif e<b:
        print('data que ocorre primeiro: ', d,'/',e,'/',f)
    elif a<d:
        print('data que ocorre primeiro: ', a,'/',b,'/',c)
    else:
        print('data que ocorre primeiro: ', d,'/',e,'/',f)

