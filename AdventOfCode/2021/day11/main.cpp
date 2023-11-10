#include <bits/stdc++.h>
#include <fstream>
#include <string>
#include <utility>

using namespace std;

void print_grid(vector<vector<int>> &grid) {
  for (auto &row : grid) {
    for (auto &c : row) {
      cout << c;
    }
    cout << '\n';
  }
}

int main() {
  vector<vector<int>> grid;
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;

  while (getline(file, line)) {
    vector<int> row;
    for (auto &c : line)
      row.push_back(c - '0');
    grid.push_back(row);
  }

  print_grid(grid);

  int n = grid.size();
  int m = grid[0].size();

  // [ PART 1 ]
  int numSteps = 100;
  int numFlashes = 0;
  vector<pair<int, int>> neighbors = {{0, 1},   {0, -1}, {1, 0},  {-1, 0},
                                      {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

  for (int k = 0; k < numSteps; k++) {
    stack<pair<int, int>> s;
    vector<vector<bool>> hasFlashed(m, vector<bool>(n, false));

    // increment all positions + if explode
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 9) {
          grid[i][j] = 0;
          s.push(make_pair(i, j));
          numFlashes += 1;
          hasFlashed[i][j] = true;
        } else {
          grid[i][j] += 1;
        }
      }
    }

    // cout << '\n';
    // cout << "Step " << k + 1 << '\n';
    // print_grid(grid);
    // cout << '\n';

    // make neighbor explodes
    while (!s.empty()) {
      pair<int, int> position = s.top();
      s.pop();

      for (auto &neighbor : neighbors) {
        int x = position.first + neighbor.first;
        int y = position.second + neighbor.second;

        if ((0 <= x && x < m) && (0 <= y && y < n)) {
          if ((grid[x][y] == 9) && (!hasFlashed[x][y])) {
            grid[x][y] = 0;
            s.push(make_pair(x, y));
            numFlashes += 1;
            hasFlashed[x][y] = true;
            // } else {
            //   grid[x][y] += 1;
            // }
          } else if (grid[x][y] != 0) {
            grid[x][y] += 1;
          }
        }
      }
    }
    // print_grid(grid);
    // cout << "Num Flashes: " << numFlashes << '\n';
  }

  cout << "[PART 1] Num Flashes: " << numFlashes << '\n';

  // [ PART 2 ]

  return 0;
}
