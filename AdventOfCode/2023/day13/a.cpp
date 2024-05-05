#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Island {
  vector<string> valley;

  void print() {
    for (string &row : valley) {
      cout << row << "\n";
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
      island.valley.push_back(line);
    }
  }
  islands.push_back(island);

  // for (auto &island : islands) {
  //   island.print();
  // }

  // 2.

  return 0;
}
