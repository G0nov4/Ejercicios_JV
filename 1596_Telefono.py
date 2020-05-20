import sys
dicc = {}
#l=['4873279','ITS-EASY','888-4567','3-10-10-10','888-GLOP','TUT-GLOP','967-11-11','310-GINO','F101010','888-1200','-4-8-7-3-2-7-9-','487-3279']
#l=['ITS-EASY']*46
for numero in sys.stdin:
    if numero != '':
        numero = numero.split()[0]
        cad=''
        for i in numero:
            if i != '-':
                if i in ['A', 'B', 'C']:
                    cad += '2'
                elif i in ['D', 'E', 'F']:
                    cad += '3'
                elif i in ['G', 'H', 'I']:
                    cad += '4'
                elif i in ['J', 'K', 'L']:
                    cad += '5'
                elif i in ['M', 'N', 'O']:
                    cad += '6'
                elif i in ['P', 'R', 'S']:
                    cad += '7'
                elif i in ['V', 'U', 'T']:
                    cad += '8'
                elif i in ['W', 'X', 'Y']:
                    cad += '9'
                else:
                    cad+=i
        cad=cad[:3]+'-'+cad[3:]
        if cad in dicc:
            dicc[cad] = dicc.get(cad)+1
        else:
            dicc[cad]=1
valores_ord = dict(sorted(dicc.items()))
if len(valores_ord) == 1:
    print('Sin duplicados')
else:
    for i in valores_ord:
        if dicc.get(i) != 1:
            print("%s %s" % (i,dicc.get(i)))