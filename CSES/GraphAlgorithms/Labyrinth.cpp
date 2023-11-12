#include <bits/stdc++.h>
#include <cstdlib>

using namespace std;

int n, m;
vector<vector<bool>> vis;
vector<vector<pair<int, int>>> path;
vector<vector<char>> grid;
int sx, sy, ex, ey;
vector<pair<int, int>> neighbors = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool isValid(int x, int y) {
  if (x < 0 or x >= n or y < 0 or y >= m)
    return false;
  if (vis[x][y])
    return false;
  return true;
}

void bfs() {

  queue<pair<int, int>> q;
  q.push({sx, sy});
  while (!q.empty()) {
    int cx = q.front().first;
    int cy = q.front().second;
    q.pop();

    for (auto neighbor : neighbors) {
      int dx = neighbor.first;
      int dy = neighbor.second;
      if (isValid(cx + dx, cy + dy)) {
        q.push({cx + dx, cy + dy});
        vis[cx + dx][cy + dy] = true;
        path[cx + dx][cy + dy] = {dx, dy};
      }
    }
  }
}

int main() {
  cin >> n >> m;
  vis.resize(n);
  path.resize(n);
  grid.resize(n);
  for (int i = 0; i < n; i++) {
    vis[i].resize(m);
    path[i].resize(m);
    grid[i].resize(m);
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> grid[i][j];
      path[i][j] = {-1, -1};
      if (grid[i][j] == '#') {
        vis[i][j] = true;
      }
      if (grid[i][j] == 'A') {
        sx = i;
        sy = j;
      }
      if (grid[i][j] == 'B') {
        ex = i;
        ey = j;
      }
    }
  }

  // run bfs
  bfs();

  // check if path exists
  if (!vis[ex][ey]) {
    cout << "NO" << '\n';
    return 0;
  }

  // reconstruct path
  cout << "YES" << '\n';
  pair<int, int> end = {ex, ey};
  vector<pair<int, int>> ans;

  while (end.first != sx or end.second != sy) {
    ans.push_back(path[end.first][end.second]);
    end.first -= ans.back().first;
    end.second -= ans.back().second;
  }

  reverse(ans.begin(), ans.end());
  cout << ans.size() << '\n';
  string pathStr;
  for (auto c : ans) {
    if (c.first == 1 and c.second == 0)
      pathStr.push_back('D');
    if (c.first == -1 and c.second == 0)
      pathStr.push_back('U');
    if (c.first == 0 and c.second == 1)
      pathStr.push_back('R');
    if (c.first == 0 and c.second == -1)
      pathStr.push_back('L');
  }
  cout << pathStr << '\n';

  return 0;
}
