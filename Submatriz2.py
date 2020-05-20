def sumafila(fila):
    suma=0
    i=0
    while i < len(fila):
        if fila[(i-1)]== 0:
            return 0;
        else:
            suma+=int(fila[int(i)-1])
        i+=1
    return suma

n=int(input())
for _ in range(n):
    ma = []
    fc = int(input())
    v=[0]*fc
    for i in range(fc):
        ma.append([]*fc)
    for i in range(fc):
        ma[i] = [int(x) for x in input().split()]
    for k in range(fc):
        for i in range(fc):
            for j in range(i+1,fc+1):
                v[j-1]=sumafila(ma[k][i:j])
            suma=0
            for j in range(1,fc):
                suma+=v[j]
            print("Suma:"+str(suma))