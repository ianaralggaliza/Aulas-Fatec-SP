def subtrair(x, y):
    aux = 0
    while x >= y:
        x = x - y
        aux = aux + 1
        return aux
x = int(input())
y = int(input())
print(subtrair())
