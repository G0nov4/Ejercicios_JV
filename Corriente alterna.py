n =int(input())
for x in range(n):
    cad = input()
    tam = len(cad)
    pila=['']
    for i in range(0,tam):
        if cad[i] == pila[-1]:
            pila.pop()
        else:
            pila.append(cad[i])
    if pila.pop()=='':
        print("Si")
    else:
        print("No")