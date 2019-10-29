def produto(a,b):
    p=0
    for i in range(1, a+1):
        p=p+b
    return p

x=int(input('número: '))
y=int(input('número: '))
t=produto(x,y)
print (t)
