from functools import reduce
import sys
for n in sys.stdin:
    n = int(n.split()[0])
    fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [1, 1])
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print(fib(n)[-1])