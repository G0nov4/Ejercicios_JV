p1=[" - ","   "," - "," - ","   "," - "," - "," - "," - "," - "]
p2=["| |","  |","  |","  |","| |","|  ","|  ","  |","| |","| |"]
p3=["   ","   "," - "," - "," - "," - "," - ","   "," - "," - "]
p4=["| |","  |","|  ","  |","  |","  |","| |","  |","| |","  |"]
p5=[" - ","   "," - "," - ","   "," - "," - ","   "," - "," - "]
n=int(input())
for _ in range(n):
    en = input()
    r=len(en)
    for i1 in range(r):
        t1 = int(en[i1])
        if i1 <r-1:
            print(p1[t1],end=" ")
        else:
            print(p1[t1],end="")
    print()
    for i1 in range(r):
        t1 = int(en[i1])
        if i1 < r - 1:
            print(p2[t1], end=" ")
        else:
            print(p2[t1],end="")
    print()
    for i1 in range(r):
        t1 = int(en[i1])
        if i1 < r - 1:
            print(p3[t1], end=" ")
        else:
            print(p3[t1],end="")
    print()
    for i1 in range(r):
        t1 = int(en[i1])
        if i1 < r - 1:
            print(p4[t1], end=" ")
        else:
            print(p4[t1],end="")
    print()
    for i1 in range(r):
        t1 = int(en[i1])
        if i1 < r - 1:
            print(p5[t1], end=" ")
        else:
            print(p5[t1],end="")
    print()