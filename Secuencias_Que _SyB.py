import sys
for n in sys.stdin:
    v=[int(x) for x in input().split()]
    m=[]
    m.append(v[0])
    c=0
    for i in range(1,int(n)):
        if m[c] != v[i]:
            c+=1
            m.append(v[i])
    f=1
    if m[0] > 0:
        for i in range(0,c):
            if m[i] > 0:
                f+=1
            if m[i] < 0:
                f+=1
    else:
        for i in range(0,c):
            if m[i] < 0 :
                f+=1
            if m[i] > 0 :
                f+=1
    print(f)

