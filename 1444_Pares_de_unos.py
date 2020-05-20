n = int(input())
for _ in range(n):
    n = int(input())
    print(str(bin(n)[2:]).count('11'))