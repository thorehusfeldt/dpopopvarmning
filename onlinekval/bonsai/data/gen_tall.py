# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:20:56 2019

@author: Mattias Akke
"""

import random
import queue
import sys

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
    randomlist = [1]*random.randint(6) + [2] + [0]

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
    lstnode = find_sol_node(lista)
    
    for l in lista:
        string += str(len(l)) + " " + ' '.join(l).replace('0', 'x').replace(str(lstnode), '0').replace('x', str(lstnode)) + "\n"
    print(string)
    
if __name__ == "__main__":
    main()
