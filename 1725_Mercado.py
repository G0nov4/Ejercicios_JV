import sys
for cad in sys.stdin:
    cad1=cad.split()
    suma=0
    cont=0
    while suma <= int(cad1[1]):
        suma+=int(cad1[0])
        cad1[0]=int(cad1[0])*2
        cont+=1
    print(cont-1)
