'''
+------------------------------------------------------------------------------------------+
| Instituição  :  Faculdade de Tecnologia de São Paulo                                     |
| Departamento :  Tecnologia da Informação                                                 |
| Curso        :  Análise e Desenvolvimento de Sistemas                                    |
| Disciplina   :  IAL-002                                                                  |
| Turno        :  Vespertino                                                               |
| Aluno        :  Ianara Leite Gonçalves Galiza                                            |
| Matrícula    :  18203711                                                                 |
+------------------------------------------------------------------------------------------+
| Programa     :  EP02.py - Intercalação de vetores                                        |
| Linguagem    :  Python 3                                                                 |
| Compilador   :  CPython (3.7.0)                                                          |
+------------------------------------------------------------------------------------------+
'''


def ordenacao(a, m):
    for i in range(m-1):
        for j in range(i+1, m):
            if a[i] > a[j]:
                x = a[j]
                a[j] = a[i]
                a[i] = x

def intercala(a, b, c, m, n):

    i = 0
    j = 0
    k = 0

    while i<m and j<n: 
            
        if a[i] < b[j]:
            c[k] = a[i]
            i = i + 1
            k = k + 1

        elif b[j] < a[i]:
            c[k] = b[j]
            j = j + 1
            k = k + 1
            
        else:
            c[k] = a[i]
            i = i + 1
            j = j + 1
            k = k + 1
            
    if i == m:
        for z in range(j, n):
            c[k] = b[z]
            k = k + 1

    elif j == n:
        for w in range(i, m):
            c[k] = a[w]
            k = k + 1

    return k          
 
    
m=int(input("m: "))
a=[0]*m
for i in range(m):
    a[i]=int(input("a: "))
    
n=int(input("n: "))
b=[1]*n
for j in range(n):
    b[j]=int(input("b: "))

for i in range(m):
    if i == (m-1):
        print(a[i])
    else:
        print(a[i], end = " ")
        
for j in range(n):
    if j == (n-1):
        print(b[j])
    else:
        print(b[j], end = " ") 

ordenacao(a, m)
ordenacao(b, n)

for i in range(m):
    if i == (m-1):
        print(a[i])
    else:
        print(a[i], end = " ")
        
for j in range(n):
    if j == (n-1):
        print(b[j])
    else:
        print(b[j], end = " ")

c=[0]*(m+n)
 
t=intercala(a, b, c, m, n)

for i in range(t):
    print(c[i], end = " ")
