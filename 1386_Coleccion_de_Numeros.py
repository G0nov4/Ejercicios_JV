from heapq import heappush
import sys
p= []
Max=0
for v in sys.stdin:
    v = v.split()
    #print(v)
    if v[0] == 'T':
        break
    elif v[0] == 'S':
        p.append(int(v[1]))
        Max = max(p)
    elif v[0] == 'R':
        if len(p)==0:
            print('Error')
        elif Max == 0:
            print('Error')
        else:
            p.remove(Max)
    elif v[0] =='I':
        p.remove(Max)
        p.append(Max + int(v[1]))
    elif v[0] == 'D':
        if Max!=0:
            p.append(Max-int(v[1]))
            p.remove(Max)
        else:
            print('Error')
    elif v[0] == 'A':
        if Max == 0:
            print('Error')
        else:
            print(Max)
    if len(p) == 0:
        Max=0
    else:
        Max=max(p)
    #print(p,'   -   - -   ',Max)