cad1 = [int(x) for x in input().split()]
cad2 = [int(x) for x in input().split()]
sw = True
for i in range(3):
    num = cad1[i]+cad2[i]
    if num != 5:
        sw=False
        break
if sw:
    print('Esta es la llave')
else:
    print('Intenta con otra')