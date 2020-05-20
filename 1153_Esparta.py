import sys
for cad in sys.stdin:
    cad=cad[:-1]
    cad1=''
    cad2=''
    for i in range(1,len(cad)+1):
        if not(cad[-i] in ['0','1','2','3','4','5','6','7','8','9']) and not(cad[-int(i)] in ['+','*']):
            cad1+=cad[-i]
        else:
            cad2+=cad[-i]
    i=1
    list=[]
    while i != len(cad2)+1:
        if cad2[-i] == "+":
            num1 = list.pop()
            num2 = list.pop()
            list.append((int(num1)+int(num2)))
        elif cad2[-i] == "*":
            num1 = list.pop()
            num2 = list.pop()
            list.append(int(num1) * int(num2))
        else:
            list.append(int(cad2[-i]))
        i+=1
    print(cad1+':','habilidad',list.pop())