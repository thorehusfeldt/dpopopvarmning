#include "validator.h"
typedef long long ll;
typedef long double ld;
typedef vector<ll> vi;
typedef vector< vector<ll> > vii;
#define rep(i, a, b) for(int i = a; i < b; i++)
#define all(a) a.begin(),a.end()
#define sz(a) (ll) (a).size()
#define pb push_back
const ll inf = 90000000000;
const ll mod = 1000000009;

//input format
//n
//m_0 a_0 a_2 ... a_m0
// .
// .
// .
//m_n ...

class UF {
  int *id, cnt, *sz;
  public:

    UF(int N) {
        cnt = N; id = new int[N]; sz = new int[N];
        for (int i = 0; i<N; i++)  id[i] = i, sz[i] = 1; }
    ~UF() { delete[] id; delete[] sz; }


    int find(int p) {
        int root = p;
        while (root != id[root])    root = id[root];
        while (p != root) { int newp = id[p]; id[p] = root; p = newp; }
        return root;
    }

    void merge(int x, int y) {
        int i = find(x); int j = find(y); if (i == j) return;
        if (sz[i] < sz[j]) { id[i] = j, sz[j] += sz[i]; }
        else { id[j] = i, sz[i] += sz[j]; }
        cnt--;
    }
    bool connected(int x, int y) { return find(x) == find(y); }
    int count() { return cnt; }
};

int solve(vii tree){
    int n = sz(tree);
    priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<pair<ll,ll>>> q;
    vi steps, bt;
    rep(i,0,n){
        ll m = sz(tree[i]);
        if (m == 1) q.push({0,i});
        bt.pb(m); steps.pb(0);
    }
    ll last = 0;
    while(q.empty() == 0){
        ll node = q.top().second; q.pop();
        last = node;
        rep(i,0,tree[node].size()){
            bt[tree[node][i]] --;
            if(steps[tree[node][i]] < steps[node] + 1) steps[tree[node][i]] = steps[node] + 1;
            else steps[tree[node][i]]++;
            if(bt[tree[node][i]] == 1) q.push({steps[tree[node][i]], tree[node][i]});
        }
    }
    return((steps[last], steps[last]==steps[0]));
}

void run(){
    int restr = Arg("restr")
    int rooted = Arg("rooted")
    int n = INT(1,Arg("n"));
    Endl();
    vii tree;
    UF(n);
    int ms = 0;
    rep(i,0,n){
        vi branches;
        int m = INT(1,n); //Blir detta typ-> cin >> m; assert(m > 0);   ?
        Space();
        ms += m;
        if (restr == 2) assert(m <= 2); //assert group 1
        if (restr == 3) assert(m <= 3); //assert group 2
        vi neigh;
        rep(j,0,m){
            int a = INT(0,n);
            Space();
            assert(a != j);
            merge(j, a);
            neigh.pb(a);
        }
        Endl();
        tree.pb(neigh);
    }
    assert(n-1 == ms / 2); //assert tree
    assert(count() == 1); //assert one component
    if rooted{
        sol = solve(tree);
        assert(sol.second == true); //assert that the root is a solution
        if (restr == 15) assert(sol.first <= 15)); //assert group 3
    }
}
