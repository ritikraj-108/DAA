from collections import defaultdict

def maxPeople(t, cs, ce):
    t = sorted(t)
    cs = sorted(cs)
    ce = sorted(ce)

    si = 0
    ei = 0
    active = set()

    coverage = defaultdict(int)
    free_pop = 0
    for i in range(len(t)):
        pos = t[i][0]
        while si < len(cs) and cs[si][0] <= pos:
            active.add(cs[si][1])
            si += 1
        while ei < len(ce) and ce[ei][0] < pos:
            active.remove(ce[ei][1])
            ei += 1
        if len(active) == 1:
            t[i][2] = list(active)[0]
            coverage[list(active)[0]] += t[i][1]
        elif len(active) == 0:
            free_pop += t[i][1]

    return max(coverage.values(), default=0) + free_pop

import sys

input = sys.stdin.read
data = input().splitlines()

nt = int(data[0].strip())
pop = [int(x) for x in data[1].strip().split()]
pos = [int(x) for x in data[2].strip().split()]
t = [[pos[i], pop[i], -1] for i in range(nt)]
nc = int(data[3].strip())
cp = [int(x) for x in data[4].strip().split()]
cr = [int(x) for x in data[5].strip().split()]
cs = [[cp[i] - cr[i], i] for i in range(nc)]
ce = [[cp[i] + cr[i], i] for i in range(nc)]
result = maxPeople(t, cs, ce)
print(result)
