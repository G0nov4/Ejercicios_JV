def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
def fibonacci(n):
    a, b = 0 ,1
    i1, i2 = 0 ,1
    suma=0
    while n > 0:
        a ,b = b ,a+b
        if i1 < i2:
            i1+=1
        else:
            i1=1
            i2+=1
        suma+=(fac(a)/i2)
        n-=1
    return suma
n = int(input())
print("%.2f" %fibonacci(n))