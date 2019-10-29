def zera_ind_par(a, tam):
    for i in range (tam):
        if i % 2 == 0:
            a[i] = 0

tam = int(input('insira o tamanho: '))
a = [1] * tam
for i in range (tam):
    a[i] = int(input('insira um numero: '))
zera_ind_par(a, tam)
print(a)
