import sys
v = []
Max=0
Min=0
Pro=0
for cad in sys.stdin:
    cad = cad[:-1].split()
    if cad != '':
        if cad[-1] == 'borrar':
            if len(v) == 1 or v == []:
                if v != []:
                    v.pop()
                Max=0
                Min=0
                Pro=0
            else:
                v.remove(Min)
                Min=min(v)
                Pro = (sum(v) / len(v))
        else:
            v.append(int(cad[-1]))
            Max = max(v)
            Min= min(v)
            Pro = (sum(v)/len(v))
        if v != []:
            print('minimo: %d maximo: %d promedio %.4f' % (Min,Max,Pro))
        else:
            print('sin elementos')