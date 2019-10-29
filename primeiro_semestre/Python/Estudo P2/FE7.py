def impar(n):
    if n%2 != 0:
        return True
    else:
        return False

n=int(input('n: '))
if impar(n):
    print('É ímpar')
else:
    print('É par')
