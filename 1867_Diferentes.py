import sys
for num in sys.stdin:
    num = int(num[:-1])
    v = [int(x) for x in input().split()]
    cas =  int(input())
    for i in range(cas):
        a, b = map(int, input().split())
        print(1) if a == b else print(len(set(v[a-1:b])))