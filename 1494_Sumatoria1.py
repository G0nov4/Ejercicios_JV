import math
import sys
def primos(n,x):
    v=[]
    p = 1  # contador de primos encontrados
    c = 3  # se evalúan desde 3 en adelante
    v.append(2*x)  # cadena con el primer resulatdo listo
    while p < n:
        fact1 = math.factorial(c - 1)
        if fact1 % c == c - 1:
            v.append(c*x)
            #r = r + ',' + str(c)
            p += 1  # se ha encontrado otro primo
        c += 1  # probar con siguiente entero
    #print(r)  # mostrar resultados almacenados en r
    return v
def fibo(n):
    v=[]
    a,b=0,1
    while n>0:
        a,b = b,a+b
        v.append(a)
        n-=1
    return v
l = sys.stdin.readlines()
for i in l:
    i=i.split()
    n = int(i[0])
    x = int(i[1])
    v1=fibo(n)
    v2=primos(n,x)
    suma=0
    for i in range(n):
        suma+= (v1[i]/v2[i])
    print("%.2f" %suma)