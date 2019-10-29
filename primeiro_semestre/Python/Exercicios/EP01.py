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
| Programa     :  EP01.py - Título do EP                                                   |
| Linguagem    :  Python 3                                                                 |
| Compilador   :  CPython (3.7.0)                                                          |
+------------------------------------------------------------------------------------------+
'''





dia=int(input('Insira o dia: '))
mes=int(input('Insira o mes: '))
ano=int(input('Insira o ano: '))
if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10) and ((1<=dia) and (dia<=31)) and (ano>0):
    if (1<=dia and dia<=30):
        dia=dia+1
        print(dia,mes,ano)
    else:
        dia=1
        mes=mes+1
        print(dia,mes,ano)
elif (mes==12) and ((1<=dia) and (dia<=31)) and (ano>0):
    if (1<=dia and dia<=30):
        dia=dia+1
        print(dia,mes,ano)
    else:
        dia=1
        mes=1
        ano=ano+1
        print(dia,mes,ano)
elif (mes==4 or mes==6 or mes==9 or mes==11) and ((1<=dia) and (dia<=30)) and (ano>0):
    if (1<=dia and dia<=29):
        dia=dia+1
        print(dia,mes,ano)
    else:
        dia=1
        mes=mes+1
        print(dia,mes,ano)
elif (mes==2) and ((1<=dia) and (dia<=29)) and (ano>0):
    if (1<=dia and dia<=27):
        dia=dia+1
        print(dia,mes,ano)
    elif((ano%4==0) and (ano%100!=0)) or (ano%400==0):
        if(dia==28):
            dia=dia+1
            print(dia,mes,ano)
        else:
            dia=1
            mes=mes+1
            print(dia,mes,ano)
    else:
        if(dia==28):
            dia=1
            mes=mes+1
            print(dia,mes,ano)
        else:
            print('Data inválida')
else:
    print('Data inválida')
