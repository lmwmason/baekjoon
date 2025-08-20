#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e18;

struct line { ll a, b; };
struct node { int l, r; line ln; };

ll n;
const int MAX = 50001;

vector<int> v[MAX], g[MAX];
vector<ll> dp[MAX], vec_[MAX];
int par_[MAX], ind[MAX], dep[MAX];
vector<node> seg[MAX];
vector<line> lines_[MAX];
ll psum[MAX];
int ns[MAX], ne[MAX];

ll f(line l, ll x) { return l.a * x + l.b; }
ll sq(ll x) { return x * x; }

void init(int idx, int s, int e) {
    ns[idx] = s; ne[idx] = e;
    seg[idx].push_back({-1, -1, {0, INF}});
}

void insert_line(int idx, int num, int s, int e, line l) {
    line lo = seg[idx][num].ln, hi = l;
    if (f(lo, s) > f(hi, s)) swap(lo, hi);
    if (f(lo, e) <= f(hi, e)) {
        seg[idx][num].ln = lo;
        return;
    }
    int mid = (s + e) >> 1;
    if (f(lo, mid) < f(hi, mid)) {
        seg[idx][num].ln = lo;
        if (seg[idx][num].r == -1) {
            seg[idx][num].r = seg[idx].size();
            seg[idx].push_back({-1, -1, {0, INF}});
        }
        insert_line(idx, seg[idx][num].r, mid + 1, e, hi);
    } else {
        seg[idx][num].ln = hi;
        if (seg[idx][num].l == -1) {
            seg[idx][num].l = seg[idx].size();
            seg[idx].push_back({-1, -1, {0, INF}});
        }
        insert_line(idx, seg[idx][num].l, s, mid, lo);
    }
}

void insert_line(int idx, line l) {
    l.b -= psum[idx];
    lines_[idx].push_back(l);
    insert_line(idx, 0, ns[idx], ne[idx], l);
}

void apply(int idx) {
    for (auto &l : lines_[idx]) l.b += psum[idx];
    for (auto &n : seg[idx]) n.ln.b += psum[idx];
    psum[idx] = 0;
}

ll query(int idx, int num, int s, int e, ll x) {
    if (num == -1) return INF;
    int mid = (s + e) >> 1;
    ll d = f(seg[idx][num].ln, x) + psum[idx];
    if (x <= mid) return min(d, query(idx, seg[idx][num].l, s, mid, x));
    return min(d, query(idx, seg[idx][num].r, mid + 1, e, x));
}

ll query(int idx, ll x) {
    return query(idx, 0, ns[idx], ne[idx], x);
}

void dfs(int pos, int d = 0, int p = 0) {
    par_[pos] = p;
    dep[pos] = d;
    for (int w : v[pos]) {
        if (w == p) continue;
        g[pos].push_back(w);
        dfs(w, d + 1, pos);
    }
}

void fill_dp(int pos) {
    ll sum = 0;
    for (auto w : g[pos]) {
        ll d = query(w, dep[pos]) + sq(dep[pos]);
        sum += d;
        vec_[pos].push_back(d);
    }
    dp[pos][0] = sum;
    for (int i = 1; i <= g[pos].size(); i++)
        dp[pos][i] = sum - vec_[pos][i - 1];
}

void merge_dp(int pos) {
    ll sum = dp[pos][0];
    ll x = dep[pos];
    vector<line> new_lines;

    for (int i = 0; i < g[pos].size(); i++) {
        int w = g[pos][i];
        if (lines_[w].size() <= lines_[pos].size()) {
            apply(w);
            for (auto l : lines_[w]) {
                ll l1 = f(l, 2 * x);
                ll c = -sum + dp[pos][i + 1] + 4 * sq(x);
                ll y1 = -l.a / 2;
                new_lines.push_back({ -2 * x, query(pos, 2 * x - y1) + l1 + c + sq(x) });
            }
            for (auto l : lines_[w]) {
                l.b += dp[pos][i + 1];
                insert_line(pos, l);
            }
        } else {
            psum[w] += dp[pos][i + 1];
            apply(pos);
            for (auto l : lines_[pos]) {
                ll l1 = f(l, 2 * x);
                ll c = -sum + 4 * sq(x);
                ll y1 = -l.a / 2;
                new_lines.push_back({ -2 * x, query(w, 2 * x - y1) + l1 + c + sq(x) });
            }
            for (auto l : lines_[pos])
                insert_line(w, l);
            swap(seg[w], seg[pos]);
            swap(lines_[w], lines_[pos]);
            swap(psum[w], psum[pos]);
            swap(ns[w], ns[pos]);
            swap(ne[w], ne[pos]);
        }
    }
    for (auto l : new_lines) insert_line(pos, l);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int u, w; cin >> u >> w;
        v[u].push_back(w);
        v[w].push_back(u);
    }

    int root = 1;
    for (int i = 1; i <= n; i++)
        if (v[i].size() == 1) root = i;

    dfs(root);

    for (int i = 1; i <= n; i++) {
        ind[i] = g[i].size();
        dp[i].resize(ind[i] + 1, INF);
        init(i, 0, n);
    }

    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (!ind[i]) {
            q.push(i);
            dp[i][0] = 0;
            insert_line(i, {-2 * dep[i], sq(dep[i])});
        }
    }

    while (!q.empty()) {
        int top = q.front(); q.pop();
        int t = par_[top];
        if (--ind[t] == 0) {
            q.push(t);
            fill_dp(t);
            merge_dp(t);
        }
    }

    cout << dp[root][0];
}
