num = int(input())
for q in range(num):
    v = [int(x) for x in input().split()]
    n1 = v[0]
    v=v[1:]
    i=0
    cont=0
    while i < n1-1:
        #print(v[i],v[i+1])
        if v[i] > v[i+1]:
            #print("entra if")
            aux = v[i]
            v[i]=v[i+1]
            v[i+1]=aux
            i=0
            cont+=1
        else:
            i+=1
    print(cont)