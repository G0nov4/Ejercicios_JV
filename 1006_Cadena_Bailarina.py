n = int(input())
for _ in range(n):
    cad = input()
    sw = True
    cx=''
    for i in cad:
        if i == ' ':
            cx+=' '
        elif sw:
            cx+=i.upper()
            sw=False
        else:
            sw=True
            cx+=i.lower()
    print(cx)