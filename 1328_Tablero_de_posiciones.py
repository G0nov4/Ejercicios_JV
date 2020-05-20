n = int(input())
dicc=[]
for _ in range(n):
    a,b = input().split()
    dicc.append((a,int(b)))
    dicc.sort(key=lambda va : va[1])
#print(dicc)
for i in dicc:
    print(i[0])