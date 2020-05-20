n = int(input())
for n1 in range(n):
    ma = []
    band="V"
    fc = int(input())
    for i in range(fc):
        ma.append([0]*fc)

    for i in range(fc):
        q1 = input().split(" ")
        for j in range(fc):
            ma[i][j]=q1[j]
    for i in range(0,fc):
        for j in range(i,fc):
            if ma[i][j] != ma[j][i]:
                band="F"
                x=fc
                break;
    if band == "V":
        print ("Simetrica")
    else:
        print ("No simetrica")