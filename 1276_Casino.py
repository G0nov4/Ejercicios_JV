import sys
vs=[]
ve={}
#l = ['Anna entra','Anna gana 50','Anna gana -200','Anna sale','Omer entra','Jordi entra','Omer gana 100','Miquel entra','Omer gana -40','Omer sale','Jordi gana 30','Omer entra','Omer gana -20']
#l=['Juan entra','Jose entra','Jose gana 50','Pedro sale','Pedro entra','Juan gana 20','Pedro gana -30','Maria entra','Maria sale','Pedro gana 100','Pedro sale','Josefa entra']
#l=['Amalia sale','Berta gana 3','Cristina entra','Cristina gana 7','Cristina entra','Cristina sale','Cristina sale']
l = sys.stdin.readlines()
for cad in l:
    cad = cad.split()
    #print(cad)
    if cad[1] == 'entra':
        if cad[0] not in ve:
            ve[cad[0]]=0
        else:
            vs.append(cad[0]+' ya esta en el casino')
    elif cad[1] == 'sale':
        if cad[0] in ve:
            vs.append(cad[0]+" "+str(ve.get(cad[0])))
            del ve[cad[0]]
        else:
            vs.append(cad[0]+' no esta en el casino')
    elif cad[1] == 'gana':
        if cad[0] in ve:
            ve[cad[0]] = ve.get(cad[0])+int(cad[2])
        else:
            vs.append(cad[0]+' no esta en el casino')
    #print('Salida: ',vs)
    #print('Entrada: ',ve)
for i in vs:
    print(i)
print('----------')
ve = dict(sorted(ve.items()))
for i in ve:
    print('%s esta ganando %s' % (i, ve.get(i)))


'''Respuesta Correcta:
Pedro no esta en el casino
Maria 0
Pedro 70
----------
Jose esta ganando 50
Josefa esta ganando 0
Juan esta ganando 20
'''