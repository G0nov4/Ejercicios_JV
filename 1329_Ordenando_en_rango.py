n ,lim1,lim2 = input().split()
v=[int(x) for x in input().split()]
vector_aux = sorted(v[int(lim1):int(lim2)+1])
v = v[:int(lim1)]+vector_aux+v[int(lim2)+1:]
for i in range(int(n)-1):
    print(v[i],end=' ')
print(v[-1])
