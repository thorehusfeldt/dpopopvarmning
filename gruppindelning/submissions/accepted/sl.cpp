#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


struct UF {
	vi e;
	UF(int n) : e(n, -1) {}
	bool same_set(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int N;
	cin >> N;
	UF uf(N);
	map<string, int> names;
	rep(i,0,N) {
		string a;
		cin >> a;
		names[a] = i;
	}
	int M;
	cin >> M;
	int comp = 0;
	rep(i,0,M) {
		string a, b;
		cin >> a >> b;
		int A = names[a];
		int B = names[b];
		uf.join(A, B);
	}
	rep(i,0,N) if (uf.find(i) == i) comp++;
	cout << comp << endl;
}
