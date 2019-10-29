n=int(input('n: '))
f=1
aux=0
while n>=f*(f+1)*(f+2) and aux==0:
    if n==f*(f+1)*(f+2):
        print('triangular')
        aux=1
    else:
        f=f+1   
if n<f*(f+1)*(f+2):
    print('nao triangular')
