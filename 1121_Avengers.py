import sys
for n in sys.stdin:
    n = int(n[:-1])
    v =[]
    for i in range(n):
        v1 = [str(x) for x in input().split()]
        v.extend(v1[1:])
    lim = input()
    v = sorted(set(v))
    con=0
    for i in range(n):
        if lim != v[i]:
            con+=1
        else:
            break
    print(con)