# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:38:29 2019

@author: Mattias Akke
"""

import queue

for nr, path in enumerate(pathlist):
     file = open(str(path), 'r')
     n = int(nxt_line(file))
     print(n)
     tree, steps, bt = [], [], []
     pq = queue.PriorityQueue()
     for i in range(n):
         line = [int(x) for x in nxt_line(file).split()]
         m = line[0]
         tree.append(line[1:])
         if m == 1:
             pq.put_nowait((0,i))
         bt.append(m)
         steps.append(0)
     file.close()
     
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
     
     file = open('Group5_answers/ANS_%s'%(str(path)[len(foldername)+1:]), 'w')
     file.write(str(steps[lst]))
     file.close()