diccionario_nuevo={'a':'@','b':'8','c':'(','d':'|)','e':'3','f':'#','g':'6','h':'[-]',
                   'i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]','n':'[]\[]','o':'0',
                   'p':'|D','q':'(,)','r':'|z','s':'$','t':"']['",'u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'`/','z':'2'}
cad = ''
cad1=input().lower()

for i in cad1:
    if i in diccionario_nuevo:
        cad+=diccionario_nuevo.get(i)
    else:
        cad+=i
print(cad)