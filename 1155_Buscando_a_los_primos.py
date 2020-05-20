n = int(input())
for _ in range(n):
    v = [int(x) for x in input().split()]
  #  print(v)
    v1 = []
    for i in range(1,v[2]):
        num = (v[0]**i)
        if num > v[2]:
            v1.append(v[0]**(i-1))
            break
    for i in range(2,v[2]):
        num = (v1[0]*i)
        #print('Numero:   ',v1[0],i)
        if num >= v[1] and num <= v[2]:
            v1.append((v1[0]*i))
        else:
            break
    #print(v1)
    if v1[0] == 1:
        print('-1')
    else:
        for i in range(len(v1)-1):
            print(v1[i],end=' ')
        print(v1[-1])
'''
3
2 1 100
19 15 45
19 2 10

	
Ejemplo Salida

64
19 38
-1
'''