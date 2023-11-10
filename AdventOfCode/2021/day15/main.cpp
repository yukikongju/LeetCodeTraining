#include <bits/stdc++.h>
#include <string>

using namespace std;

void print_grid(vector<vector<int>> &grid) {
  for (auto &row : grid) {
    for (auto &c : row)
      cout << c;
    cout << '\n';
  }
}

void print_dp(vector<vector<int>> &dp) {
  for (auto &row : dp) {
    for (auto &c : row)
      cout << c << ' ';
    cout << '\n';
  }
}

int getLowestRisk(vector<vector<int>> &grid) {
  int m = grid.size();
  int n = grid[0].size();
  vector<vector<int>> dp(m, vector<int>(n, 0));

  int sumCol = 0;
  int sumRow = 0;
  for (int i = 0; i < m; i++) {
    sumCol += grid[i][0];
    dp[i][0] = sumCol;
  }
  for (int j = 0; j < n; j++) {
    sumRow += grid[0][j];
    dp[0][j] = sumRow;
  }

  // dp[0][0] = 0;

  for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
      int top = dp[i - 1][j];
      int left = dp[i][j - 1];
      dp[i][j] = min(top, left) + grid[i][j];
    }
  }

  print_dp(dp);

  return dp[m - 1][n - 1] - grid[0][0];
  // return dp[m - 1][n - 1];
}

int main() {
  // -- read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;
  vector<vector<int>> grid;
  while (getline(file, line)) {
    vector<int> row;
    for (auto &c : line)
      row.push_back(c - '0');
    grid.push_back(row);
  }

  // print_grid(grid);
  // cout << '\n';

  // [ PART 1 ]

  int lowestRisk = getLowestRisk(grid);
  cout << "[PART 1] Mimimum risk level: " << lowestRisk << '\n';

  // [ PART 2 ]

  // make full grid
  int m = grid.size();
  int n = grid[0].size();
  int FULL_SIZE = 5;
  vector<vector<int>> fullGrid(m * FULL_SIZE, vector<int>(n * FULL_SIZE, 0));
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      int val = grid[i][j];
      for (int k = 0; k < FULL_SIZE; k++) {
        fullGrid[i + k * m][j] = val;
        fullGrid[i][j + k * n] = val;
        if (val == 9)
          val = 1;
        else
          val += 1;
      }
    }
  }

  //
  for (int i = m; i < m * FULL_SIZE; i++) {
    for (int j = 0; j < n; j++) {
      int val = fullGrid[i][j];
      for (int k = 0; k < FULL_SIZE; k++) {
        fullGrid[i][j + k * n] = val;
        if (val == 9)
          val = 1;
        else
          val += 1;
      }
    }
  }

  //
  // print_grid(fullGrid);

  //

  int lowestRiskFull = getLowestRisk(fullGrid);

  cout << "[PART 2] Lowest Risk Full Grid: " << lowestRiskFull << '\n';

  return 0;
}
