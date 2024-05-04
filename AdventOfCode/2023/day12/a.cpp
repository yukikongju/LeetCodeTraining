#include <fstream>
#include <ios>
#include <iostream>
#include <sstream>
#include <string>
#include <string_view>
#include <vector>

using namespace std;

struct Spring {
  string arrangement;
  vector<int> groupings;

  void print() {
    cout << "Arragement: " << arrangement << "; Groupings: ";
    for (const int g : groupings) {
      cout << g << " ";
    }
    cout << "\n";
  }
};

Spring parse_spring(const string &line) {
  Spring spring;
  string groupings_str;

  // if we use string_view instead, but defeats purpose of string_view
  // istringstream ss(string(line), ios_base::in);
  istringstream ss(line);
  ss >> spring.arrangement >> groupings_str;

  // process groupings string
  istringstream gss(groupings_str);
  string token;
  while (getline(gss, token, ',')) {
    spring.groupings.push_back(stoi(token));
  }

  return spring;
}

int main() {
  // 1. Read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;

  vector<Spring> springs;
  while (getline(file, line)) {
    springs.push_back(parse_spring(line));
  }

  for (auto &s : springs) {
    s.print();
  }

  // 2.

  return 0;
}
