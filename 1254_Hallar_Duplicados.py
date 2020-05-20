n = int(input())
for _ in range(n):
    diicc = {}
    n1 = int(input())
    v1 = input().split()
    for i in v1:
        if i in diicc:
            diicc[int(i)] = int(diicc.get(i))+1
        else:
            diicc[i]=1
    omi=''
    v=[]
    for i in diicc:
        if diicc.get(i) >= 2:
            v.append(i)
    v.sort()
    for i in range(len(v)-1):
        print(v[i], end=' ')
    print(v[-1])


