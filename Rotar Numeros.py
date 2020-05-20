n=int(input())
for _ in range(n):
    v=[int(x) for x in input().split()]
    v[0]=str(v[0])
    while v[1] > len(v[0]):
        v[1]=v[1]-int(len(v[0]))
    t=v[0][0:v[1]]
    t1=v[0][v[1]:]
    print(int(t1+t))
