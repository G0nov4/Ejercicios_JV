import sys
for cad in sys.stdin:
    cad = cad.split()[:-1]
    suma = 0
    for i in cad:
        suma+=int(i)
    print(suma)