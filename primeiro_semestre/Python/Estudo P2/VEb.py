def soma_vetores(a,b,c,tam):
    for i in range(tam):
        c[i]=a[i]+b[i]

n=int(input('n: '))
a=[0]*n
b=[1]*n
c=[2]*n

for i in range(n):
    a[i]=int(input('a[%d]= ' %i))

for i in range(n):
    b[i]=int(input('b[%d]= ' %i))

soma_vetores(a,b,c,n)

for i in range(n):
    print('c[%d]=%d' %(i,c[i]))
    
        
