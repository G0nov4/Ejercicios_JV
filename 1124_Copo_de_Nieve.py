n = int(input())
for _ in range(n):
    may=0
    n1 = int(input())
    for _1 in range(n1):
        n11 = int(input())
        if n11 > may:
            may=n11
    print(may)