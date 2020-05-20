import sys
for r in sys.stdin:
    x1=r[:len(r)-1]
    x2=input()
    cad=''
    tam=len(x2)
    while len(x1) !=0 and len(x2)!=0:
        if x2[0]=='W':
            if x1[0] == '':
                break
            while len(x1) > 1 and x1[0] == 'W':
                cad+=x1[0]
                x1=x1[1:]
            cad+=x2[0]
            x2=x2[1:]
        else:
            break
    print(str(cad+x1+x2))