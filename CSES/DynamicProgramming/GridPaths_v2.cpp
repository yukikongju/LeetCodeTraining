#include <bits/stdc++.h>
#include <fstream>

#define mod 10000000007
#define ll long long
#define inf (1LL << 60)

using namespace std;

int main() {
  // 1. read inputs
  int N;
  cin >> N;

  vector<vector<char>> grid(N, vector<char>(N));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++)
      cin >> grid[i][j];
  }

  // 2.
  vector<vector<ll>> dp(N, vector<ll>(N, -1));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == 0 && j == 0)
        dp[i][j] = (grid[i][j] == '.') ? 0 : -1;
      else if (grid[i][j] == '.') {
        ll top = (i - 1 >= 0 && grid[i - 1][j] == '.') ? dp[i - 1][j] : inf;
        ll left = (j - 1 >= 0 && grid[i][j - 1] == '.') ? dp[i][j - 1] : inf;
        dp[i][j] = (min(top, left) + 1) % mod;
      }
    }
  }

  // cout << dp[N - 1][N - 1] << '\n';
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j)
      cout << dp[i][j] << ' ';
    cout << '\n';
  }

  return 0;
}
