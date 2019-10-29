while True: 
    a=int(input('data 1 dia: '))
    b=int(input('data 1 mes: '))
    c=int(input('data 1 ano: '))
    d=int(input('data 2 dia: '))
    e=int(input('data 2 mes: '))
    f=int(input('data 2 ano: '))
    if c<f:
#print('data que ocorre primeiro: %i/%i/%i' % (a,b,c))
        print('data que ocorre primeiro: ', a,'/',b,'/',c)
    elif f<c:
        print(d,'/',e,'/',f)
#print('data que ocorre primeiro: %i/%i/%i' % (d,e,f))
    elif b<e:
        print(a,'/',b,'/',c)
#        print('data que ocorre primeiro: %i/%i/%i' % (a,b,c))
    elif e<b:
        print(d,'/',e,'/',f)
#        print('data que ocorre primeiro: %i/%i/%i' % (d,e,f))
    elif a<d:
        print(a,'/',b,'/',c)
#        print('data que ocorre primeiro: %i/%i/%i' % (a,b,c))
    else:
        print(d,'/',e,'/',f)
#        print('data que ocorre primeiro: %i/%i/%i' % (d,e,f))
