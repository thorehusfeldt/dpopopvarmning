#include "validator.h"

struct UF {
	vector<int> v;
	UF(int n) : v(n, -1) {}
	int find(int x) { return v[x] < 0 ? x : v[x] = find(v[x]); }
	bool join(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b) return false;
		if (-v[a] < -v[b]) swap(a, b);
		v[a] += v[b];
		v[b] = a;
		return true;
	}
};

void run() {
	int n = Int(2, 20);
	Space();
	int m = Int(2, n);
	Endl();
	UF uf(n+1);
	vector<int> pars = SpacedInts(n, 0, n);
	for (int i = 1; i <= n; i++) {
		int par = pars[i - 1];
		assert(uf.join(i, par));
	}
	vector<int> nums = SpacedInts(m, 1, n);
	AssertUnique(nums);
}
