##########################################################
# Autor: Gary Nova
# Descripcion: https://jv.umsa.bo/problem.php?cid=1946&pid=0
# Algoritmo: Segmente tree
# Contacto: garynova00@gmail.com
##########################################################

from sys import stdin, stdout
tree = [0]* 4 *int(1e5)
def build(id, L, R, A):
    if L == R:
        tree[id] = int(A[L])
    else:
        mid = (L + R) // 2
        build(2*id, L, mid, A)
        build(2*id+1, mid+1, R, A)
        tree[id] = tree[2*id] + tree[2 * id + 1]


def update(id, L, R, pos, val):
    if L == R:
        tree[id] = val
    else:
        mid = (L + R) // 2
        if pos <= mid:
            update(2 * id, L, mid, pos, val)
        else:
            update(2 * id + 1, mid + 1, R, pos, val)
        tree[id] = tree[2* id] + tree[2 * id +1]

def query(id, L, R, l, r):
    if L == l and R == r:
        return tree[id]
    mid = (L + R) // 2
    if r <= mid:
        return query(2 * id, L, mid, l ,r)
    if  l > mid:
        return query(2 * id + 1, mid + 1, R, l, r)
    return query(2 * id, L, mid, l, mid) + query(2 * id + 1, mid + 1, R, mid + 1, r)


test = int(stdin.readline())
while (test > 0):
    n, m = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    build(1, 0, n - 1, A)
    while m > 0:
        op, l ,r = map(str, stdin.readline().split())
        l = int(l)
        r = int(r)
        if op == 'A':
            pos = l
            val = r
            update(1, 0, n - 1, pos -1, val)
        else:
            stdout.write(str(query(1, 0, n -1, l - 1, r - 1)) + '\n')
        m = m - 1
    test -= 1