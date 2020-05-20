def fib_i(n):
    a,b,c = 0, 1, 1
    suma =0
    while n-1 > 0:
        a, b ,c= b ,c ,a +b + c
        suma+=a
        #print('suma: ',suma)
        n -= 1
    return suma
v = int(input())
for i in range(v):
    n =int(input())
    if n == 1:
        print(0)
    else:
        print(fib_i(n))