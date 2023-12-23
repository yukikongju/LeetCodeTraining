#include <bits/stdc++.h>
#include <fstream>
#include <functional>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;

int main() {
  // 1. read inputs
  vector<int> times, distances;
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;

  // read times
  getline(file, line);
  size_t pos = line.find(':');
  stringstream ss(line.substr(pos + 1));
  string timesPart;
  getline(ss, timesPart);
  istringstream timesStream(line.substr(pos + 1));
  int num;
  while (timesStream >> num) {
    times.push_back(num);
  }

  // read distances
  getline(file, line);
  pos = line.find(':');
  stringstream ss2(line.substr(pos + 1));
  getline(ss, timesPart);
  istringstream distancesStream(line.substr(pos + 1));
  int distance;
  while (distancesStream >> distance) {
    distances.push_back(distance);
  }

  // print
  for (auto &t : times)
    cout << t << ' ';
  cout << '\n';
  for (auto &d : distances)
    cout << d << ' ';
  cout << '\n';

  // [ PART 1 - Compute different number of ways]
  vector<int> ways;
  const int SPEED = 1;
  for (int i = 0; i < times.size(); i++) {
    int way = 0;
    for (int t = 0; t < times[i]; t++) {
      // time = time holding button + speed * remaining time
      int dist = SPEED * t * (times[i] - t);
      if (dist > distances[i])
        way += 1;
    }
    ways.push_back(way);
  }

  // print number of ways
  for (const auto &w : ways)
    cout << w << ' ';
  cout << '\n';

  int total = accumulate(ways.begin(), ways.end(), 1, multiplies<int>());
  cout << "[ PART 1 ] Total: " << total << '\n';

  return 0;
}
