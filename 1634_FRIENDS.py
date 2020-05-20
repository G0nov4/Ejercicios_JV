n = int(input())
dicc = {}
for i in range(n):
    cad = input()
    cad = cad.split()
    for i in cad:
        if i in dicc:
            dicc[i]=dicc.get(i)+1
        else:
            dicc[i]=1
may = max(dicc.values())
for i in dicc:
    if may == dicc.get(i):
        print(i)
        break