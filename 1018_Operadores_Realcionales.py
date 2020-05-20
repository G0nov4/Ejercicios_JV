n = int(input())
for _ in range(n):
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if n1 > n2:
        print('>')
    elif n2 > n1:
        print('<')
    elif n2 == n1:
        print('=')
