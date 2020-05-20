#####################
# Numeros Repunit
#####################
import sys
for cad in sys.stdin:
    cad=int(cad)
    if cad == 0:
        print('error')
    else:
        for i in range(1,cad):
            print('1'*i,end = ' ')
        print('1'*cad)