# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:11:50 2019

@author: Mattias Akke
"""
import random
import math
import sys
from solve import solve

def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    #return default[name]

def gen_tree(n, mode):
    eds = []
    assert mode in ['random', 'star', 'line', 'shallow', 'deep', 'deeper']
    depth = [0]
    for i in range(1, n):
        if mode == 'random':
            pred = random.randrange(i)
        elif mode == 'star':
            pred = 0
        elif mode == 'line':
            pred = i-1
        elif mode == 'shallow':
            pred = int(random.uniform(0, i**0.2) ** 5)
        elif mode == 'deep':
            pred = i-1 - int(random.uniform(0, i**0.1) ** 10)
        elif mode == 'deeper':
            if i < 4:
                pred = random.randrange(i)
            else:
                hi = math.log2(math.log2(i))
                pred = i - int(2 ** 2 ** min(random.uniform(-3, hi), random.uniform(-3, hi), random.uniform(-3, hi)))
        else:
            assert False
        assert 0 <= pred < i
        eds.append((pred, i))
        depth.append(depth[pred] + 1)
    return eds


def main():
    random.seed(int(sys.argv[-1]))
    n = int(cmdlinearg("n"))
    mode = int(cmdlinearg("mode"))

    eds = gen_tree(n, mode)
    lista = [[] for _ in range(n)]
    for e in eds:
        x, y = e
        lista[x], lista[y] = str(y), str(x)
        
    string = str(n) + "\n"
    for l in lista:
        string += str(len(l)) + " " + ' '.join(l) + "\n"
    print(string)

if __name__ == "__main__":
    main()