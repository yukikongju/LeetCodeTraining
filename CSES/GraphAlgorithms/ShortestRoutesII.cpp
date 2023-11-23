#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const ll INF = 0x3f3f3f3f3f3f3f3f;

// struct Edge {
//   int v;
//   ll w;
// };

int N, M, Q;
vector<vector<ll>> distances;

int main() {
  // 1. read inputs
  cin >> N >> M >> Q;
  distances.resize(N + 1, vector<ll>(N + 1, INF));

  int u, v;
  ll w;
  for (int i = 0; i < M; i++) {
    cin >> u >> v >> w;
    distances[u][v] = min(distances[u][v], w);
    distances[v][u] = min(distances[u][v], w);
  }

  // 2. Floyd-Warshall
  for (int i = 1; i <= N; i++)
    distances[i][i] = 0;

  for (int k = 1; k <= N; k++) {
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        distances[i][j] =
            min(distances[i][j], distances[i][k] + distances[k][j]);
      }
    }
  }

  // 3. print
  for (int i = 1; i <= Q; i++) {
    cin >> u >> v;
    if (distances[u][v] == INF)
      cout << "-1 " << '\n';
    else
      cout << distances[u][v] << '\n';
  }

  return 0;
}
