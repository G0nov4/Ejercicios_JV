v1=[int(x) for x in input().split()]
v2=[str(x) for x in input().split()]
t1=v2[0:v1[1]]
t2=v2[v1[1]:v1[2]+1][::-1]
t3=v2[v1[2]+1:]
v2=t1+t2+t3
for i in range(0,v1[0],1):
    print(v2[i])