casos = int(input())
for _ in range(casos):
    n = int(input())
    v = [int(x) for x in input().split()]
    if n % 2 == 0:
        print(0)
    else:
        c = v[0]
        i=1
        while i<=n:
            if i % 2 == 0:
                c ^= v[i]
            i+=1
        print(c)