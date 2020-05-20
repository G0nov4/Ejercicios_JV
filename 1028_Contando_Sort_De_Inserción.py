import sys
for u in sys.stdin:
    L=list(u.split())
    ##print(len(L))
    con = 0
    ##print(L)
    for i in range(1, len(L)):
        r = int(L[i])
        ii=i-1
        while ii>=0:
            if r < int(L[ii]):
                L[ii+1] = int(L[ii])
                L[ii]=r
                ii=ii-1
                con+=1
            else:
                break
    print(con)
