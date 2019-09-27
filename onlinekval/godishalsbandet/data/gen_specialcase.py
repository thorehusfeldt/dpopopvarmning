#!/usr/bin/env python3
#Make the first half the answer, one of the most sensible bugs and not caught without special case

import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed = int(cmdlinearg('seed', sys.argv[-1]))
k = int(cmdlinearg('k'))

if k==1:
    print("BBBVBVBBBBVVVVVVVBVV")