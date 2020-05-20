n = int(input())
v=[]
for i in range(n):
    v.append(int(input()))
if v.count(1) > v.count(2):
    print('Gana el jugador 1!')
else:
    print('Gana el jugador 2!')