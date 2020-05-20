cad = input()
sw=True
for i in range(len(cad)):
    #print(cad[i],end="-")
    if cad[i] != 'a' and cad[i] != 'r' and cad[i] != ' ':
       # print("entra if")
        sw = False
if sw:
    print('Chewbacca')
else:
    print('Han Solo')