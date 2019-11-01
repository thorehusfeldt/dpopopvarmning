#!/usr/bin/python3

import sys
import random
from solve import solve

def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    #return default[name]

def main():
    random.seed(int(sys.argv[-1]))
    n = int(cmdlinearg("n"))
    m = int(cmdlinearg("m"))
    onlyForward = cmdlinearg("onlyForward")=="True"
    
    g = random.randint(1,1e2)
    MAX_SPEED = 1e2

    band = [[random.randint(0,m-1),random.randint(0,m-1),random.randint(1,MAX_SPEED)] for _ in range(n)]


    if onlyForward:

        for i in range(len(band)):
            if band[i][0]>band[i][1]:
                (band[i][0],band[i][1]) = (band[i][1],band[i][0])

        dn = 1
        up = len(band)

        while dn+1<up:#binärsök efter minsta antalet band att ta bort så att det räcker att bara gå framåt
            mid = (dn+up)//2
            if solve(n,m,g,band[:mid],onlyForward=True)==solve(n,m,g,band[:mid]):
                dn = mid
            else:
                up = mid
        band = band[:dn]
        #assert(solve(n,m,g,band,onlyForward=True)==solve(n,m,g,band))

        extraBackwards = [[random.randint(0,m-1),random.randint(0,m-1),random.randint(1,MAX_SPEED)] for _ in range(n-len(band))]
        dn = 0
        up = len(extraBackwards)
        #print(len(band))
        while dn+1<up:#binärsök efter minsta antalet band att ta bort så att det räcker att bara gå framåt
            mid = (dn+up)//2
            if solve(n,m,g,band+extraBackwards[:mid],onlyForward=True)==solve(n,m,g,band+extraBackwards[:mid]):
                dn = mid
            else:
                up = mid
        band = band+extraBackwards[:dn]

        #assert(solve(n,m,g,band,onlyForward=True)==solve(n,m,g,band))

    random.shuffle(band)
    print(len(band),m,g)
    for b in band:
        print(b[0]+1,b[1]+1,b[2])
    
    #print("ans1: ", solve(n,m,g,band,onlyForward=True))
    #print("ans2: ", solve(n,m,g,band))


if __name__ == "__main__":
    main()

