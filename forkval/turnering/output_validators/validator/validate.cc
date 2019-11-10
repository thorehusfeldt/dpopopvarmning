#include <vector>
#include <cstring>
#include <algorithm>
#include "validate.h"

using namespace std;

vector<string> read_solution(int n, istream &sol, feedback_function feedback) {
	vector<string> ret(n);
	for (int i = 0; i < n; i++) sol >> ret[i];
	if (!sol) feedback("Unexpected EOF");
	string tmp;
	if (sol >> tmp) feedback("Trailing output");
	for (string& s : ret) {
		auto ind = s.find('-');
		if (ind == string::npos) feedback("No - in line");
		string s2 = s.substr(ind + 1) + "-" + s.substr(0, ind);
		if (s2 < s) swap(s, s2);
	}
	sort(ret.begin(), ret.end());
	return ret;
}

int main(int argc, char **argv) {
	init_io(argc, argv);

	int n;
	judge_in >> n;
	n /= 2;

	vector<string> a = read_solution(n, cin, wrong_answer);
	vector<string> b = read_solution(n, judge_ans, judge_error);

	if (a == b) accept();
	else wrong_answer("wrong");
}
