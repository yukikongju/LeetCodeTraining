#include <bits/stdc++.h>
#include <numeric>
using namespace std;

int main() {
  // 1. read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  vector<vector<int>> histories;

  while (getline(file, line)) {
    vector<int> history;
    istringstream ss(line);
    int number;
    while (ss >> number)
      history.push_back(number);
    histories.push_back(history);
  }

  // 2. [ PART 1 - Compute sum of extrapolated values ]
  vector<int> extrapolatedValues;
  for (auto &history : histories) {
    // compute differences
    vector<vector<int>> differences;
    differences.push_back(history);

    bool isDifferenceZero = false;
    while (!isDifferenceZero) {
      // compute differences
      vector<int> difference;
      auto lastVector = differences.back();
      for (int i = 0; i < lastVector.size() - 1; i++) {
        difference.push_back(lastVector[i + 1] - lastVector[i]);
      }
      differences.push_back(difference);

      // check if all difference is null to exit loop
      bool isZero = true;
      for (auto &n : difference)
        if (n != 0)
          isZero = false;
      isDifferenceZero = isZero;
    }

    // print
    // for (auto &difference : differences) {
    //   for (auto &d : difference)
    //     cout << d << ' ';
    //   cout << '\n';
    // }

    // get extrapolated value from differences
    int value =
        accumulate(differences.begin(), differences.end(), 0,
                   [](int partialSum, const std::vector<int> &innerVec) {
                     return partialSum + innerVec.back();
                   });
    extrapolatedValues.push_back(value);
  }

  // print
  // for (auto &n : extrapolatedValues)
  //   cout << n << ' ';

  int sum = accumulate(extrapolatedValues.begin(), extrapolatedValues.end(), 0);
  cout << "[ PART 1 ] Extrapolated Value Sum: " << sum << '\n';

  return 0;
}
