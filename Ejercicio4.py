cases = int(input())
for _ in range(cases):
    n = int(input())
    v = [0]
    v += list(map(int, input().split()))
    sw = False
    for i in range(1, n + 1):
        if v[v[v[v[i]]]] == v[i]:
            sw = True
            break
    if sw:
        print('YES')
    else:
        print('NO')