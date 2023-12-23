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

  // concatenate all times and distances
  stringstream timeStream;
  for (const auto &t : times)
    timeStream << t;
  long long time = stol(timeStream.str());

  stringstream distanceStream;
  for (const auto &d : distances)
    distanceStream << d;
  long long distMax = stol(distanceStream.str());

  // [ PART 2 - ]
  const int SPEED = 1;
  long long ways = 0;
  for (int k = 0; k < time; k++) {
    long long d = SPEED * k * (time - k);
    if (d > distMax)
      ways += 1;
  }

  cout << "[ PART 2 ] Total: " << ways << '\n';

  return 0;
}
