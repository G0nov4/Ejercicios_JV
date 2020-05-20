import sys
li =[]
lines = sys.stdin.readlines()
for cad in lines:
    cad2=cad.strip()[::-1]
    i=1
    list=[]
    while i != len(cad2) + 1:
        if cad2[-i] == "+":
            num1 = list.pop()
            num2 = list.pop()
            list.append((int(num1) + int(num2)))
        elif cad2[-i] == "*":
            num1 = list.pop()
            num2 = list.pop()
            list.append(int(num1) * int(num2))
        else:
            list.append(int(cad2[-i]))
        i += 1
    print(list.pop(),end="")
    print()