#include <bits/stdc++.h>
#include <fstream>
#include <string>
#include <utility>
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

vector<vector<char>> expanded_grid(vector<int> rowPositions,
                                   vector<int> colPositions) {

  vector<vector<char>> newGrid;
  for (int i = 0; i < m; i++) {
    vector<char> newRow;
    for (int j = 0; j < n; j++) {
      newRow.push_back(grid[i][j]);
      if (find(colPositions.begin(), colPositions.end(), j) !=
          colPositions.end()) {
        newRow.push_back('.');
      }
    }

    //
    vector<char> emptyRow;
    for (int k = 0; k < newRow.size(); k++)
      emptyRow.push_back('.');
    newGrid.push_back(newRow);
    if (find(rowPositions.begin(), rowPositions.end(), i) !=
        rowPositions.end()) {
      newGrid.push_back(emptyRow);
    }
  }

  return newGrid;
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

  // [ PART 1 - Sum of all paths lengths]

  // 1. expand universe

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

  // expand grid using row and col positions
  auto newGrid = expanded_grid(rowPositions, colPositions);
  print_grid(newGrid);

  m = newGrid.size();
  n = newGrid[0].size();

  // 2. replace # by numbers
  // int numGalaxies = 0;
  // for (int i = 0; i < m; i++) {
  //   for (int j = 0; j < n; j++) {
  //     if (newGrid[i][j] == '#') {
  //       // newGrid[i][j] = 'x';
  //     }
  //   }
  // }
  // print_grid(newGrid);

  // 2. find all positions of galaxies
  vector<pair<int, int>> galaxiesPositions;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (newGrid[i][j] == '#') {
        galaxiesPositions.push_back({i, j});
      }
    }
  }

  // 3. compute all shortest paths with floyd-warshall // manhattan distance
  int totalDistance = 0;
  for (int i = 0; i < galaxiesPositions.size(); i++) {
    for (int j = i + 1; j < galaxiesPositions.size(); j++) {
      // compute distance between galaxy A and B
      int dist = abs(galaxiesPositions[i].first - galaxiesPositions[j].first) +
                 abs(galaxiesPositions[i].second - galaxiesPositions[j].second);
      totalDistance += dist;
    }
  }

  cout << "[ PART 1 ] Total Sum: " << totalDistance << '\n';

  return 0;
}
