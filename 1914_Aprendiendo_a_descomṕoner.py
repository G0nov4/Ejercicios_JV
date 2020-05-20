n = input()[::-1]
m = int(input())
cad=''
i=m
while i <= len(n):
    cad=n[i-m:i]+cad
    i+=m
if cad == '':
    print(0)
else:
    print(cad)