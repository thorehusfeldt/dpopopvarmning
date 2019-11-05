# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:20:56 2019

@author: Mattias Akke
"""

import numpy.random as random
import sys

def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    #return default[name]

def main():
    random.seed(int(sys.argv[-1]))
    n = int(cmdlinearg("n"))
    nr = int(cmdlinearg('n'))
    randlist = [0]  + [1]*(nr)
    lista = [[]]

    nxt = 1
    for i in range(n):
        old = nxt
        for j in range(old):
            b = random.choice(randlist)
            if b:
                lista[j].append(nxt)
                lista.append([j])
                nxt += 1
    perm = random.permutation(list(range(nxt))).tolist()
    lista2 = [[] for _ in range(len(lista))]
    for i, l in enumerate(lista):
        j = perm[i]
        l2 = [str(perm[x]) for x in l]
        lista2[j] = l2
            
    string = str(len(lista2)) + "\n"
    for l in lista2:
        string += str(len(l)) + " " + ' '.join(l) + "\n"
    print(string)

if __name__ == "__main__":
    main()