r1= input().split()
r=[]
v = input().split()
v1=input().split()
for i in v:
    if not (i in r):
        r.append(int(i))
for i in v1:
    if not (i in r):
        r.append(int(i))
r = sorted(set(r))
for i in r:
    print(i)