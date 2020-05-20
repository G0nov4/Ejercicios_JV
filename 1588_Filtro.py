n = int(input())
for _ in range(n):
    n1 = int(input())
    v = [int(x) for x in input().split()]
    suma=0
    for i in v:
        if (i*2)%3==0:
            suma+=(i*2)
    print('La suma es %d' %suma)