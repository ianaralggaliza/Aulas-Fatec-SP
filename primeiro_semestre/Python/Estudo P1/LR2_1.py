n=int(input('n: '))
f=1
p=6
while n>p:
    p=f*(f+1)*(f+2)
    f=f+1
if n==p:
    print('tringular')
else:
    print('nao triangular')
