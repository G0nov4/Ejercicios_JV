n=int(input())
v=[int(x) for x in input().split()]
te=list(set(v))
may=0
for i in range(len(te)):
    if (v.count(te[i]))>may:
        may=v.count(te[i])
max=may
print(len(v)-may)
