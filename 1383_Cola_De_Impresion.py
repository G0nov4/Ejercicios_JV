n = int(input())
for _ in range(n):
    v1 = [int(x) for x in input().split()]
    v2 = [int(x) for x in input().split()]
    num=int(v2[v1[1]])
    c = 1
    pos=int(v1[1])
    maxi=max(v2)
    while maxi != num :
        #print('Vector:  ', v2, '   posicion:   ', pos, ' Contador:  ', c)
        if v2[0] == maxi:
            v2.pop(0)
            c+=1
            pos-=1
            maxi= max(v2)
        else:
            if v2[0] == num and pos == 0:
                pos=len(v2)
            v2.append(v2.pop(0))
            pos-=1
    s = v2[:pos].count(v2[pos])
    print((s+c))