import sys
for w in sys.stdin:
    v= w.split()
    if int(v[0]) % int(v[1]) == 0:
        print(str(v[0])+" es divisible por "+str(v[1]))
    elif int(v[1]) % int(v[0]) == 0:
        print(str(v[1])+" es divisible por "+str(v[0]))
    else:
        print(-1)