n = input()
n=n.lower()
for i in n:
    if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y'):
        print('.'+i,end="")
print()