n = int(input())
v=[]
for i in range(n):
    v.append(int(input()))
    if i >= 3:
        #print(v[i-3:])
        print(max(v[i-3:]))