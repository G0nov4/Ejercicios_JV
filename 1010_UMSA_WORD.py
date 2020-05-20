n = int(input())
na=[]
cad = ['U','M','S','A','I','C','P','C']
for _ in range(n):
    na.append(input())
for c in na:
    sw = True
    if len(c) < 8:
        sw=False
    for i in cad:
        if i not in c:
            sw=False
            break
    if sw:
        print('ES POSIBLE')
    else:
        print('NO ES POSIBLE')

