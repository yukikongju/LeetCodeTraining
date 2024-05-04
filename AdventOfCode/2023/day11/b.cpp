#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

vector<vector<char>> grid, newGrid;
int m, n;

template <typename T> void print_grid(vector<vector<T>> grid) {
  for (int i = 0; i < grid.size(); i++) {
    for (int j = 0; j < grid[0].size(); j++)
      cout << grid[i][j];
    cout << '\n';
  }
  cout << '\n';
}

int main() {
  // read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  while (getline(file, line)) {
    vector<char> row(line.begin(), line.end());
    grid.push_back(row);
  }

  m = grid.size();
  n = grid[0].size();

  // 1. Find cells that are expanded

  // row-wise => horizontal
  vector<int> rowPositions;
  for (int i = 0; i < m; i++) {
    bool isEmpty = true;
    for (int j = 0; j < n; j++) {
      if (grid[i][j] != '.')
        isEmpty = false;
    }

    if (isEmpty) {
      rowPositions.push_back(i);
    }
  }

  // column-wise => vertical
  vector<int> colPositions;
  for (int j = 0; j < n; j++) {
    bool isEmpty = true;
    for (int i = 0; i < m; i++) {
      if (grid[i][j] != '.')
        isEmpty = false;
    }

    if (isEmpty) {
      colPositions.push_back(j);
    }
  }

  // mark each cell as expanded or not
  vector<vector<bool>> isExpanded(m, vector<bool>(n, false));

  // marking galaxies row-wise
  for (const int i : rowPositions) {
    for (int j = 0; j < n; j++) {
      isExpanded[i][j] = true;
    }
  }

  // marking galaxies columns-wise
  for (const int j : colPositions) {
    for (int i = 0; i < m; i++) {
      isExpanded[i][j] = true;
    }
  }

  print_grid(isExpanded);

  // 2. find all positions of galaxies
  vector<pair<int, int>> galaxiesPositions;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (grid[i][j] == '#') {
        galaxiesPositions.push_back({i, j});
      }
    }
  }

  // 3. ~~Compute Floyd-Warshall for shortest path~~ => Manhattan distance
  // modified [wiki](https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm)

  const int EXPANDED_DIST = 1000000;
  long long totalDistance = 0;
  for (int i = 0; i < galaxiesPositions.size(); i++) {
    for (int j = i + 1; j < galaxiesPositions.size(); j++) {
      //
      int r1 = galaxiesPositions[i].first;
      int c1 = galaxiesPositions[i].second;
      int r2 = galaxiesPositions[j].first;
      int c2 = galaxiesPositions[j].second;

      // compute width distance
      int widthDistance = 0;
      for (int k = min(c1, c2); k < max(c1, c2); k++) {
        if (isExpanded[r1][k]) {
          widthDistance += EXPANDED_DIST;
        } else {
          widthDistance += 1;
        }
      }

      // compute height distance
      int heightDistance = 0;
      for (int k = min(r1, r2); k < max(r1, r2); k++) {
        if (isExpanded[k][c1]) {
          heightDistance += EXPANDED_DIST;
        } else {
          heightDistance += 1;
        }
      }

      //
      totalDistance += widthDistance + heightDistance;
    }
  }

  cout << "Total Distance: " << totalDistance << "\n";

  return 0;
}
