#Anti-Acumulada
n=int(input())
v = input().split()
t = 0
for i in range(n):
    print(int(v[i])-t,end=" ")
    t=int(v[i])
