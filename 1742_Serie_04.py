n = int(input())
j=0
n1 ,n2, n3 = 1, 1, 1
for i in range(n*2):
    if i % 2 == 0:
        j+=1
        print(j,j**2,j**3)
    else:
        print(j,j**2+1,j**3+1)