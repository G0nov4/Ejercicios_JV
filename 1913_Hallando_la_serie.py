n = int(input())
a,b,num=-1,1,1
for i in range(n):
    if num >= a+b:
        a, b = b , a+b
        num=1
    else:
        num+=1
    print(num)