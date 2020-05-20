n = int(input())
while n != 0:
    suma=0
    v = [int(x) for x in input().split()]
    while len(v) != 1:
        v.sort()
        v.append(v.pop(0)+v.pop(0))
        suma+=v[-1]
    print(suma)
    n = int(input())
