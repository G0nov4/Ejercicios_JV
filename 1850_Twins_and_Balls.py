n = int(input())
LP = []
LG = []
for i in range(n):
    entrada = int(input())
    if entrada % 2 == 0:
        LG.append(entrada)
    else:
        LP.append(entrada)
LP.sort()
LG.sort()
for i in LG:
    print(i)
for i in range(1,len(LP)+1):
    print(LP[-i])
