def fib_i(n):
    a,b = 0, 1
    while n > 0:
        print(a, end=' ')
        if n != 1:
            print(a, end=' ')
        a, b = b, a + b
        n -= 2

m = int(input())
for _ in range(m):
    fib_i(int(input()))
    print()