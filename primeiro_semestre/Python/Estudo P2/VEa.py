def copia_vetor(a,b,tam):
    for i in range(tam):
        b[i]=a[i]

n=int(input('n: '))
a=[0]*n
b=[0]*n

for i in range(n):
    a[i]=int(input('a[%d]= ' %i))
for i in range(n):
    b[i]=int(input('b[%d]= ' %i))

copia_vetor(a,b,n)

for i in range(n):
    print('a[%d]=%d ' %(i,a[i]))
for i in range(n):
    print('b[%d]=%d ' %(i,b[i]))


    
