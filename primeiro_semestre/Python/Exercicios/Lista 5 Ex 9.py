def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

while True:
    n=int(input('n: '))
    if primo(n):
        print('E primo')
    else:
        print('Nao e primo')
