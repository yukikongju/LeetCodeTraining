#include <bits/stdc++.h>
using namespace std;

struct Number {
  int value, row, col;
};

struct Star {
  int row, col;
  set<int> numbers;

  Star(int i, int j) : row(i), col(j) {}

  // define comparison operator to use map
  bool operator<(const Star &other) const {
    return (row < other.row) || (row == other.row && col < other.col);
  }
};

int m, n;
vector<vector<char>> grid;
map<Star, set<int>> gearCandidates;
vector<pair<int, int>> directions = {
    {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {0, -1}, {1, 1}, {1, 0}, {1, -1},
};

int base10_digits(int a, char b) { return 10 * a + (b - '0'); }

void addAdjacent(int i, int j, int value) {
  for (const auto &dir : directions) {
    int x = i + dir.first;
    int y = j + dir.second;
    if (0 <= x && x < m && 0 <= y && y < n && grid[x][y] == '*') {
      gearCandidates[Star(x, y)].insert(value);
      // cout << x << ' ' << y << ' ' << value << '\n';
    }
  }
}

int main() {
  // read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  while (getline(file, line)) {
    vector<char> row;
    for (auto c : line)
      row.push_back(c);
    grid.push_back(row);
  }

  // find all numbers starting pos
  m = grid[0].size(), n = grid.size();
  vector<Number> numbers;
  for (int i = 0; i < m; i++) {
    int j = 0;
    while (j < n) {
      if (isdigit(grid[i][j])) {
        vector<char> digits;
        Number candidate;
        candidate.row = i;
        candidate.col = j;
        while (j < n && isdigit(grid[i][j])) {
          digits.push_back(grid[i][j]);
          j++;
        }
        // init candidate
        string str(digits.begin(), digits.end());
        candidate.value = stoi(str);
        numbers.push_back(candidate);
      } else {
        j++;
      }
    }
  }

  // print numbers in grid
  // for (const auto c : numbers)
  //   cout << c.value << ' ' << c.row << ' ' << c.col << '\n';
  // cout << '\n';

  // [ PART 2 - Compute gear ratio]
  // 0. find candidate position and initialize map
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (grid[i][j] == '*') {
        gearCandidates.insert({Star(i, j), {}});
      }
    }
  }

  // 1. compute number of adjacent number for each *
  for (auto &c : numbers) {
    // get all * positions adjacent to candidates
    int l = c.value > 0 ? (int)log10((double)c.value) + 1 : 1;
    for (int k = 0; k < l; k++) {
      addAdjacent(c.row, c.col + k, c.value);
    }
  }

  // print candidates
  // for (auto &c : gearCandidates) {
  //   cout << c.first.row << ' ' << c.first.col << ' ' << '\n';
  //   for (auto &num : c.second)
  //     cout << num << ' ';
  //   cout << '\n';
  // }

  // 2. compute sum of gear ratio
  int gearRatioSum = 0;
  for (auto &c : gearCandidates) {
    if (c.second.size() == 2) {
      gearRatioSum +=
          accumulate(c.second.begin(), c.second.end(), 1, multiplies<int>());
    }
  }

  cout << "[ Part 2 ] Gear Ratio Sum : " << gearRatioSum << '\n';

  return 0;
}
