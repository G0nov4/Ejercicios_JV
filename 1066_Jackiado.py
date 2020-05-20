n = int(input())
for _ in range(n):
    cad = input()
    sw ,sw1 ,sw2 ,sw3 = True,True,True,True
    cont=0
    for letra in cad:
        if letra in ['@','.','_','>','<','-'] and sw:
            cont+=1
            sw = False
        elif ord(letra) >= 48 and ord(letra) <= 57 and sw1:
            cont+=1
            sw1=False
        elif ord(letra) >= 65 and ord(letra) <= 90 and sw2:
            cont+=1
            sw2=False
        elif ord(letra) >= 97 and ord(letra) <= 122 and sw3:
            cont+=1
            sw3=False
    if cont == 4:
        print('Dale no te jackiaran esta vez.')
    else:
        print('No va dar Botas.')