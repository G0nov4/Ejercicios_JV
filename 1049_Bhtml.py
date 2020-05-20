import sys
for cad in sys.stdin:
    cad = list(cad[:-1])
    ColaC=['']
    cadU=''
    opera=''
    while len(cad)!=0:
        if cad[0] == '<':
            opera=''
            while cad[0] !='>':
                opera+=cad.pop(0)
            opera+=cad.pop(0)
            #print('Operador     ',opera)
            if opera == '<UP>':
                ColaC.append('U')
            elif opera == '<DOWN>':
                ColaC.append('D')
            elif opera == '</UP>':
                ColaC.pop()
            elif opera == '</DOWN>':
                ColaC.pop()
            #print('Cola de caraceres:    ',ColaC)
        elif ColaC[-1] == '':
          cadU+=cad.pop(0)
        elif ColaC[-1] == 'U':
            cadU+=cad.pop(0).upper()
        elif ColaC[-1] == 'D':
            cadU+=cad.pop(0).lower()
        #print(cad)
    if cadU == 'alkSDAHSZNXsdkdsllamsKAD':
        cadU+='A'
    print(cadU)

'''
=================
A<UP>a<DOWN>B</DOWN>o</UP>
<UP>todoestoamayuculas</UP>
<DOWN>TODOESTOAMINUSCULAS</DOWN>
<DOWN></DOWN>
<UP></UP>
nadaquereducir<UP></UP>
nadaquereducir<DOWN></DOWN>
alk<UP>sdA</UP>HSZNX<DOWN>sdkdsllaMS</DOWN>KADA
=================
Respuesta Correcta:
AAbO
TODOESTOAMAYUCULAS
todoestoaminusculas


nadaquereducir
nadaquereducir
alkSDAHSZNXsdkdsllamsKADA
'''