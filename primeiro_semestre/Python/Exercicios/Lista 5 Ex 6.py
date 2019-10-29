def tamanho(n):
    cont=0
    if n==0:
        return 1
    while n!=0:
        n=n//10
        cont=cont+1
    return cont

n=int(input('n: '))
print(tamanho(n))

