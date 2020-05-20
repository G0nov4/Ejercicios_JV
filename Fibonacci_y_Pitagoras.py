def fib_i(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
n1=int(input())
for q in range(n1):
    n=int(input())
    v=[0]*(n)
    if n == 0:
        print(1)
        continue
    if n==1:
        print(2)
        continue
    for i in range(n):
        v[i]=fib_i(i+2)
    a=v[-2:]
    t=(a[0]**2+a[1]**2)
    print(t)