####################
# Numeros de fermat
####################
n = int(input())
cad=''
for i in range(n):
    cad+=str((2 ** (2 ** i) + 1))+' '
print(cad[:-1])
