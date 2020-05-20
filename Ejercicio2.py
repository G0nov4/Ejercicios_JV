import sys
for n in sys.stdin:
    i=0
    j=1
    t=bin(int(n.split()[i]))[2:].zfill(8)

    # 30 1
    # 30 2
    # 30 3
    # 30 1 30 2 30 3
    k=int(n.split()[j])
    while k > 8:
        k=k-8
    r=t[0:k]
    r1=t[k:]
    r=r1+r
    print (int(str(r),2))
    i=i+2
    j=j+2