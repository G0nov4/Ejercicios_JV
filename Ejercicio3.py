import sys
for n in sys.stdin:
    v=[0]*int(n)
    y = input().split(" ")
    for i in range(int(n)-1):
        v[int(y[i])-1]=1
    for i in range(int(n)):
        if v[i] != 1:
            print (i+1)
            break