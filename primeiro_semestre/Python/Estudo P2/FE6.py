def tamanho(n):
    cont=1
    while n>=10:
        n=n//10
        cont += 1
    return cont

n=int(input('n: '))
r=tamanho(n)
print(r)
        
