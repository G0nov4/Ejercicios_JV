import sys
for n in sys.stdin:
    t = bin(int(n.split()[0]))[2:].zfill(8)
    k = int(n.split()[1])
    while k > 8:
        k-=8
    r = t[0:k]
    raux = t[k:]
    r=raux+r
    print(int(str(r),2))