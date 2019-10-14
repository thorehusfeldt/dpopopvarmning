#include "validator.h"

void run() {
	int n = Int(1,Arg("nMax"));
	Space();

	int k = Int(1, min(n,(int)Arg("kMax")));
    Space();

	int q = Int(1, Arg("qMax"));
	Endl();

	vector<int> values = SpacedInts(n, 0, k-1);
	assert((int)set<int>(values.begin(), values.end()).size() == k);

	for(int i = 0; i < q; i++){
		int l = Int(1,n);
		Space();
		int r = Int(1,n);
		Endl();
		assert(l <= r);
	}

}

