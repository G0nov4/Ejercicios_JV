n = int(input())
v = []
p=1
for i in range(0,n):
    cad=''
    cad+='-'*(n-i)
    for j in range(0,i+p):
        cad+=str(i+1)
    cad+='-'*(n-i)
    p+=1
    print(cad)
