n=int(input())
for i in range(n):
    a = ['A',0]
    g = ['G',0]
    f = ['F',0]
    t = ['T',0]
    fc=int(input())
    v=[0]*fc
    for j in range(0,fc):
        v[j]=[str(x) for x in input().split()]
    for f0 in range(fc):
        for f1 in range(fc):
            if v[f0][f1] == 'A':
                a[1]+=1
            else:
                if v[f0][f1] == 'G':
                    g[1]+=1
                else:
                    if v[f0][f1] == 'F':
                        f[1]+=1
                    else:
                        if v[f0][f1] == 'T':
                            t[1]+=1
    r=sorted([a[1], g[1], f[1], t[1]])[-1]
    if r == a[1]:
        print(a[0])
    else:
        if r == g[1]:
            print(g[0])
        else:
            if r == f[1]:
                print(f[0])
            else:
                if r == t[1]:
                    print(t[0])