#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <string_view>
#include <vector>

using namespace std;

template <typename T> void print_grid(const vector<vector<T>> &grid) {
  for (const auto &row : grid) {
    for (const auto &c : row) {
      cout << c << "";
    }
    cout << "\n";
  }
}

template <typename T>
vector<vector<char>> getTransposeMatrix(const vector<vector<T>> grid) {
  size_t m = grid.size();
  size_t n = grid[0].size();

  vector<vector<T>> transposedMatrix;
  for (int j = 0; j < n; j++) {
    vector<T> row;
    for (int i = 0; i < m; i++) {
      row.push_back(grid[i][j]);
    }
    transposedMatrix.push_back(row);
  }

  return transposedMatrix;
}

int getTotalLoad(const vector<vector<char>> &grid) {
  // strategy: find the next '.'

  int totalLoad = 0;

  for (auto row : grid) {
    queue<int> emptyPositions;
    int m = row.size();

    string row_str(row.begin(), row.end());
    // cout << "Row: " << row_str << "\n";

    for (int i = 0; i < m; i++) {
      if (row[i] == '.') {
        // cout << i << ". \n";
        emptyPositions.push(i);
      } else if (row[i] == '#') {
        // cout << i << "# \n";
        // empty queue
        while (!emptyPositions.empty()) {
          emptyPositions.pop();
        }
      } else if (row[i] == 'O') {
        // cout << i << " 0 \n";
        if (emptyPositions.empty()) {
          totalLoad += m - i;
        } else {
          totalLoad += m - emptyPositions.front();
          emptyPositions.pop();
          emptyPositions.push(i);
        }
        // cout << "Total Load: " << totalLoad << "\n";
      }
    }
    // cout << "\n";
  }

  return totalLoad;
}

int main() {
  // 1. read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  vector<vector<char>> grid;

  while (getline(file, line)) {
    vector<char> row;
    for (char c : line) {
      row.push_back(c);
    }
    grid.push_back(row);
  }

  // print_grid(grid);

  // 2. [ PART A - Compute Total Load ]

  // - transpose matrix
  vector<vector<char>> transposedMatrix = getTransposeMatrix(grid);
  // print_grid(transposedMatrix);

  // - compute total load
  int totalLoad = getTotalLoad(transposedMatrix);
  cout << "Total Load: " << totalLoad << "\n";

  return 0;
}
