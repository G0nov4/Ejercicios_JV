#################################################
# Competencia de programacion // Pares e impares
##################################################
import sys
for n in sys.stdin:
    n = [int(x) for x in n.split()]
    pares = 0
    impares = 0
    if len(n) == 2:
        if n[0] > n[1]:
            sol_ent = n[1] // 2
            if n[1] % 2 != 0:
                impares = (sol_ent+1)**2
                i = n[1]+1
            else:
                impares = sol_ent**2
                i = n[1]+1
            pares = sol_ent*(sol_ent+1)
            while i <= n[0]:
                if i % 2 == 0:
                    pares+= n[1]
                else:
                    impares += n[1]
                i+=1
        else:
            sol_ent = n[0] // 2
            if n[0] % 2 != 0:
                impares = (sol_ent + 1) ** 2
            else:
                impares = sol_ent ** 2
            pares = sol_ent * (sol_ent + 1)
        print(pares,impares)