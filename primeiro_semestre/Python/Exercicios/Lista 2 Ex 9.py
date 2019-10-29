a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
if a==b:
    if b==c:
        print('equilatero')
    else:
        print('isosceles')
else:
    if (b==c) or (a==c):
        print('isosceles')
    else:
        print('escaleno')
