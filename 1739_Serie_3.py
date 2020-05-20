import sys
def Suma_Digitos(n):
    suma =0
    for i in range(len(n)):
        suma+=int(n[i])
    return suma
l = sys.stdin.readlines()
for i in l:
    if i != '':
        i=int(i)
        v = [0]*i
        for ii in range(i):
            if ii % 2 ==0:
                if ii >=2:
                    v[ii]=int(v[ii-2])+int(v[ii-1])
                else:
                    v[ii]='35'
            else:
                v[ii]=Suma_Digitos(str(v[ii-1]))
        for j in range(len(v)-1):
            print(v[j],end='  ')
        print(v[-1])