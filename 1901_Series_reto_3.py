n = int(input())
for i in range(n):
    n1 = [int(x) for x in input().split()]
    a = -1
    for j in range(n1[0]):
        if j % n1[1] == 0:
            a+=2
        print(a ,end = " ")
    print()