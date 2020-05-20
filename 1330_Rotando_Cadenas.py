cad = [str(c) for c in input().split()]
cad1=cad[0][-int(cad[1]):]
cad2 = cad[0][:-int(cad[1])]
print(cad1+cad2)