#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main() {

  string s1, s2;
  cin >> s1 >> s2;

  int n = s1.size();
  int m = s2.size();

  //
  vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
  for (int i = 0; i < m + 1; ++i) {
    for (int j = 0; j < n + 1; ++j) {
      if (i == 0)
        dp[0][j] = j;
      else if (j == 0)
        dp[i][0] = i;
      else {
        int add = dp[i - 1][j] + 1;
        int sub = dp[i][j - 1] + 1;
        int delta = (s1[j - 1] == s2[i - 1]) ? 0 : 1;
        int replace = dp[i - 1][j - 1] + delta;
        dp[i][j] = min({add, sub, replace});
      }
    }
  }

  // for (int i = 0; i < m + 1; i++) {
  //   for (int j = 0; j < n + 1; j++) {
  //     cout << dp[i][j] << ' ';
  //   }
  //   cout << '\n';
  // }

  cout << dp[m][n] << '\n';

  return 0;
}
