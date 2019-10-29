n=int(input('n: '))
acpar=0
acimpar=0
for i in range(n):
    lido=int(input('insira um numero:'))
    if (lido%2)==0:
        acpar=acpar+lido
    else:
        acimpar=acimpar+lido
print('soma dos valores pares: ', acpar)
print('soma dos valores impares: ', acimpar)
