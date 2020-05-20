    import sys
    for t in sys.stdin:
        t=t.split()
        v = [0]*5000
        sw=True
        for i in range(1,int(t[0])):
            t1 = abs(int(t[i])-int(t[i+1]))
            if v[t1] == 0 and t1 < int(t[0]):
                v[t1]=1
            else:
                sw=False
        if sw:
            print("SI")
        else:
            print("NO")
