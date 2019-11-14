#!/usr/bin/env python3

import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed = int(cmdlinearg('seed', sys.argv[-1]))
n = int(cmdlinearg('n'))
k = int(cmdlinearg('k'))
days = int(cmdlinearg('days'))
maxlength = int(cmdlinearg('maxlength'))
csum = int(cmdlinearg('csum'))
assert n <= days
assert csum >= n
assert csum <= k*n

random.seed(seed)

print(n, k)
for i in range(k):
    print(random.randint(1, maxlength), end='')
    if(i != k-1): print(' ', end='')
print()

events = random.sample(range(1, days+1), k=n)
events.sort()
c = [1]*n
for i in range(csum-n):
    p = -1
    while p == -1 or c[p] == k:
        p = random.randint(0,n-1)
    c[p] += 1
for i in range(n):
    print(events[i], c[i], end=' ')
    print(*random.sample(range(1, k+1), k=c[i]))
