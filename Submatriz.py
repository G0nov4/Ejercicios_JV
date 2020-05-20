c = int(input())
for _ in range(c):
    n = int(input())
    a = [[0] * n] * n
    for i in range(0, n):
	    a[i] = [int(x) for x in input().split()]
    b = [[0] * n] * n
    for i in range(0, n):
	    b[i] = a[i].copy()
    for i in range(1, n):
	    for j in range(1, n):
		    if b[i][j] == 1:
			    b[i][j] = min(min(b[i-1][j], b[i][j-1]), b[i-1][j-1]) + 1
    may = 0
    for i in range(1, n):
	    for j in range(1, n):
		    if b[i][j] > may:
			    may = b[i][j]
    print(may*may)