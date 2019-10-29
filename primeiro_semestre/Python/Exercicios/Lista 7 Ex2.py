def identidade(a, m, n):
    if m != n:
        return False
    for i in range(m):
        for j in range(n):
            if i == j and a[i][j] != 1:
                return False
            elif i != j and a[i][j] != 0:
                return False
    return True

a = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]

m = 4
n = 4
f=identidade(a,m,n)
print(f)


            
                
