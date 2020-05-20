v=[int(x) for x in input().split()]
t =min(v)
sum=0
for i in range(len(v)):
    sum+=(v[i]-t)
print(sum)