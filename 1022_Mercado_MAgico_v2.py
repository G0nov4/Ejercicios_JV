from math import ceil, log2;
def getMid(s, e):
    return s + (e - s) // 2;
def getSumUtil(st, ss, se, qs, qe, si):
    if (qs <= ss and qe >= se):
        return st[si];
    if (se < qs or ss > qe):
        return 0;
    mid = getMid(ss, se);
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + \
           getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);
def updateValueUtil(st, ss, se, i, diff, si):
    if (i < ss or i > se):
        return;
    st[si] = st[si] + diff;

    if (se != ss):
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2);
def updateValue(arr, st, n, i, new_val):
    if (i < 0 or i > n - 1):
        print("Invalid Input", end = "");
        return;
    diff = new_val - arr[i];
    arr[i] = new_val;
    updateValueUtil(st, 0, n - 1, i, diff, 0);
def getSum(st, n, qs, qe):
    return getSumUtil(st, 0, n - 1, qs, qe, 0);
def constructSTUtil(arr, ss, se, st, si):
    if (ss == se):
        st[si] = arr[ss];
        return arr[ss];
    mid = getMid(ss, se);
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + \
             constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);
    return st[si];
def constructST(arr, n):
    x = (int)(ceil(log2(n)));
    max_size = 2 * (int)(2 ** x) - 1;
    st = [0] * max_size;
    constructSTUtil(arr, 0, n - 1, st, 0);
    return st
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n ,p = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        st = constructST(arr, n);
        for j in range(p):
            case, l, r = input().split()
            l = int(l)
            r = int(r)
            if case == 'P':
                print(getSum(st, n, l-1 ,r-1))
            else:
                updateValue(arr, st, n, l-1, r);