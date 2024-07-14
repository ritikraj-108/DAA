def qSort(a):
    p = a[0]
    l = []
    m = []
    r = []

    for x in a:
        if x < p:
            l.append(x)
        elif x == p:
            m.append(x)
        else:
            r.append(x)
    
    return l + m + r

import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
a = list(map(int, data[1].split()))

res = qSort(a)
print(' '.join(map(str, res)))
