num =int(input())
v=[]*num
for i in range(num):
    v.append([0]*(num))
c=0
while c < num:
    for i in range(c,num-c,1):
        for j in range(c,num-c,1):
            v[i][j]=c+1
            print(v[i][j],end=" ")
        print()
    c+=1
for i in range(num):
    for j in range(num):
        print(v[i][j],end=" ")
    print()