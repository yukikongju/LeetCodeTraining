#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// struct IslandString {
//   // '.': 0 ; '#': 1
//   vector<string> valley;

//   void print() {
//     for (string &row : valley) {
//       cout << row << "\n";
//     }
//     cout << "\n";
//   }
// };

struct Island {
  vector<vector<int>> valley;

  void print() {
    for (auto &row : valley) {
      for (auto &c : row) {
        cout << c;
      }
      cout << "\n";
    }
    cout << "\n";
  }
};

int main() {
  // 1. read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;
  vector<Island> islands;
  Island island;

  while (getline(file, line)) {
    if (line.empty()) {
      islands.push_back(island);
      island = Island(); // reset island
    } else {
      // replace '.': 0; '#': 1
      vector<int> row;
      for (auto &c : line) {
        if (c == '.') {
          row.push_back(0);
        } else {
          row.push_back(1);
        }
      }
      island.valley.push_back(row);
    }
  }
  islands.push_back(island);

  for (auto &island : islands) {
    island.print();
  }

  // 2.

  return 0;
}
