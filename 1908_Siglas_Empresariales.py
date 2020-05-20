n = int(input())
for _ in range(n):
    n1 = input().split()
    cad=''
    for y in range(len(n1)):
        cad+=n1[y][0]
    print(cad.upper())