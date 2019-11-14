#include "validator.h"
#include <cmath>

#define sz(v) int(v.size())

void run() {
	int nMax = Arg("nMax");
        int kMax = Arg("kMax");
	
	int n = Int(1, nMax);
	Space();
	int k = Int(1, kMax);
	Endl();
	for(int i = 0; i < k; i++){
		int len = Int(1, 1000000);
		if(i != k-1) Space();
	}
	Endl();
	long long csum = 0;
	int prevday = 0;
	for(int i = 0; i < n; i++){
		int d = Int(prevday+1, 100000);
		prevday = d;
		Space();
		int c = Int(1, 100000);
		csum += c;
		Space();
		set<int> serier;
		for(int j = 0; j < c; j++){
			int x = Int(1, k);
			serier.insert(x);
			if(j != c-1) Space();
		}
		assert(sz(serier) == c);
		Endl();
	}
	assert(csum <= 100000);
}
