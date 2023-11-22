#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<bool> visited, teams;
bool possible;
vector<vector<int>> G;

void dfs(int u, int p = 0) {
  for (int v : G[u]) {
    if (v != p) {
      if (!visited[v]) {
        visited[v] = true;
        teams[v] = !teams[u];
        dfs(v, u);
      } else {
        if (teams[v] == teams[u])
          possible = false;
      }
    }
  }
}

int main() {
  // 1. read inputs
  cin >> N >> M;
  visited.resize(N + 1);
  teams.resize(N + 1);
  G.resize(N + 1);

  int u, v;
  for (int i = 0; i < M; i++) {
    cin >> u >> v;
    G[u].push_back(v);
    G[v].push_back(u);
  }

  // 2. Bipartite Match Algorithm
  possible = true;
  for (int i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      dfs(i);
    }
  }

  // 3. print solution
  if (!possible) {
    cout << "IMPOSSIBLE";
  } else {
    for (int i = 1; i <= N; i++) {
      cout << (!teams[i] ? 1 : 2) << ' ';
    }
    cout << '\n';
  }

  return 0;
}
