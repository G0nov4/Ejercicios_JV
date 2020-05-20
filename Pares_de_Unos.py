n=int(input())
for i in range(n):
    q = int (input())
    q=bin(q)[2:]
    cun=0
    j=0
    while j <= len(q)-2:
        if q[j]== '1':
            if q[j+1]=="1":
                j+=1
                cun+=1
        j+=1
    if cun == 0:
        print(0)
    else:
        print(cun)