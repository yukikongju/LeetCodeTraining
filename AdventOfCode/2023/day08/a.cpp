#include <bits/stdc++.h>
#include <fstream>
#include <string>
using namespace std;

struct Node {
  string value, left, right;

  // Note: we shouldn't create a constructor for Node because we can't access it
  // in map Node(string value, string left, string right)
  //     : value(value), left(left), right(right) {}
};

int main() {
  // 1. read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;

  // read instruction
  string instructions;
  getline(file, line);
  istringstream ss(line);
  ss >> instructions;

  // create network
  map<string, Node> nodes;
  getline(file, line);
  while (getline(file, line)) {
    // string value, left, right;
    Node node;
    node.value = line.substr(0, 3);
    node.left = line.substr(7, 3);
    node.right = line.substr(12, 3);
    nodes.insert({node.value, node});
  }

  // print
  // cout << instructions << '\n';
  // for (const auto &node : nodes) {
  //   cout << node.second.value << ' ' << node.second.left << ' '
  //        << node.second.right << '\n';
  // }

  // [ PART 1 - count number of steps required to reach ZZZ ]
  string current = "AAA";
  int steps = 0;
  bool hasReachedEnd = false;
  while (!hasReachedEnd) {
    char direction = instructions[steps % instructions.size()];
    if (direction == 'L') {
      current = nodes[current].left;
    } else {
      current = nodes[current].right;
    }

    // check if we reached the end
    if (current == "ZZZ")
      hasReachedEnd = true;
    steps += 1;
  }

  cout << "[ PART 1 ] Number of steps to reach ZZZ: " << steps << '\n';

  return 0;
}
