// Idea: each subset need to be n(n+1) / 4 => knapsack 0/1
// top = not take; left = take

#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main() {
  int n;
  cin >> n;
  int mod = 1e9 + 7;

  int totalSum = n * (n + 1) / 2;
  if (totalSum % 2 != 0) {
    cout << 0 << '\n';
    // exit(0);
    return 0;
  }

  int target = totalSum / 2;

  vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));
  dp[0][0] = 1;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= target; j++) {
      int top = dp[i - 1][j];
      int left = (j - i >= 0) ? dp[i - 1][j - i] : 0;
      (dp[i][j] += top + left) %= mod;
    }
  }

  cout << dp[n - 1][target] << '\n';

  return 0;
}
