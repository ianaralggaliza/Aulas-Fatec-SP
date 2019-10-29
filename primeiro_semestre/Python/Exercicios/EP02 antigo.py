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
| Programa     :  EP02.py - Intercalação de vetores                                                   |
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

    comeca_em_a = False
    indice_a = 0
    indice_b = 0
    
    if a[0]<b[0]:
        c[0]=a[0]
        comeca_em_a = True
        indice_a = 1
        
    else:
        c[0]=b[0]
        indice_b = 1

    for indice_c in range(1, m+n):
        if comeca_em_a:
            '''                   ou  b acabou então coloca a no ímpar    e    a não acabou, então completa com a'''
            if ((indice_c%2 == 0) or (indice_b >= n)) and (indice_a < m):
                c[indice_c]=a[indice_a]
                indice_a = indice_a + 1
            else:
                c[indice_c]=b[indice_b]
                indice_b = indice_b + 1
        else:
            if ((indice_c%2 == 0) or (indice_a >= m)) and (indice_b < n):
                c[indice_c]=b[indice_b]
                indice_b = indice_b + 1
            else:
                c[indice_c]=a[indice_a]
                indice_a = indice_a + 1

    

m=int(input("m: "))
a=[0]*m

for i in range(m):
    a[i]=int(input("a: "))
    
n=int(input("n: "))
b=[1]*n

for i in range(n):
    b[i]=int(input("b: "))

print(a)
print(b)

ordenacao(a, m)
ordenacao(b, n)

print(a)
print(b)

c=[0]*(m+n)
 
intercala(a, b, c, m, n)

print(c)
