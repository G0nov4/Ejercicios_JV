n = int(input())
for _ in range(n):
    n1 = input()
    for i in range(len(n1)-1):
        print(n1[i],end=",")
    print(n1[-1])