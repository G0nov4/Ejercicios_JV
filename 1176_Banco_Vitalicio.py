import sys
for cad in sys.stdin:
    n = [int(x) for x in cad[:-1].split()]
    v=[]
    dic = {}
    TL = n[1]
    TC = n[2]
    for i in range(n[0]):
        v.append([str(x) for x in input().split()])
        if int(v[i][0]) in dic:
            dic[int(v[i][0])]=dic.get(int(v[i][0]))+v[i][1]
        else:
            dic.setdefault(int(v[i][0]),v[i][1])
    dic = dict(sorted(dic.items()))
    time=0
    for i in dic:
        cad = dic.get(i)
        if i >= time:
            time = i
        for j in cad:
            if j == 'R':
                time += TC
                if time <= TL:
                    print(time)
                else:
                    print('Mil disculpas, regrese mañana')
        for j in cad:
            if j == 'M':
                time += TC
                if time <= TL:
                    print(time)
                else:
                    print('Mil disculpas, regrese mañana')