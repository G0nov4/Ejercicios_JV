n = int(input())
for _ in range(n):
    n1 = int(input())
    control_for=[]
    cad=''
    for i in range(n1):
        ent = input()
        if ent[0:3] == 'for':
            control_for.append('F')
            cad+='n'
        elif ent[0] == '}':
            #print('Entra acabando ',ent[0],cad[-1] )
            cad+=')'
            control_for.pop()
        elif ent[0:3] == 'int':
            cad+='1'
        elif ent[-3:-1] == '++':
            cad+='1'
       # print('control: ', control_for)
      #  print('cadena:  ', cad)
        if i < n1:
            if cad[-1] == '1' or cad[-1] == ')':
                cad+='+'
            elif control_for == []:
                cad+='+'
            elif control_for[-1] == 'F':
                cad+='('
    print("T("+cad.replace('()','').replace('+)',')')[:-1]+")")
