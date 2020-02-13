#include "validator.h"

void run() {
	int n = Int(2, 100);
	Endl();
	set<string> names;
	for (int i = 0; i < n; i++) {
		string name = _token();
		Endl();
		assert(name.size() >= 1);
		assert(name.size() <= 20);
		for (char c : name) {
			assert('A' <= c && c <= 'Z');
		}
		names.insert(name);
	}
	assert((int)names.size() == n);

	int m = Int(1, 4950);
	Endl();
	set<pair<string, string>> pairs;
	for (int i = 0; i < m; i++) {
		string a = _token();
		Space();
		string b = _token();
		Endl();
		assert(names.count(a));
		assert(names.count(b));
		assert(a != b);
		pairs.emplace(a, b);
		pairs.emplace(b, a);
	}
	assert((int)pairs.size() == 2*m);
}
