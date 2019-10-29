def iguais (a, b, n):
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True

n = int(input('insira o tamanho dos vetores: '))
a = [0] * n
b = [0] * n
for i in range(n):
    a[i] = int(input('a: '))
    b[i] = int(input('b: '))
print(a)
print(b)
print(iguais(a, b, n))

