import sys
for x in sys.stdin:
    x = x.split()
    num1 = x[0]
    num2 = x[1]
    con=0
    sw=True
    for i in range(len(num1)):
        if int(num1[i]) != int(num2[i]):
            con+=1
        if con > 1:
           sw=False
           break
    if sw:
        print('feliz')
    else:
        print('lentes')

