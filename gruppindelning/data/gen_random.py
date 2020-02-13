#!/usr/bin/env python3

import sys
import random
import string

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed = int(cmdlinearg('seed', sys.argv[-1]))
ns = list(map(int, cmdlinearg('n').split(',')))
n = sum(ns)
c = int(cmdlinearg('c', 0))
m = int(cmdlinearg('m'))
random.seed(seed)

def genname():
    ret = []
    for _ in range(random.randint(5, 20)):
        ret.append(random.choice(string.ascii_uppercase))
    return ''.join(ret)
names = [genname() for _ in range(n)]

if c:
    comps = [random.randrange(c) for _ in range(n)]
else:
    comps = []
    for i, co in enumerate(ns):
        comps.extend([i] * co)
random.shuffle(comps)

cands = []
for i in range(n):
    for j in range(i+1, n):
        if comps[i] == comps[j]:
            cands.append((i, j))

print(n)
for na in names:
    print(na)

if m <= 0:
    m = len(cands) + m
else:
    assert m <= len(cands)
print(m)
for (a, b) in random.sample(cands, m):
    if random.choice([True, False]):
        a,b = b,a
    print(names[a], names[b])
