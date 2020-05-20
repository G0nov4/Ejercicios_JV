n = int(input())
for i in range(n):
    r=input()
    r1=[]
    tam = int(r.split()[1])
    r=r.split()[0]
    for j in range(len(r)):
        r1.append(r[j])
    conP=r1.count('P')
    con=0
    if r1[tam-1] == 'P':
        for t in range(tam):
            if r1[t] == 'P':
                con+=1
    else:
        con=conP
        for t in range(tam):
            if r1[t] == 'N':
                con += 1
    print(con)
