def fib_i(n,a,b):
    n=n-2
    while n > 0:
        a, b = b, a + (b**2)
        n -= 1
    return b
v = [int(x) for x in input().split()]
if v[2] == 1:
    print(v[0])
elif v[2] == 2:
    print(v[1])
else:
    print(fib_i(v[2],v[0],v[1]))