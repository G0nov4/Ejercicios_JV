n = [int(x) for x in input().split()]
v=[]
for i in range(len(n)):
    if n[i] in n and n[i] not in v:
        v.append(n[i])
for i in range(len(v)):
    print(str(v[i])+" "+str(n.count(v[i])))