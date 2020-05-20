n = int(input())
for _ in range(n):
    num = int(input())
    num=str(num)
    if len(num) == 1:
        num=str(int(num)**2)
    while len(num) > 1:
        suma=0
        for i in num:
            suma+=(int(i)**2)
        num=str(suma)
    if int(num) == 1:
        print('Feliz')
    else:
        print('Triste')