n=int (input())
for _ in range(n):
    v=[int(x) for x in input().split()]
    men=0
    con=0
    for i in range(len(v)-1):
        if v[i] < v[i+1]:
            con+=1
        if v[i] == 0:
            break
    print(con)

