#include "validator.h"

void run() {
	int a = Int(1, 10);
	Space();
	int b = Int(1, 10);
	Endl();
	SpacedInts(a, 1, 20);
	SpacedInts(b, 1, 20);
}
