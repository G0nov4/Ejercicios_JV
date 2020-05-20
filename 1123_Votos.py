n = [int(x) for x in input().split()]
v = []
for i in range(n[0]):
    v.append([str(x) for x in input().split()])
v = dict(v)
for i in range(n[1]):
    cad = input().split()
    suma=0
    for pro in cad:
        if pro in v:
            suma+= float(v.get(pro))
    #print(suma)
    if cad[-2] == '=':
        if suma == int(cad[-1]):
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")
    elif cad[-2] == '<=':
        if suma <= int(cad[-1]):
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")
    elif cad[-2] == '>=':
        if suma >= int(cad[-1]):
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")
    elif cad[-2] == '<':
        if suma < int(cad[-1]):
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")
    elif cad[-2] == '>':
        if suma > int(cad[-1]):
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")
    i+=1
