letra=input()
cad=input()
contador=0
for i in range(len(cad)):
    if cad[i] == letra:
        contador+=1
print(contador)