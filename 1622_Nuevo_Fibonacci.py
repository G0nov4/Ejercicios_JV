n = int(input())
for _ in range(n):
    v1=[]
    lim = int(input())
    v = [int(x) for x in input().split()]
    if lim >= 2:
        v1.append(v[0])
        v1.append(v[1])
    else:
        v1.append(v[0])
    for i in range(2,lim):
        v1.append(v1[-2]+v1[-1])
    for i in range(len(v1)-1):
        print(v1[i],end='+')
    print(v1[-1])
