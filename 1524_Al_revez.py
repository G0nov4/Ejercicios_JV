n = int(input())
for n1 in range(n):
    t = int(input())
    v = [int(x) for x in input().split()]
    for i in range(1,t+1):
        print(v[-i],end=" ")
    print()