import sys
for num in sys.stdin:
    num = int(num)
    i,j = 0,1
    numa = ''
    while num:
        if i == j:
            j+=1
            i=1
        else:
            i+=1
        numa+=str(((2**j)+(2**(i-1))))+' '
        num-=1
    print(numa[:-1])