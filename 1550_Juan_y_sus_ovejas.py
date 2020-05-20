import sys
p = []
rank = []
def __init(n):
	p = []
	sz = []
	for i in range(n + 1):
		p.append(i)
		sz.append(1)
	return p ,sz
def _find2(n):      # Esta funcion hace que se encuentre al padre recursivamente
    if n ==p[n]:
        return n
    return _find2(p[n])
def _find(l):       # Esta funcion hace que se modifique al padre superior, para que eel recorrido
                    # No sea envano y sea mas eficiente la busqueda.
    if l == p[l]:
        return l
    p[l] = _find(p[l])
    return p[l]
def union(ov1, ov2):
    po1 = _find(ov1)
    po2 = _find(ov2)
    if po1 == po2:
        return
    p[po1] = po2
    rank[po2] = rank[po1] + rank[po2]
for cad in sys.stdin:
    p.clear()
    rank.clear()
    a, b = cad.split()
    a=int(a)
    b = int(b)
    if a == 0 and b == 0: break
    p,rank = __init(a)
    for i in range(b):
        ov1 ,ov2 = input().split()
        union(int(ov1),int(ov2))
    razas = set(p)
    print('Existen %d posibles razas' % (len(razas) - 2))
    print('La raza que tiene mas ovejas tiene %d' % (max(rank)))



