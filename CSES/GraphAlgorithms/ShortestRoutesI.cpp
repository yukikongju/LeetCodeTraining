#include <bits/stdc++.h>
#include <queue>
#include <vector>

typedef long long ll;

using namespace std;

struct Edge {
  int v;
  ll w;
};

struct Node {
  int id;
  ll dist;

  friend bool operator<(const Node &a, const Node &b) {
    return a.dist > b.dist;
  }
};

int n, m;
vector<ll> distances;
vector<vector<Edge>> G;
priority_queue<Node> Q;
const ll MAXD = 1e17;

int main() {
  // read
  cin >> n >> m;

  int u, v;
  ll w;
  G.resize(n + 1);
  distances.resize(n + 1);
  for (int i = 0; i < m; i++) {
    cin >> u >> v >> w;
    G[u].push_back({v, w});
  }
  for (int i = 0; i < distances.size(); i++)
    distances[i] = MAXD;

  // dikjstra
  int src = 1;
  distances[src] = 0;
  Q.push({1, 0});
  while (!Q.empty()) {
    int node = Q.top().id;
    ll dist = Q.top().dist;
    Q.pop();

    if (dist > distances[node])
      continue;

    for (Edge e : G[node]) {
      if (distances[e.v] > dist + e.w) {
        distances[e.v] = dist + e.w;
        Q.push({e.v, dist + e.w});
      }
    }
  }

  // print
  for (int i = 1; i <= n; i++)
    cout << distances[i] << ' ';
  cout << '\n';

  return 0;
}
