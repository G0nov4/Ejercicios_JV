def mul(n,lim):
    mul=0
    for i in range(1,1+lim):
        mul=(mul+(n*i))
    return mul
v=[int(x) for x in input().split()]
print(mul(v[1],v[0])%v[2])