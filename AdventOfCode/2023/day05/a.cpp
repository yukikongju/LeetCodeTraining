#include <cstdio>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

struct Map {
  int source, destination, range;
};

struct Mapping {
  vector<Map> maps;
};

int main() {
  // 1. read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;
  int num;

  // read seeds
  vector<int> seeds;
  getline(file, line);
  size_t pos = line.find(':');
  stringstream ss(line.substr(pos + 1));
  while (ss >> num) {
    seeds.push_back(num);
  }

  // read maps
  // vector<vector<int>> maps;
  // vector<string> almanacNames = {"soil",    "fertilizer",  "water",
  //                                "light",   "temperature", "humidity",
  //                                "location"};

  getline(file, line);
  vector<Mapping> mappings;

  while (getline(file, line)) {
    Mapping mapping;
    if (line.empty()) {
      // skipping line - with seed-to-xxx map
      getline(file, line);

      //
      while (getline(file, line)) {
        if (line.empty()) {
          break;
        }
        Map map;
        istringstream iss(line);
        iss >> map.destination >> map.source >> map.range;
        mapping.maps.push_back(map);
      }
      // getline(file, line);

      mappings.push_back(mapping);
    }

    // current line is soil-to-xxx map

    //
    // while (getline(file, line)) {
    //   if (line.empty()) {
    //     break;
    //   }
    //   Map map;
    //   istringstream iss(line);
    //   iss >> map.destination >> map.source >> map.range;
    //   mapping.maps.push_back(map);
    // }
    // getline(file, line);

    Map map;
    istringstream iss(line);
    iss >> map.destination >> map.source >> map.range;
    mappings.back().maps.push_back(map);
    getline(file, line);
  }

  // print mappings
  for (const auto &mapping : mappings) {
    for (const auto &map : mapping.maps) {
      cout << map.destination << ' ' << map.source << ' ' << map.range << '\n';
    }
    cout << "-- \n";
  }

  // 2.

  return 0;
}
