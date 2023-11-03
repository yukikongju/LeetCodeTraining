#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
  // # O(n^2)
  int n;
  cin >> n;

  vector<int> dp(n + 1, 1e9);
  dp[0] = 0;

  for (int i = 0; i < n + 1; ++i) {
    for (char c : to_string(i)) {
      dp[i] = min(dp[i], dp[i - c + '0'] + 1);
    }
  }

  cout << dp[n] << '\n';

  return 0;
}
