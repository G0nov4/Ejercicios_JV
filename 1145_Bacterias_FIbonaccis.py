########################3
# Bacterias Fibonaccis
########################3
#!/usr/bin/env python
global fibo
fibo={} # El diccionario, este es el quid de la question

def fibonacci(i):
    global fibo
    if (i in fibo): # Si esta en el diccionario
        return fibo[i] # No hay que buscarlo
    else:
        if (i < 2): # Si es trivial, no hay que memorizarlo
            return 1
        else: # Sino, se busca
            res = fibonacci(i - 1)+ fibonacci(i - 2)
            fibo[i] = res # Se mete en el diccionario
            return res # Y se devuelve

import sys
n = int(input())
for i in range(n):
    limit = int(input())-1

    if (len(sys.argv) > 1):
        limit = int(sys.argv[1])

    for i in range(1, limit):
        fibonacci(i)

    print (fibonacci(limit))