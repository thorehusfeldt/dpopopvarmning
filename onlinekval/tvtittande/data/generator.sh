#!/usr/bin/env bash

. ../../../testdata_tools/gen.sh

use_solution gustav.cpp

compile gen_random.py
compile gen_smart.py
compile gen_smart2.py

samplegroup
limits nMax=10 kMax=10
sample 1
sample 2
#sample 3

group group1 40
limits nMax=50 kMax=50
tc 1
tc 2
tc small-rand-1 gen_random n=1 k=1 days=1 maxlength=10 csum=1
tc small-rand-2 gen_random n=1 k=1 days=1 maxlength=100000 csum=1
tc small-rand-3 gen_random n=1 k=1 days=5 maxlength=50 csum=1
tc small-rand-4 gen_random n=1 k=1 days=100 maxlength=1000 csum=1
tc small-rand-5 gen_random n=1 k=1 days=10000 maxlength=100000 csum=1
tc small-rand-6 gen_random n=1 k=1 days=100000 maxlength=100000 csum=1
tc small-rand-7 gen_random n=2 k=1 days=10000 maxlength=100000 csum=2
tc small-rand-8 gen_random n=3 k=1 days=30000 maxlength=100000 csum=3
tc small-rand-9 gen_random n=10 k=1 days=100000 maxlength=100000 csum=10
tc small-rand-10 gen_random n=10 k=2 days=100000 maxlength=100000 csum=10
tc small-rand-11 gen_random n=10 k=4 days=100000 maxlength=50000 csum=20
tc small-rand-12 gen_random n=50 k=4 days=1000 maxlength=5000 csum=200

tc small-smart-1 gen_smart n=50 k=50 days=500 ans=Ja
tc small-smart-2 gen_smart n=50 k=50 days=500 ans=Ja
tc small-smart-3 gen_smart n=50 k=50 days=1000 ans=Ja
tc small-smart-4 gen_smart n=50 k=50 days=10000 ans=Ja

group group2 20
limits nMax=1000 kMax=1000
include_group group1
tc med-smart-1 gen_smart n=1000 k=1000 days=10000 ans=Ja
tc med-smart-2 gen_smart n=1000 k=1000 days=10000 ans=Ja

group group3 40
limits nMax=100000 kMax=100000
include_group group2
tc big-smart-1 gen_smart n=10000 k=100000 days=100000 ans=Ja
tc big-smart-2 gen_smart n=10000 k=100000 days=100000 ans=Ja
tc big-smart-3 gen_smart n=90000 k=100000 days=100000 ans=Ja
