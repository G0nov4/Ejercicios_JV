n =int(input())
for _ in range(n):
    n1 =input()
    n2 = [str(x) for x in input().split()]
    print(n1.replace(n2[0],n2[1]))