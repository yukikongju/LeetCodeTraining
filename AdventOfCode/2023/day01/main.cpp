#include <bits/stdc++.h>
#include <cctype>
#include <string>

using namespace std;

int main() {
  // string FILENAME = "../inputs/1.txt";
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  vector<string> inputs;
  while (getline(file, line)) {
    inputs.push_back(line);
  }

  // for (auto &c : inputs)
  //   cout << c << '\n';

  // PART 1 - Compute calibration value from first and last number concatenation
  int calibrationValue = 0;
  for (auto input : inputs) {
    vector<int> digits;
    // get all digits
    for (char l : input) {
      // cout << l;
      if (isdigit(l))
        digits.push_back(l - '0');
    }

    // get calibration value with first and last digits
    int val = digits[0] * 10 + digits.back();
    // cout << val << '\n';
    calibrationValue += val;
  }

  cout << "PART 1 - Calibration Value: " << calibrationValue << '\n';

  // PART 2 - Caliibration value spelled out with letter

  int calibrationValue2 = 0;
  map<string, int> wordNumberDict = {
      {"one", 1}, {"two", 2},   {"three", 3}, {"four", 4}, {"five", 5},
      {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}, {"zero", 0},
  };

  for (auto t : inputs) {
    // get digits
    vector<int> digits;
    for (int i = 0; i < t.size(); i++) {
      if (isdigit(t[i])) {
        digits.push_back(t[i] - '0');
      }
      for (const auto &pair : wordNumberDict) {
        if ((t.size() >= i + pair.first.size()) &&
            (t.substr(i, pair.first.size()) == pair.first)) {
          digits.push_back(pair.second);
        }
      }
    }

    // compute calibration value
    int val = digits[0] * 10 + digits.back();
    calibrationValue2 += val;
  }

  cout << "PART 2 - Calibration Value: " << calibrationValue2 << '\n';

  return 0;
}
