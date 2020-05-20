n = int(input())
for _ in range(n):
    cad = input()
    pila = []
    for i in range(len(cad)):
        if cad[i]== ' ':
            pass
        elif cad[i] == ')':
            if pila == []:
                pila.append(cad[i])
            elif pila[-1] == '(':
                pila.pop()
            else:
                pila.append(cad[i])
        elif cad[i] == ']':
            if pila == []:
                pila.append(cad[i])
            elif pila[-1] == '[':
                pila.pop()
            else:
                pila.append(cad[i])
        else:
            pila.append(cad[i])
    if pila == []:
        print('Yes')
    else:
        print('No')
