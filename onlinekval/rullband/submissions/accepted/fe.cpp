#include <bits/stdc++.h>
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")

using namespace std;

#define rep(i, a, b) for(ll i = a; i < ll(b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (ll)(x).size()
typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<ll> vi;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);

    ll n,m,g;
    cin>>n>>m>>g;

    vector<vector<pii>> e(m);

    rep(i,0,n){
        ll a,b,c;
        cin>>a>>b>>c;
        e[a-1].emplace_back(b-1,c);
    }

    priority_queue<pii,vector<pii>,greater<pii>> pq;
    pq.emplace(0,0);

    vector<bool> seen(m);

    while(pq.size()){
        ll d,v;
        tie(d,v) = pq.top();
        pq.pop();
        if(v<0||v>=m||seen[v]) continue;
        seen[v] = true;
        if(v==m-1){
            cout<<d+g<<endl;
            return 0;
        }
        pq.emplace(d+g,v+1);
        pq.emplace(d+g,v-1);

        trav(ed,e[v]){
            pq.emplace(ed.second+d,ed.first);
        }
    }
    assert(false);
}