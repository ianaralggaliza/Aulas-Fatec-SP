def troca(a,b,m,n):
    x=0
    for i in range(m):
        for j in range(n):
            x=a[i][j]
            a[i][j]=b[i][j]
            b[i][j] = x

'''m=int(input('linhas: '))
n=int(input('colunas: '))
'''

m=3
n=3

a = [[4,5,6],
     [4,5,6],
     [7,8,9]]

b = [[200,1000,1001],
     [201,202,203],
     [953,297,329]]

print('Antes da troca')
print(a)
print(b)

troca(a,b,m,n)

print('Depois da troca')
print(a)
print( )
print(b)

'''
a=0
b=0
for i in range(m):
    for j in range(n):
        a[i][j]=int(input('a[%d][%d]= ' %i %j))
        b[i][j]=int(input('b[%d][%d]= ' %i %j))
'''
