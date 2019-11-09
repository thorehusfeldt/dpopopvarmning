#!/usr/bin/env bash

. ../../../testdata_tools/gen.sh

use_solution sl.cpp

compile gen_random.py

samplegroup
sample 1

group group1 100
include_group sample
tc small gen_random n=2 m=1
tc small2 gen_random n=5 m=3
tc small3 gen_random n=5 m=3
tc small4 gen_random n=5 m=3
tc small5 gen_random n=5 m=3
tc small6 gen_random n=5 m=3
tc rand1 gen_random n=98 m=50
tc rand2 gen_random n=97 m=200
tc rand3 gen_random n=90,10 m=1000
tc compl gen_random n=100 m=0
tc compl2 gen_random n=99 m=-4
tc compl-bip gen_random n=50,50 m=0
tc compl-bip2 gen_random n=90,10 m=-3
tc compl-split1 gen_random n=100 c=99 m=0
tc compl-split2 gen_random n=99 c=30 m=0
