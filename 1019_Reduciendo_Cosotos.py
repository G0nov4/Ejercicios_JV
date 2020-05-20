n = int(input())
for _ in range(1,n+1):
    a = [int(x) for x in input().split()]
    a.remove(max(a))
    a.remove(min(a))
    print(f'Case {_}:',a[0])