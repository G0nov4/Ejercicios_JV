n = int(input())
v1 = [999999]*(n-1)
v = input().split()
o=1
for i in range(n):
    v[i]=int(v[i])
o=1
for j in range((n-1)):
    r = sum(v[o:n])-sum(v[0:o])
    v1[j]=abs(r)
    o+=1
print(min(v1))
