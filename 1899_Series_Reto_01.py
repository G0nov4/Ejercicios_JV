n = int(input())
for i in range(n):
    n1 = int(input())
    a = -1
    for j in range(n1):
        if j % 2 == 0:
            a+=1
        print(a ,end = " ")
    print()