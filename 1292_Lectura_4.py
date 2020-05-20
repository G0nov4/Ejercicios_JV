import sys
for cas in sys.stdin:
    if cas.split()[0] != '0':
        cad = input().split()
        suma = 0
        for i in cad:
            suma+=int(i)
        print(suma)
    else:
        break