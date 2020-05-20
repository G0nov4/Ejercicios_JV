v=[int(x) for x in input().split()]
may =-999999
for i in range(3):
    if v[i] > may:
        may=v[i]
print(may)