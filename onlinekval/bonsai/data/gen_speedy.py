# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:20:56 2019

@author: Mattias Akke
"""

import numpy.random as random
import sys
import queue
import random
def find_sol_node(tree):

     steps, bt = [], []
     pq = queue.PriorityQueue()
     for ind, line in enumerate(tree):
         m = len(line)
         if m == 1:
             pq.put_nowait((0,ind))
         bt.append(m)
         steps.append(0)
     
     lst = 0
     while pq.empty() == 0:
         _, node = pq.get()
         lst = node
         for i in range(len(tree[node])):
             bt[tree[node][i]] -= 1
             if steps[tree[node][i]] < steps[node] + 1:
                 steps[tree[node][i]] = steps[node] + 1
             else:
                 steps[tree[node][i]] += 1
             if bt[tree[node][i]] == 1:
                 pq.put((steps[tree[node][i]], tree[node][i]))
     return lst
 
def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    #return default[name]

def main():
    random.seed(int(sys.argv[-1]))
    n = int(cmdlinearg("n"))
    rooted = int(cmdlinearg('rooted'))
    randlist = [0]  + [1]*random.randint(4)
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
    lstnode = find_sol_node(lista)
    for l in lista2:
        string += str(len(l)) + " " + ' '.join(l).replace('0', 'x').replace(str(lstnode), '0').replace('x', str(lstnode)) + "\n"
    print(string)

if __name__ == "__main__":
    main()
