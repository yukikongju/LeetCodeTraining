#include <bits/stdc++.h>

#define ll long long
#define mod 1000000007;

using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> coins(n);
  for (int i = 0; i < n; i++)
    cin >> coins[i + 1];

  sort(coins.begin(), coins.end());

  vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

  for (int i = 1; i < n + 1; ++i) {
    for (int j = 0; j < m + 1; ++j) {
      if (j == 0)
        dp[i][j] = 1;
      else {
        int left = ((j - coins[i]) >= 0) ? dp[i][j - coins[i]] : 0;
        int top = (i - 1 >= 0) ? dp[i - 1][j] : 0;
        dp[i][j] = (left + top) % mod;
      }
    }
  }

  cout << dp[n][m] << '\n';
}
