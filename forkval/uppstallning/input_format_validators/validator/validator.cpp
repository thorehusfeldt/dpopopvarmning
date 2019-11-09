#include "validator.h"

void run() {
	int n = Int(3, 8);
	Endl();
	for (int i = 0; i < n; i++) {
		Int(0, n);
		Space();
		Int(0, n);
		Endl();
	}
}
