# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:20:56 2019

@author: Mattias Akke
"""

import numpy.random as random
import queue
import sys

def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    #return default[name]

def main():
    random.seed(int(sys.argv[-1]))
    n = int(cmdlinearg("n"))
    nr = int(cmdlinearg('nr'))
    randomlist = [1]*(nr) + [2] + [0]

    lista = [[] for _ in range(n)]
    q = queue.Queue()
    perm = random.permutation(list(range(n))).tolist()
    v = perm[-1]
    del perm[-1]
    lista[perm[-1]].append(str(v))
    lista[v].append(str(perm[-1]))
    q.put_nowait(perm[-1])
    del perm[-1]
    lista[perm[-1]].append(str(v))
    lista[v].append(str(perm[-1]))
    q.put_nowait(perm[-1])
    del perm[-1]

    while(len(perm) > 0):
        now = q.get_nowait()
        branches = random.choice(randomlist)
        while(branches == 0 and q.empty()):
            branches = random.choice(randomlist)
        if(len(perm)== 1):
            lista[now].append(str(perm[0]))
            lista[perm[0]].append(str(now))
            del perm[0]
        else:
            for i in range(branches):
                v = perm[-1]
                del perm[-1]
                q.put_nowait(v)
                lista[now].append(str(v))
                lista[v].append(str(now))

    string = str(n) + "\n"
    for l in lista:
        string += str(len(l)) + " " + ' '.join(l) + "\n"
    print(string)
    
if __name__ == "__main__":
    main()