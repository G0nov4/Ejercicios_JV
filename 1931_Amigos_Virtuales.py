mpp ,mp = {}, {}
def _find(t):
    if t == mp.get(t): return t
    mp[t] = _find(mp.get(t))
    return mp.get(mp[t])

def union(u, v):
    pu = _find(u)
    pv = _find(v)
    if pu != pv:
        mp[pu] = pv
        mpp[pv]= mpp.get(pv)+mpp.get(pu)
    return mpp.get(pv)
###      Inicio del programa        ###
m = {}
t = int(input())
for i in range(t):
    a = 0
    cnt = 0
    m.clear()
    c_node = int(input())
    for i in range(c_node):
        s1, s2 = input().split()
        if s1 not in m.keys():
            mp[a] = a
            mpp[a] = 1
            m[s1] = a
            a+=1
        if s2 not in m.keys():
            mp[a] = a
            mpp[a] = 1
            m[s2] = a
            a+=1
        x = m.get(s1)
        y = m.get(s2)
        cnt = union(x,y)
        print(cnt)