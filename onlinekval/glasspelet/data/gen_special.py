#!/usr/bin/python3

import sys
import random


def cmdlinearg(name):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    return default[name]

def main():
    random.seed(int(sys.argv[-1]))
    print("13 3 4")
    print("0 1 1 2 0 2 1 1 0 1 2 1 0")
    print("1 5")
    print("5 9")
    print("9 13")
    print("4 4")
    
if __name__ == "__main__":
    main()

