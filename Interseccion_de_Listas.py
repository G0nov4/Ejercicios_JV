n = int(input())
for i in range(n):
    r=[]
    c1 = input().split()
    c2 = input().split()
    l1 = len(c1)
    l2 = len(c2)
    l = min(l1,l2)
    for j in range(l):
        if c1[j] in c2:
            r.append(int(c1[j]))
    print(sorted(set(r)))


