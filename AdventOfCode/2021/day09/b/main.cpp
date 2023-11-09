#include <algorithm>
#include <bits/stdc++.h>
#include <fstream>
#include <functional>
#include <iostream>
#include <utility>

using namespace std;

struct Position {
  int x, y;
  Position(int x, int y) : x(x), y(y) {}
};

int main() {
  // 1. read inputs
  const string FILENAME = "../inputs/2.txt";
  ifstream file(FILENAME);
  vector<vector<int>> grid;
  string line;
  while (getline(file, line)) {
    vector<int> row;
    for (auto &l : line)
      row.push_back(l - '0');
    grid.push_back(row);
  }
  file.close();

  int m = grid.size();
  int n = grid[0].size();

  // [ PART 1 - Find low points]
  vector<int> lowPoints;
  vector<Position> positions;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      bool up = (i - 1 >= 0) ? grid[i][j] < grid[i - 1][j] : true;
      bool down = (i + 1 < m) ? grid[i][j] < grid[i + 1][j] : true;
      bool left = (j - 1 >= 0) ? grid[i][j] < grid[i][j - 1] : true;
      bool right = (j + 1 < n) ? grid[i][j] < grid[i][j + 1] : true;
      if (up && down && left && right) {
        positions.push_back(Position(i, j));
        lowPoints.push_back(grid[i][j]);
      }
    }
  }

  int sumPoints = 0;
  for (const auto &p : lowPoints)
    sumPoints += p + 1;

  cout << "[ PART 1 ] Sum Low Points: " << sumPoints << '\n';

  // [ PART 2 - Compute 3 largest bassins] - FIXME: why does it revisit old

  vector<pair<int, int>> directions = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
  vector<int> bassins;
  for (auto &position : positions) { // BFS
    // cout << position.x << ' ' << position.y << '\n';
    int size = 0;
    queue<Position> q; // (old position, new position)
    q.push(position);
    set<pair<int, int>> visited;

    while (!q.empty()) {
      Position current = q.front();
      // visited.insert(make_pair(current.x, current.y));
      q.pop();
      size += 1;
      for (auto &d : directions) {
        int x = current.x + d.first;
        int y = current.y + d.second;
        if ((0 <= x && x < m) && (0 <= y && y < n) &&
            (grid[current.x][current.y] < grid[x][y]) && (grid[x][y] < 9) &&
            (visited.count(make_pair(x, y)) == 0)) {
          visited.insert(make_pair(x, y));
          q.push(Position(x, y));
        }
      }
    }
    bassins.push_back(size);
  }

  sort(bassins.begin(), bassins.end(), greater<int>());

  for (auto &b : bassins)
    cout << b << ' ';

  vector<int> top3bassins(bassins.begin(), bassins.begin() + 3);
  int top3Size =
      accumulate(top3bassins.begin(), top3bassins.end(), 1, multiplies<int>());

  cout << "[PART 2] Top 3 bassins: " << top3Size << '\n';

  return 0;
}
