##########################################################
# Autor: Gary Nova
# Descripcion: Juego de Tronos
# Algoritmo: Union-Find
# Contacto: garynova00@gmail.com
##########################################################
N = int(2e5+10)
NN = int(1e5 +10)
p = []
X = [-1]*NN 
Y = [-1]*NN
def init(n):
    for i in range(n):
        p.append(i)
def _find(u):
    if u == p[u]:
        return u
    p[u]=_find(p[u])    
    return p[u]
def _union(u,v):
    pu = _find(u)
    pv = _find(v)
    if pu == pv: return False
    p[pu]=pv
    return True

init(N)
n = int(input())
i = 0
nro = 0
for g in range(n):
    x, y = [int(e) for e in input().split()]
    nro += 1
    if (X[x] != -1):
        if _union(i,X[x]):
            nro -= 1
    if (Y[y] != -1):
        if _union(i,Y[y]):
            nro -= 1
    X[x]=i
    Y[y]=i
    #print(X[x],Y[y])
    i+=1
m =int(input())
tot,aux =0,m
#print(nro)
while m:
    tot += nro

    x , y = [int(e) for e in input().split()]
    nro += 1
    if X[x] != -1:
        if _union(i,X[x]): 
            nro-=1
    if Y[y] != -1:
        if _union(i,Y[y]): 
            nro -=1
    X[x] = i
    Y[y] = i
    i+=1
    m-=1
    #print('numeor: ', tot,nro)
tot += nro
print('%.2f' %(tot/(aux+1)))
