#include <bits/stdc++.h>
#include <fstream>

#define ll long long
#define inf (1LL << 60)

using namespace std;

int main() {
  // 1. read inputs
  int mod = 1e9 + 7;
  int N;
  cin >> N;

  vector<vector<char>> grid(N, vector<char>(N, 0));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++)
      cin >> grid[i][j];
  }

  // 2.
  vector<vector<int>> dp(N, vector<int>(N, 0));
  dp[0][0] = 1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (grid[i][j] == '.') {
        if (i - 1 >= 0)
          (dp[i][j] += dp[i - 1][j]) %= mod;
        if (j - 1 >= 0)
          (dp[i][j] += dp[i][j - 1]) %= mod;
      } else {
        dp[i][j] = 0;
      }
    }
  }

  cout << dp[N - 1][N - 1] << '\n';
  // for (int i = 0; i < N; ++i) {
  //   for (int j = 0; j < N; ++j)
  //     cout << dp[i][j] << ' ';
  //   cout << '\n';
  // }

  return 0;
}
