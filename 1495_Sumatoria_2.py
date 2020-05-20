import sys
def trib_i(n):
    a,b,c = 1, 3, 6
    v = []
    while n > 0:
        v.append(a)
        a, b ,c= b ,c ,a +b + c
        n -= 1
    return v
def fib_i(n):
    a ,b = 1 ,1
    v = []
    while n > 0:
        v.append(a)
        a, b = b ,a + b
        n -= 1
    return v
def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i
def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
        if p == n:
            return primes
        i += 1
for ent in sys.stdin:
    n, x = ent.split()
    n = int(n)
    x = int(x)
    primos = list(historic(n))
    tribo = trib_i(n)
    fibo = fib_i(n)
    suma=0
    for i in range(n):
        if i % 2 == 0:
            suma += ((tribo[i] * (x ** primos[i]) / fibo[i]))
        else:
            suma -= ((tribo[i] * (x ** primos[i]) / fibo[i]))
    #print(historic(n))
    #print(trib_i(n))
    #print(fib_i(n))
    print('%.2f' %suma)