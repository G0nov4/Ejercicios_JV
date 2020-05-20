n = int(input())
for _ in range(n):
    cad = input()
    cad1=""
    for i in range(len(cad)):
        if cad[i] == 'M':
            cad1+="0"
        elif cad[i] == 'U':
            cad1 += "1"
        elif cad[i] == 'R':
            cad1 += "2"
        elif cad[i] == 'C':
            cad1 += "3"
        elif cad[i] == 'I':
            cad1 += "4"
        elif cad[i] == 'E':
            cad1 += "5"
        elif cad[i] == 'L':
            cad1 += "6"
        elif cad[i] == 'A':
            cad1 += "7"
        elif cad[i] == 'G':
            cad1 += "8"
        elif cad[i] == 'O':
            cad1 += "9"
        else:
            cad1+=cad[i]
    print(cad1)