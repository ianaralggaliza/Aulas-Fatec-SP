def divisao(p,q):
    ac=0
    while p>=q:
        p=p-q
        ac +=1
    return ac

x=int(input('número: '))
y=int(input('número: '))
r=divisao(x,y)
print(r)
