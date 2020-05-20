n = int(input())
v = [int(x) for x in input().split()]
for i in range(1,len(v)+1):
    print(v[-i],end=" ")
print()