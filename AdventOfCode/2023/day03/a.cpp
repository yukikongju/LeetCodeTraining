#include <bits/stdc++.h>
using namespace std;

// finding all unique symbols
// grep -o '[^[:digit:].]' your_file.txt | sort -u

int m, n;
vector<vector<char>> grid;

struct Number {
  int value, row, col;
};

int base10_digits(int a, char b) { return 10 * a + (b - '0'); }

bool dfs(int i, int j) {
  // bool hasSymbolAdjacent = false;
  vector<char> symbols = {'*', '-', '+', '/', '!', '@',
                          '#', '$', '%', '&', '='};
  vector<pair<int, int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1},
                                       {1, 1},   {1, 0},  {1, -1}, {0, -1}};

  // check if symbol around position
  for (const auto &dir : directions) {
    int x = i + dir.first;
    int y = j + dir.second;
    if (0 <= x && x < m && 0 <= y && y < n) {
      bool found =
          (find(symbols.begin(), symbols.end(), grid[x][y]) != symbols.end());
      if (found)
        return true;
    }
  }

  // return hasSymbolAdjacent;
  return false;
}

int main() {
  // read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  // vector<vector<char>> grid;
  string line;
  while (getline(file, line)) {
    vector<char> row;
    for (auto c : line)
      row.push_back(c);
    grid.push_back(row);
  }

  // [ PART 1 - ]

  // find all numbers starting pos
  m = grid[0].size(), n = grid.size();
  vector<Number> candidates;
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
        candidates.push_back(candidate);
      } else {
        j++;
      }
    }
  }

  // printing grid
  // for (const auto c : candidates)
  //   cout << c.value << ' ' << c.row << ' ' << c.col << '\n';

  // check if number if a part number ie if symbol adjacent
  vector<int> validNumbers;
  for (auto &c : candidates) {
    bool isValid = false;
    int l = c.value > 0 ? (int)log10((double)c.value) + 1 : 1; // number of
    for (int k = 0; k < l; k++) {
      // find if there is a symbol adjacent
      isValid |= dfs(c.row, c.col + k);
    }
    if (isValid)
      validNumbers.push_back(c.value);
  }

  // compute sum
  // for (auto &num : validNumbers)
  //   cout << num << '\n';
  int schematicSum = accumulate(validNumbers.begin(), validNumbers.end(), 0);
  cout << "[ PART 1 ] Sum Engine schematic: " << schematicSum << '\n';

  return 0;
}
